# Globridge Capital IFSC — Replica

An end-to-end replica of **Globridge Capital IFSC** ([https://csatwork.in/globridge-preview/](https://csatwork.in/globridge-preview/)), an Authorised Fund Management Entity (FME) registered with the International Financial Services Centres Authority (IFSCA Reg. No. `FDM2026FUM1106`) at GIFT City, Gandhinagar, managing the **Leader Angel IFSC Fund** (Category I Angel Fund).

---

## 📁 Repository Structure

```
.
├── client/
│   ├── assets/
│   │   ├── hero-bg.jpg                          # Hero background
│   │   ├── gift-city-bg.jpg                     # GIFT City skyline feature
│   │   ├── globridge-logo.png                   # Header logo
│   │   ├── city-skyline-dusk.jpg                # Fund card skyline
│   │   ├── insight-1-outbound-angel.jpg         # Article 1 thumbnail
│   │   ├── insight-2-university-spinouts.jpg    # Article 2 thumbnail
│   │   ├── insight-3-leader-themes.jpg          # Article 3 thumbnail
│   │   ├── insight-4-category-1-angel-fund.jpg  # Article 4 thumbnail
│   │   ├── globridge-logo-footer.png            # Footer logo
│   │   ├── insights/                            # Source Insights PDFs
│   │   │   ├── 01_Outbound_Angel_Investing_through_GIFT_IFSC.pdf
│   │   │   ├── 02_University_Spin-outs_as_an_Asset_Class.pdf
│   │   │   ├── 03_Inside_the_LEADER_Themes.pdf
│   │   │   └── 04_How_a_Category_I_Angel_Fund_in_IFSC_Works.pdf
│   │   ├── policy/                              # Source Policy PDFs
│   │   │   ├── Complaint-Handling-and-Grievance-Redressal-Policy.pdf
│   │   │   └── ESG-and-Responsible-Investment-Policy.pdf
│   │   └── team/                                # High-resolution executive headshots
│   │       ├── Aditya-Sarawad.jpeg
│   │       ├── Basanagouda.jpeg
│   │       ├── Krishnamurthy.jpeg
│   │       ├── Pavan.jpeg
│   │       ├── Sahil.jpeg
│   │       └── Shilpa.jpeg
│   ├── index.html                               # Core SPA application (13 pages + router)
│   └── package.json                             # Client scripts
├── server/                                      # Empty folder (reference does not require backend logic)
├── package.json                                 # Root npm configuration & dev scripts
├── serve.js                                     # Zero-dependency local preview dev server
├── verify_pages.py                              # Automated regression & verification test suite
└── README.md
```

---

## 🚀 Getting Started

### Quick Start
To start the local development server:

```bash
npm run dev
# or
node serve.js
```
Then visit `http://localhost:3000` in your browser.

Alternatively, you can open `client/index.html` directly in any web browser without a server.

### Running Automated Tests
```bash
npm test
# or
python verify_pages.py
```

### Production Deployment (Vercel)
The repository includes a production-ready `vercel.json` configured for static edge delivery:
- **Framework Preset**: `Other`
- **Root Directory**: `./`
- **Output Directory**: `client`
- **Build Command**: `npm run build` (or None)
- **Install Command**: None

---

## 🌟 Key Features & Updates

### 1. Clean Presentation (Review Notes & Draft Bar Removed)
- Completely removed the top draft review bar (`.draftbar` banner and `#toggleNotes` toggle button).
- Completely removed all 13 yellow review note boxes (`.rv`) and their container margins/paddings across all pages for a clean, live-ready presentation.

### 2. Team Photos & Framing
- Height set to **`300px`** with tailored `object-position` for each executive, ensuring complete face visibility and balanced framing.

### 3. Native Policy & Insights Articles
- Policy documents and Insights articles are presented as native web articles with clean typography, tables, and pull-quotes, with no embedded PDF toolbars or viewers.
- Removed all *"Coming Soon"* placeholders across the entire application.

### 4. Complaint Handling Policy Table
- Preserved exact 7-column quarterly complaints reporting table from the source PDF under Section 13 with `Nil` values and touch-friendly mobile horizontal scrolling.
