#!/usr/bin/env node
/**
 * OneSignal to FCM Migration Script
 * Migrates 240K+ push notification subscribers using streaming
 * 
 * Usage:
 *   node MIGRATION-SCRIPT.js --input onesignal_export.csv
 */

const fs = require('fs');
const { Pool } = require('pg');
const { from: copyFrom } = require('pg-copy-streams');
const { parse } = require('csv-parse');
const { Transform } = require('stream');
const path = require('path');

// PostgreSQL connection
const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  port: process.env.DB_PORT || 5432,
  database: process.env.DB_NAME || 'evil_apples',
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD,
});

/**
 * Device Type Mapping
 * Maps OneSignal's numeric device codes to readable strings
 */
const mapDeviceType = (type) => {
  const types = {
    '0': 'ios',
    '1': 'android',
    '5': 'chrome_web',
    '11': 'windows_phone',
    '3': 'chrome_extension',
  };
  return types[type] || 'unknown';
};

/**
 * Create database table if it doesn't exist
 */
async function createTable() {
  const client = await pool.connect();
  
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS push_subscribers (
        id SERIAL PRIMARY KEY,
        user_id UUID,
        fcm_token VARCHAR(255) UNIQUE NOT NULL,
        platform VARCHAR(50) NOT NULL,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        tags JSONB DEFAULT '{}',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        INDEX idx_user_id (user_id),
        INDEX idx_platform (platform),
        INDEX idx_fcm_token (fcm_token)
      );
    `);
    
    console.log('✅ Database table ready');
  } catch (error) {
    console.error('❌ Table creation failed:', error.message);
    throw error;
  } finally {
    client.release();
  }
}

/**
 * Stream-based migration
 * Processes CSV without loading entire file into memory
 */
async function migrate(inputFile) {
  if (!fs.existsSync(inputFile)) {
    throw new Error(`File not found: ${inputFile}`);
  }
  
  console.log(`📂 Reading: ${inputFile}`);
  console.log('🚀 Starting migration...\n');
  
  const client = await pool.connect();
  let processedCount = 0;
  let errorCount = 0;
  
  try {
    // PostgreSQL COPY for maximum speed
    const dbStream = client.query(copyFrom(
      `COPY push_subscribers (fcm_token, user_id, platform) 
       FROM STDIN WITH (FORMAT csv, DELIMITER ',')`
    ));
    
    // Transform OneSignal CSV rows to our format
    const transformer = new Transform({
      objectMode: true,
      transform(row, encoding, callback) {
        try {
          const platform = mapDeviceType(row.device_type);
          
          // Skip unknown platforms or invalid tokens
          if (platform === 'unknown' || !row.identifier) {
            errorCount++;
            return callback();
          }
          
          // Format: token, user_id, platform
          const userId = row.external_user_id || null;
          const csvLine = `${row.identifier},${userId},${platform}\n`;
          
          processedCount++;
          
          // Progress indicator every 10K
          if (processedCount % 10000 === 0) {
            console.log(`   Processed: ${processedCount.toLocaleString()} tokens...`);
          }
          
          callback(null, csvLine);
        } catch (error) {
          errorCount++;
          callback();
        }
      }
    });
    
    // Stream pipeline: File → Parse → Transform → Database
    await new Promise((resolve, reject) => {
      fs.createReadStream(inputFile)
        .pipe(parse({ columns: true, skip_empty_lines: true }))
        .pipe(transformer)
        .pipe(dbStream)
        .on('finish', resolve)
        .on('error', reject);
    });
    
    console.log('\n✅ Migration complete!');
    console.log(`   Total processed: ${processedCount.toLocaleString()}`);
    console.log(`   Errors/skipped: ${errorCount.toLocaleString()}`);
    
  } catch (error) {
    console.error('\n❌ Migration failed:', error.message);
    throw error;
  } finally {
    client.release();
  }
}

/**
 * Verify migration results
 */
async function verify() {
  console.log('\n🔍 Verifying migration...\n');
  
  const results = await pool.query(`
    SELECT 
      platform,
      COUNT(*) as count
    FROM push_subscribers
    GROUP BY platform
    ORDER BY count DESC;
  `);
  
  console.log('📊 Platform Distribution:');
  results.rows.forEach(row => {
    console.log(`   ${row.platform}: ${parseInt(row.count).toLocaleString()}`);
  });
  
  const total = await pool.query('SELECT COUNT(*) FROM push_subscribers');
  console.log(`\n   Total subscribers: ${parseInt(total.rows[0].count).toLocaleString()}`);
}

/**
 * Main execution
 */
async function main() {
  const args = process.argv.slice(2);
  const inputFile = args[1] || './onesignal_export.csv';
  
  console.log('\n╔════════════════════════════════════════════════╗');
  console.log('║   OneSignal → FCM Migration Tool              ║');
  console.log('║   Evil Apples Push Notification System       ║');
  console.log('╚════════════════════════════════════════════════╝\n');
  
  try {
    // Step 1: Create table
    await createTable();
    
    // Step 2: Migrate data
    await migrate(inputFile);
    
    // Step 3: Verify
    await verify();
    
    console.log('\n🎉 Migration successful! Ready to send pushes.\n');
    
  } catch (error) {
    console.error('\n💥 Fatal error:', error.message);
    process.exit(1);
  } finally {
    await pool.end();
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = { migrate, createTable, verify };
