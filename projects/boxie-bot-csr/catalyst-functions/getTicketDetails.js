/**
 * Catalyst Function: getTicketDetails
 * Get complete ticket information including thread
 */

const ZohoDeskClient = require('../src/zoho-desk-client');

module.exports = async (catalystApp) => {
  try {
    const request = catalystApp.request;
    const { ticketId } = request.body;

    if (!ticketId) {
      return catalystApp.response.status(400).json({
        error: 'ticketId is required'
      });
    }

    // Initialize Desk client
    const deskClient = new ZohoDeskClient();

    // Get ticket details
    const ticketResult = await deskClient.getTicketDetails(ticketId);
    
    if (!ticketResult.success) {
      return catalystApp.response.status(500).json({
        error: ticketResult.error
      });
    }

    // Get conversation thread
    const threadResult = await deskClient.getTicketThread(ticketId);

    // Combine ticket data with thread
    const ticket = ticketResult.data;
    const thread = threadResult.success ? threadResult.data : [];

    const response = {
      id: ticket.ticketNumber,
      subject: ticket.subject,
      description: ticket.description,
      status: ticket.status,
      priority: ticket.priority,
      customer: {
        name: ticket.contact?.firstName + ' ' + ticket.contact?.lastName,
        email: ticket.contact?.email
      },
      assignee: ticket.assignee ? {
        name: ticket.assignee.firstName + ' ' + ticket.assignee.lastName,
        email: ticket.assignee.email
      } : null,
      createdTime: ticket.createdTime,
      modifiedTime: ticket.modifiedTime,
      conversation: thread.map(msg => ({
        from: msg.fromEmailAddress || msg.author?.name,
        content: msg.content,
        timestamp: msg.createdTime,
        direction: msg.direction
      }))
    };

    return catalystApp.response.json({
      success: true,
      ticket: response
    });

  } catch (error) {
    console.error('Error in getTicketDetails function:', error);
    return catalystApp.response.status(500).json({
      error: error.message
    });
  }
};
