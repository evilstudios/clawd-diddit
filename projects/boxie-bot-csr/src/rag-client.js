/**
 * RAG (Retrieval-Augmented Generation) Client
 * Handles semantic search using Supabase + pgvector
 */

const { createClient } = require('@supabase/supabase-js');
const OpenAI = require('openai');
const config = require('./config');

class RagClient {
  constructor() {
    if (!config.isRagEnabled()) {
      console.warn('⚠️  RAG not configured. Set SUPABASE_URL and SUPABASE_SERVICE_KEY');
      this.enabled = false;
      return;
    }

    this.enabled = true;
    this.supabase = createClient(config.supabaseUrl, config.supabaseServiceKey);
    this.openai = new OpenAI({ apiKey: config.openaiApiKey });
    this.embeddingModel = config.openaiEmbeddingModel;
  }

  /**
   * Generate embedding for text
   */
  async generateEmbedding(text) {
    try {
      const response = await this.openai.embeddings.create({
        model: this.embeddingModel,
        input: text
      });

      return response.data[0].embedding;
    } catch (error) {
      console.error('Error generating embedding:', error.message);
      throw error;
    }
  }

  /**
   * Search knowledge base using semantic search
   */
  async search(query, limit = 5) {
    if (!this.enabled) {
      return {
        success: false,
        error: 'RAG not configured'
      };
    }

    try {
      // Generate embedding for query
      const queryEmbedding = await this.generateEmbedding(query);

      // Perform vector similarity search
      const { data, error } = await this.supabase.rpc('match_documents', {
        query_embedding: queryEmbedding,
        match_threshold: 0.7,
        match_count: limit
      });

      if (error) throw error;

      return {
        success: true,
        results: data || []
      };
    } catch (error) {
      console.error('Error searching knowledge base:', error.message);
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Index a document (chunk and store embeddings)
   */
  async indexDocument(document) {
    if (!this.enabled) {
      return {
        success: false,
        error: 'RAG not configured'
      };
    }

    try {
      const { id, title, content, metadata = {} } = document;

      // Chunk the content (simple implementation: split by paragraphs)
      const chunks = this.chunkText(content);

      // Generate embeddings for each chunk
      const records = [];
      for (let i = 0; i < chunks.length; i++) {
        const chunk = chunks[i];
        const embedding = await this.generateEmbedding(chunk);

        records.push({
          document_id: id,
          chunk_index: i,
          title,
          content: chunk,
          embedding,
          metadata: {
            ...metadata,
            total_chunks: chunks.length
          }
        });
      }

      // Insert into Supabase
      const { data, error } = await this.supabase
        .from('documents')
        .insert(records);

      if (error) throw error;

      return {
        success: true,
        indexed: records.length
      };
    } catch (error) {
      console.error('Error indexing document:', error.message);
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Chunk text into smaller pieces (simple implementation)
   */
  chunkText(text, maxChunkSize = 512) {
    const paragraphs = text.split(/\n\n+/);
    const chunks = [];
    let currentChunk = '';

    for (const paragraph of paragraphs) {
      if ((currentChunk + paragraph).length <= maxChunkSize) {
        currentChunk += (currentChunk ? '\n\n' : '') + paragraph;
      } else {
        if (currentChunk) chunks.push(currentChunk);
        currentChunk = paragraph;
      }
    }

    if (currentChunk) chunks.push(currentChunk);

    return chunks;
  }

  /**
   * Delete document from index
   */
  async deleteDocument(documentId) {
    if (!this.enabled) {
      return {
        success: false,
        error: 'RAG not configured'
      };
    }

    try {
      const { error } = await this.supabase
        .from('documents')
        .delete()
        .eq('document_id', documentId);

      if (error) throw error;

      return {
        success: true
      };
    } catch (error) {
      console.error('Error deleting document:', error.message);
      return {
        success: false,
        error: error.message
      };
    }
  }
}

module.exports = RagClient;
