/**
 * Catalyst Function: generateResponse
 * Generate AI-powered response draft using ticket context + RAG
 */

const OpenAI = require('openai');
const ZohoDeskClient = require('../src/zoho-desk-client');
const RagClient = require('../src/rag-client');
const config = require('../src/config');

module.exports = async (catalystApp) => {
  try {
    const request = catalystApp.request;
    const { ticketId } = request.body;

    if (!ticketId) {
      return catalystApp.response.status(400).json({
        error: 'ticketId is required'
      });
    }

    // Initialize clients
    const deskClient = new ZohoDeskClient();
    const ragClient = new RagClient();
    const openai = new OpenAI({ apiKey: config.openaiApiKey });

    // Get ticket details
    const ticketResult = await deskClient.getTicketDetails(ticketId);
    if (!ticketResult.success) {
      return catalystApp.response.status(500).json({
        error: ticketResult.error
      });
    }

    const ticket = ticketResult.data;

    // Get conversation thread
    const threadResult = await deskClient.getTicketThread(ticketId);
    const thread = threadResult.success ? threadResult.data : [];

    // Search knowledge base for relevant context
    let ragContext = '';
    if (ragClient.enabled) {
      const ragResult = await ragClient.search(ticket.subject + ' ' + ticket.description, 3);
      if (ragResult.success && ragResult.results.length > 0) {
        ragContext = '\n\nRelevant Knowledge Base Articles:\n' + 
          ragResult.results.map(doc => `- ${doc.title}: ${doc.content}`).join('\n');
      }
    }

    // Find similar resolved tickets
    const similarResult = await deskClient.getSimilarResolvedTickets(ticketId, 2);
    let similarContext = '';
    if (similarResult.success && similarResult.data.length > 0) {
      similarContext = '\n\nSimilar Previously Resolved Tickets:\n' +
        similarResult.data.map(t => `- ${t.subject} (Status: ${t.status})`).join('\n');
    }

    // Build context for GPT
    const context = `
Ticket #${ticket.ticketNumber}
Subject: ${ticket.subject}
Status: ${ticket.status}
Priority: ${ticket.priority}
Customer: ${ticket.contact?.firstName} ${ticket.contact?.lastName}

Original Message:
${ticket.description}

Recent Conversation:
${thread.slice(-3).map(msg => 
  `${msg.direction === 'in' ? 'Customer' : 'Agent'}: ${msg.content}`
).join('\n')}
${ragContext}
${similarContext}
`;

    // Generate response using GPT
    const completion = await openai.chat.completions.create({
      model: config.openaiModel,
      messages: [
        {
          role: 'system',
          content: `You are a helpful customer service representative. Generate a professional, empathetic response to the customer's ticket based on the context provided. Follow company policies and SOPs. Keep responses concise but complete.`
        },
        {
          role: 'user',
          content: `Generate a response draft for this support ticket:\n\n${context}`
        }
      ],
      temperature: 0.7,
      max_tokens: 500
    });

    const responseDraft = completion.choices[0].message.content;

    return catalystApp.response.json({
      success: true,
      ticketId: ticket.ticketNumber,
      draft: responseDraft,
      context: {
        hasRagContext: !!ragContext,
        hasSimilarTickets: !!similarContext
      }
    });

  } catch (error) {
    console.error('Error in generateResponse function:', error);
    return catalystApp.response.status(500).json({
      error: error.message
    });
  }
};
