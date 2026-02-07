/**
 * Local Testing Script
 * Test configuration and connections before deploying
 */

const config = require('../src/config');
const ZohoDeskClient = require('../src/zoho-desk-client');
const RagClient = require('../src/rag-client');

async function runTests() {
  console.log('🧪 Boxie Bot CSR - Local Testing\n');
  console.log('='.repeat(50));

  // Test 1: Configuration
  console.log('\n1️⃣  Testing Configuration...');
  try {
    if (config.isValid()) {
      console.log('   ✅ All required config present');
      console.log(`   - Zoho Desk Org: ${config.zohoDeskOrgId}`);
      console.log(`   - OpenAI Model: ${config.openaiModel}`);
      console.log(`   - Environment: ${config.catalystEnvironment}`);
    } else {
      console.log('   ❌ Missing required configuration');
      console.log('   → Copy .env.example to .env and fill in values');
      process.exit(1);
    }
  } catch (error) {
    console.log('   ❌ Configuration error:', error.message);
    process.exit(1);
  }

  // Test 2: Zoho Desk Connection
  console.log('\n2️⃣  Testing Zoho Desk Connection...');
  try {
    const deskClient = new ZohoDeskClient();
    const result = await deskClient.searchTickets({ limit: 1 });
    
    if (result.success) {
      console.log('   ✅ Zoho Desk connection working');
      console.log(`   - Found ${result.count} tickets`);
    } else {
      console.log('   ❌ Zoho Desk connection failed');
      console.log(`   - Error: ${result.error}`);
      console.log('   → Check ZOHO_DESK_ORG_ID and ZOHO_DESK_API_TOKEN');
    }
  } catch (error) {
    console.log('   ❌ Zoho Desk error:', error.message);
  }

  // Test 3: OpenAI Connection
  console.log('\n3️⃣  Testing OpenAI Connection...');
  try {
    const OpenAI = require('openai');
    const openai = new OpenAI({ apiKey: config.openaiApiKey });
    
    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: 'Say "test successful"' }],
      max_tokens: 10
    });

    if (response.choices[0].message.content) {
      console.log('   ✅ OpenAI connection working');
    }
  } catch (error) {
    console.log('   ❌ OpenAI connection failed');
    console.log(`   - Error: ${error.message}`);
    console.log('   → Check OPENAI_API_KEY');
  }

  // Test 4: RAG Configuration
  console.log('\n4️⃣  Testing RAG Configuration...');
  try {
    const ragClient = new RagClient();
    
    if (ragClient.enabled) {
      console.log('   ✅ RAG enabled');
      console.log(`   - Supabase URL: ${config.supabaseUrl}`);
      console.log('   - Ready for knowledge base indexing');
    } else {
      console.log('   ⚠️  RAG not configured (optional)');
      console.log('   → Set SUPABASE_URL and SUPABASE_SERVICE_KEY to enable');
      console.log('   → System will work without RAG, but with limited knowledge base search');
    }
  } catch (error) {
    console.log('   ❌ RAG error:', error.message);
  }

  // Summary
  console.log('\n' + '='.repeat(50));
  console.log('\n📊 Test Summary:');
  console.log('   Configuration: ✅');
  console.log('   Zoho Desk: Check output above');
  console.log('   OpenAI: Check output above');
  console.log('   RAG: Check output above');
  
  console.log('\n✨ Next Steps:');
  console.log('   1. Fix any failed tests above');
  console.log('   2. Deploy to Catalyst: catalyst deploy');
  console.log('   3. Configure Custom GPT with your Catalyst URLs');
  console.log('   4. Test end-to-end\n');
}

// Run tests
runTests().catch(error => {
  console.error('\n❌ Test suite failed:', error);
  process.exit(1);
});
