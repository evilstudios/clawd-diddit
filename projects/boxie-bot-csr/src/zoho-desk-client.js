/**
 * Zoho Desk API Client
 * Handles all interactions with Zoho Desk API
 */

const axios = require('axios');
const config = require('./config');

class ZohoDeskClient {
  constructor() {
    this.baseUrl = config.zohoDeskBaseUrl;
    this.orgId = config.zohoDeskOrgId;
    this.apiToken = config.zohoDeskApiToken;

    this.client = axios.create({
      baseURL: this.baseUrl,
      headers: {
        'orgId': this.orgId,
        'Authorization': `Zoho-oauthtoken ${this.apiToken}`,
        'Content-Type': 'application/json'
      }
    });
  }

  /**
   * Search tickets with filters
   */
  async searchTickets({ status, priority, assignee, department, limit = 50, sortBy = 'createdTime' }) {
    try {
      const params = {
        limit,
        sortBy
      };

      // Build search query
      const searchQuery = [];
      if (status) searchQuery.push(`status:${status}`);
      if (priority) searchQuery.push(`priority:${priority}`);
      if (assignee) searchQuery.push(`assigneeId:${assignee}`);
      if (department) searchQuery.push(`departmentId:${department}`);

      if (searchQuery.length > 0) {
        params.searchStr = searchQuery.join(' AND ');
      }

      const response = await this.client.get('/tickets/search', { params });

      return {
        success: true,
        data: response.data.data || [],
        count: response.data.count || 0
      };
    } catch (error) {
      console.error('Error searching tickets:', error.response?.data || error.message);
      return {
        success: false,
        error: error.response?.data?.message || error.message
      };
    }
  }

  /**
   * Get ticket details by ID
   */
  async getTicketDetails(ticketId) {
    try {
      const response = await this.client.get(`/tickets/${ticketId}`);

      return {
        success: true,
        data: response.data
      };
    } catch (error) {
      console.error('Error getting ticket details:', error.response?.data || error.message);
      return {
        success: false,
        error: error.response?.data?.message || error.message
      };
    }
  }

  /**
   * Get ticket conversation thread
   */
  async getTicketThread(ticketId) {
    try {
      const response = await this.client.get(`/tickets/${ticketId}/threads`);

      return {
        success: true,
        data: response.data.data || []
      };
    } catch (error) {
      console.error('Error getting ticket thread:', error.response?.data || error.message);
      return {
        success: false,
        error: error.response?.data?.message || error.message
      };
    }
  }

  /**
   * Get similar resolved tickets (simple text matching for now)
   */
  async getSimilarResolvedTickets(ticketId, limit = 5) {
    try {
      // First get the original ticket
      const ticketResult = await this.getTicketDetails(ticketId);
      if (!ticketResult.success) {
        return ticketResult;
      }

      const originalTicket = ticketResult.data;
      const keywords = this.extractKeywords(originalTicket.subject);

      // Search for resolved tickets with similar keywords
      const searchResult = await this.searchTickets({
        status: 'Closed',
        limit
      });

      if (!searchResult.success) {
        return searchResult;
      }

      // Filter by keyword similarity (basic implementation)
      const similar = searchResult.data.filter(ticket => {
        const ticketText = `${ticket.subject} ${ticket.description}`.toLowerCase();
        return keywords.some(keyword => ticketText.includes(keyword));
      });

      return {
        success: true,
        data: similar.slice(0, limit)
      };
    } catch (error) {
      console.error('Error finding similar tickets:', error.message);
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Extract keywords from text (simple implementation)
   */
  extractKeywords(text) {
    if (!text) return [];

    const stopWords = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'is', 'are', 'was', 'were'];
    
    return text
      .toLowerCase()
      .split(/\s+/)
      .filter(word => word.length > 3 && !stopWords.includes(word))
      .slice(0, 5);
  }

  /**
   * Update ticket
   */
  async updateTicket(ticketId, updates) {
    try {
      const response = await this.client.patch(`/tickets/${ticketId}`, updates);

      return {
        success: true,
        data: response.data
      };
    } catch (error) {
      console.error('Error updating ticket:', error.response?.data || error.message);
      return {
        success: false,
        error: error.response?.data?.message || error.message
      };
    }
  }

  /**
   * Add reply to ticket
   */
  async addReply(ticketId, reply) {
    try {
      const response = await this.client.post(`/tickets/${ticketId}/threads`, {
        contentType: 'html',
        content: reply,
        isPublic: true
      });

      return {
        success: true,
        data: response.data
      };
    } catch (error) {
      console.error('Error adding reply:', error.response?.data || error.message);
      return {
        success: false,
        error: error.response?.data?.message || error.message
      };
    }
  }
}

module.exports = ZohoDeskClient;
