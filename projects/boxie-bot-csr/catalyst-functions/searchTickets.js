/**
 * Catalyst Function: searchTickets
 * Search Zoho Desk tickets with filters
 */

const ZohoDeskClient = require('../src/zoho-desk-client');

module.exports = async (catalystApp) => {
  try {
    const request = catalystApp.request;
    const { status, priority, assignee, department, limit } = request.body;

    // Initialize Desk client
    const deskClient = new ZohoDeskClient();

    // Search tickets
    const result = await deskClient.searchTickets({
      status,
      priority,
      assignee,
      department,
      limit: limit || 50
    });

    if (!result.success) {
      return catalystApp.response.status(500).json({
        error: result.error
      });
    }

    // Format response for Custom GPT
    const formattedTickets = result.data.map(ticket => ({
      id: ticket.ticketNumber,
      subject: ticket.subject,
      status: ticket.status,
      priority: ticket.priority,
      customer: ticket.contact?.firstName + ' ' + ticket.contact?.lastName,
      createdTime: ticket.createdTime,
      assignee: ticket.assignee?.firstName + ' ' + ticket.assignee?.lastName
    }));

    return catalystApp.response.json({
      success: true,
      count: result.count,
      tickets: formattedTickets
    });

  } catch (error) {
    console.error('Error in searchTickets function:', error);
    return catalystApp.response.status(500).json({
      error: error.message
    });
  }
};
