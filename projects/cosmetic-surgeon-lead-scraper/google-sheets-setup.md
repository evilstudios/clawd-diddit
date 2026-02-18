# Google Sheets Setup Guide
## Cosmetic Surgeon Lead Generation System

## Step 1: Create New Google Sheet

**Sheet Name:** "Cosmetic Surgery Lead Pipeline"

---

## Sheet Structure

### Tab 1: "🔥 Hot Leads" (Score 8-10)
Immediate outreach priority

| Lead ID | Name | Score | Location | Procedure | Phone | Email | Instagram | Source | Last Activity | Notes | Status |
|---------|------|-------|----------|-----------|-------|-------|-----------|--------|---------------|-------|--------|

**Conditional Formatting:**
- Rows: Light red background (#fff0f0)
- Score column: Red text, bold
- Status dropdown: "New" (yellow), "Contacted" (blue), "Consultation Booked" (green), "Not Interested" (gray)

---

### Tab 2: "🟡 Warm Leads" (Score 5-7)
Nurture sequence

| Lead ID | Name | Score | Location | Procedure | Phone | Email | Instagram | Source | Last Activity | Notes | Status |

**Conditional Formatting:**
- Rows: Light yellow background (#fffef0)
- Score column: Orange text, bold

---

### Tab 3: "📊 All Leads" (Master List)
Complete database with all leads

| Lead ID | Name | Score | Location | Procedure | Phone | Email | Instagram | Source | Last Activity | Notes | Status | Date Added |

**Features:**
- Filter views enabled
- Sort by score (default)
- Search functionality
- Export button (File → Download → CSV)

---

### Tab 4: "📈 Dashboard"
Visual performance tracking

```
┌─────────────────────────────────────────────────┐
│  LEAD GENERATION DASHBOARD                      │
│  Last Updated: [Auto-timestamp]                 │
├─────────────────────────────────────────────────┤
│                                                  │
│  Total Leads This Month: [COUNT]                │
│  🔴 Hot Leads (8-10):     [COUNT]               │
│  🟡 Warm Leads (5-7):     [COUNT]               │
│  🟢 Cold Leads (1-4):     [COUNT]               │
│                                                  │
│  ──────────────────────────────────────────────  │
│                                                  │
│  Conversion Funnel:                             │
│  └─ New Leads:              [COUNT]             │
│  └─ Contacted:              [COUNT]             │
│  └─ Consultations Booked:   [COUNT]             │
│  └─ Closed (Procedure):     [COUNT]             │
│                                                  │
│  Conversion Rate: [%]                           │
│  Cost Per Lead: $[CALC]                         │
│  Revenue Generated: $[CALC]                     │
│  ROI: [CALC]x                                   │
│                                                  │
│  ──────────────────────────────────────────────  │
│                                                  │
│  Top Procedures:                                │
│  [Chart: Procedure breakdown]                   │
│                                                  │
│  Lead Sources:                                  │
│  [Chart: Source breakdown]                      │
│                                                  │
│  Geographic Heatmap:                            │
│  [Chart: City breakdown]                        │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Formulas:**
```
Total Leads: =COUNTA('All Leads'!A:A)-1
Hot Leads: =COUNTIF('All Leads'!C:C,">=8")
Warm Leads: =COUNTIFS('All Leads'!C:C,">=5",'All Leads'!C:C,"<8")
Conversion Rate: =(Consultations Booked / Total Leads)*100
```

---

### Tab 5: "⚙️ Settings" (Hidden from client)

**Configuration:**
```
Practice Name: [Beverly Hills Aesthetic Center]
Location: [Beverly Hills, CA]
Target Radius: [50 miles]
Specialties: [Breast Aug, Rhinoplasty, Facelift, Botox]
Scraping Schedule: [Daily / Weekly / Monthly]
```

**API Keys** (protected):
```
Apollo.io: [HIDDEN]
Hunter.io: [HIDDEN]
Instagram: [HIDDEN]
```

**Lead Cost Tracking:**
```
Monthly Subscription: $1,299
Leads Delivered: [AUTO-COUNT]
Cost Per Lead: [AUTO-CALC]
```

---

## Automation Features (Google Apps Script)

### Script 1: Auto-Import New Leads
```javascript
function importNewLeads() {
  // Fetch from scraper API endpoint
  // Parse JSON
  // Append to "All Leads" sheet
  // Sort by score
  // Distribute to Hot/Warm tabs
  // Send notification email
}
```

### Script 2: Update Dashboard
```javascript
function updateDashboard() {
  // Count leads by category
  // Calculate conversion metrics
  // Update charts
  // Timestamp update
}
```

### Script 3: Weekly Summary Email
```javascript
function sendWeeklySummary() {
  // Count new leads this week
  // Highlight top 5 hot leads
  // Email to practice owner/admin
}
```

### Script 4: Status Tracking
```javascript
function onEdit(e) {
  // When status changes to "Consultation Booked"
  // Auto-calculate ROI
  // Update dashboard
  // Log to "Conversions" tracking sheet
}
```

---

## Custom Menu Bar

**Menu: "Lead Gen Tools"**
- Refresh Leads (manual trigger)
- Export to CSV
- Send to CRM
- View Dashboard
- Settings

---

## Data Validation Rules

**Status Column:**
- Dropdown: "New", "Contacted", "Consultation Booked", "Procedure Scheduled", "Completed", "Not Interested", "Invalid Contact"

**Score Column:**
- Number validation: 1-10 only

**Email Column:**
- Email format validation

**Phone Column:**
- Phone format validation: (XXX) XXX-XXXX

---

## Sharing & Permissions

**Practice Owner/Admin:**
- Editor access to Hot Leads, Warm Leads, All Leads, Dashboard
- Viewer access to Settings (can't edit API keys)

**Sales Team:**
- Editor access to Hot Leads, Warm Leads (can update status)
- Viewer access to All Leads, Dashboard

**Scraper System:**
- Service account with API access
- Can append to All Leads sheet only

---

## Mobile-Friendly View

**Google Sheets Mobile App Features:**
- Filter by "New" status for quick outreach
- One-tap to call/email from lead row
- Update status on-the-go
- View dashboard metrics

---

## Sample Data Import

Import the generated `cosmetic_surgery_leads.csv`:

1. Open Google Sheets
2. File → Import → Upload
3. Select `cosmetic_surgery_leads.csv`
4. Import location: "Insert new sheet"
5. Rename to "All Leads"
6. Apply formatting from template

---

## Demo Presentation Script

**For Sales Calls:**

> "Let me show you how this works. Every day, our system scrapes Instagram, RealSelf, and review sites for people showing interest in cosmetic procedures in your area.
> 
> [Open Google Sheet]
> 
> See the 'Hot Leads' tab? These are people who asked about pricing, commented on procedure posts, or actively researched on RealSelf in the last 30 days. Each lead is scored 1-10 based on intent signals.
> 
> [Click on a hot lead]
> 
> Here's Sarah from Beverly Hills. Score of 9. She commented 'love the results!' on a breast augmentation post, follows 4 local med spas, and we found her email and phone. She's ready for outreach RIGHT NOW.
> 
> [Switch to Dashboard tab]
> 
> This dashboard shows your pipeline at a glance. You can track how many leads convert to consultations, calculate your ROI, and see which procedures are most popular.
> 
> [Switch to Settings]
> 
> It's fully customizable to your practice—target radius, specialties, even which procedures to prioritize.
> 
> And the best part? This all updates automatically. Every morning you wake up to fresh, qualified leads in your inbox. No cold calling, no expensive ads. Just high-intent prospects who are already thinking about cosmetic procedures."

---

## Next Steps for Live Implementation

1. **Create template Google Sheet** with all tabs/formatting
2. **Build Apps Script automation** for auto-import
3. **Connect scraper backend** (Python script → Google Sheets API)
4. **Test with pilot client** (1-2 practices)
5. **Refine based on feedback**
6. **Scale to 10+ practices**

---

**Files in this directory:**
- `README.md` - System overview
- `scraper-prototype.py` - Demo lead generator
- `cosmetic_surgery_leads.csv` - Sample data export
- `google-sheets-setup.md` - This file
