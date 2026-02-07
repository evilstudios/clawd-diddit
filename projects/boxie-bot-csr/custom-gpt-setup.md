# Custom GPT Setup Guide

This guide walks you through setting up the CSR Copilot Custom GPT in ChatGPT.

## Prerequisites

1. ChatGPT Plus or Enterprise account
2. Access to Custom GPT creation
3. Deployed MCP Gateway server (with public URL)
4. Zoho Desk credentials configured

## Step-by-Step Setup

### Step 1: Create a New Custom GPT

1. Go to [ChatGPT](https://chat.openai.com)
2. Click on your profile → "My GPTs"
3. Click "Create a GPT"
4. Choose "Configure" tab

### Step 2: Configure Basic Information

**Name:**
```
CSR Copilot - WineShipping Support Assistant
```

**Description:**
```
AI-powered assistant for customer service representatives. Helps with ticket management, response generation, and customer support for WineShipping.
```

**Profile Picture:**
- Upload a relevant icon or logo (optional)

### Step 3: Add Instructions

Copy the entire content from `custom-gpt/instructions.md` into the "Instructions" field.

Key points from instructions:
- The GPT acts as a CSR assistant
- It has access to 6 main tools
- It follows specific workflows and policies
- It maintains professional tone
- It references SOPs and policies

### Step 4: Add Knowledge Files

Upload the following documents as knowledge files:

1. `docs/sop.md` - Standard Operating Procedures
2. `docs/policies.md` - Customer Service Policies

These files will be used by the GPT to provide policy-compliant responses.

### Step 5: Configure Actions

1. Click "Create new action"
2. Choose "Import from URL" or paste the OpenAPI specification
3. Paste the content from `custom-gpt/openapi-spec.yaml`
4. Update the server URL to your deployed MCP Gateway endpoint

Example server URL:
```
https://your-mcp-gateway.example.com
```

### Step 6: Configure Authentication (Optional)

If your MCP Gateway requires authentication:

1. Choose authentication type (API Key, OAuth, etc.)
2. Configure the authentication settings
3. Test the connection

For API Key authentication:
- Auth Type: "API Key"
- API Key: Your gateway API key
- Auth Header: "Authorization"

### Step 7: Configure Capabilities

Enable/disable the following:

- ✅ **Web Browsing**: Disabled (not needed)
- ✅ **DALL·E Image Generation**: Disabled (not needed)
- ✅ **Code Interpreter**: Disabled (not needed)

### Step 8: Test the Custom GPT

Before publishing, test each tool:

#### Test 1: Search Tickets
```
Search for open tickets with high priority
```

Expected: List of tickets matching criteria

#### Test 2: Get Ticket Details
```
Show me details for ticket ID 123456
```

Expected: Complete ticket information

#### Test 3: Get Ticket Thread
```
Get the conversation history for ticket 123456
```

Expected: All messages in the thread

#### Test 4: Find Similar Tickets
```
Find similar resolved tickets about shipping delays
```

Expected: List of resolved tickets with similar issues

#### Test 5: Generate Response
```
Generate a response draft for ticket 123456
```

Expected: Professional, contextual response draft

#### Test 6: Summarize Ticket
```
Summarize ticket 123456 and tell me the next steps
```

Expected: Summary with recommended actions

### Step 9: Publish or Share

Once testing is complete:

**For Personal Use:**
- Click "Only me" to keep it private

**For Team Use:**
- Click "Share" → "Anyone with the link"
- Copy the link and share with your CSR team

**For Organization:**
- If you have ChatGPT Enterprise, you can publish to your organization

### Step 10: Train Your Team

Provide training to CSRs on:
1. How to access the Custom GPT
2. What questions to ask
3. How to interpret responses
4. When to use which tools
5. Policy and SOP awareness

## Example Conversation Flows

### Scenario 1: Handling a New Ticket

**CSR:** "I have ticket #12345 about a shipping delay. Can you help me?"

**GPT:** (Calls getTicketDetails and getTicketThread) "Here's what I found..."
- Ticket details summary
- Recent messages
- Similar resolved cases
- Suggested response

### Scenario 2: Finding Solutions

**CSR:** "Customer asking about returns. Find similar cases."

**GPT:** (Calls getSimilarResolvedTickets) "I found 5 similar resolved tickets..."
- List of similar tickets
- Common resolution patterns
- Policy references

### Scenario 3: Draft Response

**CSR:** "Draft a response for ticket #12345"

**GPT:** (Calls generateResponseDraft) "Here's a suggested response..."
- Context-aware draft
- Policy-compliant language
- Professional tone

## Troubleshooting

### Actions Not Working

1. Verify server URL is correct and accessible
2. Check authentication configuration
3. Ensure MCP Gateway is running
4. Test API endpoints directly
5. Check logs for errors

### GPT Not Following Instructions

1. Review and clarify instructions
2. Provide more specific examples
3. Update knowledge files
4. Test with different phrasings

### Knowledge Files Not Referenced

1. Ensure files are properly uploaded
2. Reference specific sections in instructions
3. Ask GPT to cite policies explicitly

### Rate Limiting Issues

1. Implement rate limiting on MCP Gateway
2. Add retry logic with exponential backoff
3. Consider caching frequently accessed data

## Best Practices

1. **Keep Instructions Updated**: Regularly review and update instructions based on usage
2. **Update Knowledge Files**: Keep SOPs and policies current
3. **Monitor Usage**: Track which tools are used most frequently
4. **Gather Feedback**: Collect CSR feedback for improvements
5. **Security**: Regularly review access permissions
6. **Testing**: Test after any configuration changes
7. **Documentation**: Keep this guide updated

## Advanced Configuration

### Adding Custom Tools

To add new tools to your Custom GPT:

1. Implement the tool in MCP server (`src/index.ts`)
2. Add to OpenAPI specification
3. Update Custom GPT instructions to reference new tool
4. Test thoroughly before rolling out

### Integrating Additional Systems

Beyond Zoho Desk, you can integrate:
- CRM systems (Salesforce, HubSpot)
- Knowledge bases
- Analytics platforms
- Internal databases

Update the MCP Gateway to connect to these systems.

### Customizing Response Generation

Modify the `generateAIResponse` function in `src/index.ts` to:
- Use different AI models (OpenAI, Anthropic)
- Apply custom templates
- Include more context
- Fine-tune response style

## Maintenance

### Regular Tasks

**Weekly:**
- Review GPT usage logs
- Update knowledge files as policies change
- Check for API errors

**Monthly:**
- Review CSR feedback
- Update instructions based on learnings
- Test all Actions
- Update documentation

**Quarterly:**
- Major review of instructions
- Evaluate new features
- Training refreshers
- Security audit

## Support and Resources

- [OpenAI Custom GPT Documentation](https://platform.openai.com/docs/guides/gpt)
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk)
- [Zoho Desk API Docs](https://desk.zoho.com/support/APIDocument.do)

---

**Questions?** Contact the development team or refer to the main README.md
