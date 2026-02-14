# LYLYS Design System
## "Digital Warmth" Brand Guidelines

### 🎨 Color Palette

#### Core Colors
| Role | Name | Hex | Purpose |
|------|------|-----|---------|
| **Primary** | Heartbeat Red | `#FF4B5C` | Brand identity, logos, "Love" elements |
| **Secondary** | Broadcast Amber | `#FFB347` | Highlights, badges, "Creator" spotlight |
| **Action** | Connection Teal | `#00CEC9` | CTAs, success states, high-conversion buttons |
| **Base** | Studio Slate | `#2D3436` | Text, navigation, footer backgrounds |
| **Soft** | Paper White | `#F9F9F9` | Main background, clean & airy UI |

#### CSS Variables
```css
:root {
  /* Brand Colors */
  --primary: #FF4B5C;        /* Heartbeat Red */
  --secondary: #FFB347;      /* Broadcast Amber */
  --accent: #00CEC9;         /* Connection Teal */
  --neutral: #2D3436;        /* Studio Slate */
  --bg-light: #F9F9F9;       /* Paper White */
  
  /* Semantic Colors */
  --color-love: var(--primary);
  --color-creator: var(--secondary);
  --color-action: var(--accent);
  --color-text: var(--neutral);
  --color-bg: var(--bg-light);
  
  /* Spacing Scale */
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */
  
  /* Typography */
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-display: 'Inter', var(--font-sans);
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(45, 52, 54, 0.05);
  --shadow-md: 0 4px 6px rgba(45, 52, 54, 0.1);
  --shadow-lg: 0 10px 15px rgba(45, 52, 54, 0.1);
  --shadow-glow: 0 0 20px rgba(255, 179, 71, 0.3);
}
```

---

## 🎯 Visual Implementation Guide

### 1. The "Glow" Effect
**Use Case**: Creator avatars, spotlight elements  
**Implementation**:
```css
.creator-spotlight {
  box-shadow: 0 0 20px rgba(255, 179, 71, 0.3); /* Broadcast Amber glow */
  border: 2px solid var(--secondary);
}
```

### 2. Call-to-Action Buttons
**Primary CTA**: "Start Free Trial", "Get Fan Audit"
```css
.btn-primary {
  background: var(--accent);        /* Connection Teal */
  color: white;
  box-shadow: var(--shadow-md);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: #00B8B3;              /* Darker teal */
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}
```

### 3. Data Visualization
**Fan Audit Charts**:
- **High-Value Superfans**: Heartbeat Red (`#FF4B5C`)
- **Rising Supporters**: Broadcast Amber (`#FFB347`)
- **General Audience**: Studio Slate (`#2D3436`)

```javascript
const chartColors = {
  superfans: '#FF4B5C',
  rising: '#FFB347',
  general: '#2D3436'
};
```

### 4. Physical Branding (Printful Boxes)
**Box Design**:
- Base: Natural Kraft (Cardboard) or White
- Tape/Logo: Heartbeat Red (`#FF4B5C`)
- Typography: Studio Slate (`#2D3436`)

**Premium Look**: Similar to Glossier, Target, Warby Parker

---

## 🧩 Component Patterns

### Hero Section
```jsx
<section className="hero bg-gradient-to-br from-[#F9F9F9] to-white">
  <h1 className="text-[#2D3436] font-bold">
    Your <span className="text-[#FF4B5C]">Superfans</span> Are Leaving
  </h1>
  <p className="text-[#2D3436]/80">
    Automate gratitude. Build loyalty. Grow revenue.
  </p>
  <button className="bg-[#00CEC9] text-white hover:shadow-lg">
    Get Your Free Fan Audit →
  </button>
</section>
```

### Creator Card
```jsx
<div className="card bg-white border-2 border-[#FFB347]/20 rounded-xl shadow-[0_0_20px_rgba(255,179,71,0.3)]">
  <div className="avatar">
    <img src={creator.avatar} alt={creator.name} />
    <span className="badge bg-[#FFB347]">Creator</span>
  </div>
  <h3 className="text-[#2D3436]">{creator.name}</h3>
  <p className="text-[#2D3436]/70">{creator.followers} followers</p>
</div>
```

### Fan Audit Results
```jsx
<div className="audit-chart">
  <div className="stat superfans">
    <div className="bar bg-[#FF4B5C]" style={{width: '80%'}}></div>
    <span>12 Superfans</span>
  </div>
  <div className="stat rising">
    <div className="bar bg-[#FFB347]" style={{width: '60%'}}></div>
    <span>34 Rising Supporters</span>
  </div>
  <div className="stat general">
    <div className="bar bg-[#2D3436]/30" style={{width: '40%'}}></div>
    <span>1.2K General Audience</span>
  </div>
</div>
```

---

## 📐 Layout Guidelines

### Spacing Scale
- **xs** (4px): Icon gaps, tight spacing
- **sm** (8px): Between related elements
- **md** (16px): Standard component spacing
- **lg** (24px): Between sections
- **xl** (32px): Major section padding
- **2xl** (48px): Hero section spacing
- **3xl** (64px): Page section dividers

### Typography Scale
```css
/* Headings */
.h1 { font-size: 3.5rem; font-weight: 700; color: var(--neutral); }
.h2 { font-size: 2.5rem; font-weight: 700; color: var(--neutral); }
.h3 { font-size: 1.875rem; font-weight: 600; color: var(--neutral); }
.h4 { font-size: 1.5rem; font-weight: 600; color: var(--neutral); }

/* Body */
.body-lg { font-size: 1.25rem; line-height: 1.6; }
.body { font-size: 1rem; line-height: 1.6; }
.body-sm { font-size: 0.875rem; line-height: 1.5; }

/* Special */
.label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; }
```

---

## 🎭 Brand Voice & Tone

### Core Messaging
**Headline**: "Your Superfans Are Leaving. We'll Bring Them Back."  
**Subhead**: "Automate gratitude. Build loyalty. Grow revenue."  
**CTA**: "Get Your Free Fan Audit →"

### Tone Guidelines
- **Warm but Professional**: Not corporate, not overly casual
- **Fan-First Language**: "Your fans deserve recognition"
- **Action-Oriented**: "Start rewarding", "Build loyalty"
- **Data-Informed**: "12 fans need recognition" (specific numbers)

### Copy Examples

**Hero**:
> Stop Losing Your Superfans  
> Mid-tier creators have 10-100K subscribers but lose touch with their most loyal fans.  
> LYLYS tracks engagement and rewards your top 1% automatically.

**Features**:
> 🔍 **Scout** — Find your superfans automatically  
> 💌 **Concierge** — Track milestones & anniversaries  
> 🎁 **Fulfillment** — Ship rewards without lifting a finger

**Social Proof**:
> "I had no idea I had 23 fans who watched every video. LYLYS found them and sent thank-you gifts automatically." — *Sarah M., Podcast Creator*

---

## 🖼️ Visual Assets Needed

### Immediate
- [ ] LYLYS logo (Heartbeat Red + Studio Slate)
- [ ] Favicon
- [ ] OG image (social sharing)

### Phase 2
- [ ] Creator avatars (placeholder illustrations)
- [ ] Fan reward mockups (stickers, hats)
- [ ] Dashboard screenshots
- [ ] Chart/graph illustrations

---

## 📱 Responsive Breakpoints

```css
/* Mobile First */
@media (min-width: 640px)  { /* sm */ }
@media (min-width: 768px)  { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

---

## ✅ Design System Checklist

- [x] Color palette defined
- [x] CSS variables created
- [x] Component patterns documented
- [x] Typography scale established
- [x] Spacing system defined
- [x] Brand voice guidelines written
- [ ] Logo created
- [ ] Favicon generated
- [ ] Component library built (Next.js)

---

**Status**: Design system ready for implementation  
**Next**: Build Next.js components with Tailwind CSS  
**Location**: `projects/lylys/`
