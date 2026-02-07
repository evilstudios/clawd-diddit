/**
 * Catalyst Function: ragSearch
 * Semantic search across knowledge base (SOPs, policies, documentation)
 */

const RagClient = require('../src/rag-client');

module.exports = async (catalystApp) => {
  try {
    const request = catalystApp.request;
    const { query, limit } = request.body;

    if (!query) {
      return catalystApp.response.status(400).json({
        error: 'query is required'
      });
    }

    // Initialize RAG client
    const ragClient = new RagClient();

    if (!ragClient.enabled) {
      return catalystApp.response.status(503).json({
        error: 'RAG service not configured'
      });
    }

    // Search knowledge base
    const result = await ragClient.search(query, limit || 5);

    if (!result.success) {
      return catalystApp.response.status(500).json({
        error: result.error
      });
    }

    // Format results for Custom GPT
    const formattedResults = result.results.map(doc => ({
      title: doc.title,
      content: doc.content,
      relevance: doc.similarity,
      source: doc.metadata?.source || 'knowledge_base'
    }));

    return catalystApp.response.json({
      success: true,
      query,
      results: formattedResults
    });

  } catch (error) {
    console.error('Error in ragSearch function:', error);
    return catalystApp.response.status(500).json({
      error: error.message
    });
  }
};
