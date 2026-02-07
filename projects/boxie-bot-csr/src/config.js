/**
 * Configuration Management
 * Loads environment variables with validation and defaults
 */

require('dotenv').config();

class Config {
  constructor() {
    this.validateRequired();
  }

  // Zoho Desk Configuration
  get zohoDeskOrgId() {
    return process.env.ZOHO_DESK_ORG_ID;
  }

  get zohoDeskApiToken() {
    return process.env.ZOHO_DESK_API_TOKEN;
  }

  get zohoDeskBaseUrl() {
    return process.env.ZOHO_DESK_BASE_URL || 'https://desk.zoho.com/api/v1';
  }

  // OpenAI Configuration
  get openaiApiKey() {
    return process.env.OPENAI_API_KEY;
  }

  get openaiModel() {
    return process.env.OPENAI_MODEL || 'gpt-4';
  }

  get openaiEmbeddingModel() {
    return 'text-embedding-3-small';
  }

  // Supabase Configuration
  get supabaseUrl() {
    return process.env.SUPABASE_URL;
  }

  get supabaseAnonKey() {
    return process.env.SUPABASE_ANON_KEY;
  }

  get supabaseServiceKey() {
    return process.env.SUPABASE_SERVICE_KEY;
  }

  // Catalyst Configuration
  get catalystProjectId() {
    return process.env.CATALYST_PROJECT_ID;
  }

  get catalystEnvironment() {
    return process.env.CATALYST_ENVIRONMENT || 'development';
  }

  // Security
  get apiKey() {
    return process.env.API_KEY;
  }

  // Logging
  get logLevel() {
    return process.env.LOG_LEVEL || 'info';
  }

  // Validation
  validateRequired() {
    const required = [
      'ZOHO_DESK_ORG_ID',
      'ZOHO_DESK_API_TOKEN',
      'OPENAI_API_KEY',
      'API_KEY'
    ];

    const missing = required.filter(key => !process.env[key]);

    if (missing.length > 0) {
      console.warn('⚠️  Missing required environment variables:', missing.join(', '));
      console.warn('⚠️  Copy .env.example to .env and configure the values');
    }
  }

  // Helper: Check if all required configs are present
  isValid() {
    return !!(
      this.zohoDeskOrgId &&
      this.zohoDeskApiToken &&
      this.openaiApiKey &&
      this.apiKey
    );
  }

  // Helper: Check if RAG is configured
  isRagEnabled() {
    return !!(
      this.supabaseUrl &&
      this.supabaseServiceKey
    );
  }
}

module.exports = new Config();
