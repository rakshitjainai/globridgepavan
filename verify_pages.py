"""
Comprehensive verification test suite for Globridge Capital IFSC replica
"""
import re
import os

with open('client/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f'client/index.html size: {len(html)} bytes')

# 1. Verify 13 pages
expected_pages = [
    'home', 'about', 'team', 'approach', 'fund', 'insights',
    'investors', 'contact', 'disclosures', 'article', 'doc',
    'terms', 'privacy'
]
for p in expected_pages:
    assert f'id="page-{p}"' in html, f"Missing page: {p}"
print(f"[PASS] All {len(expected_pages)} pages verified!")

# 2. Verify Team Photos height and individual crops
assert '.tm .ph{height:300px;' in html, "Container height is not 300px"

team_members = [
    ('tm-kv', 'Krishnamurthy.jpeg', 'center 10%'),
    ('tm-ps', 'Pavan.jpeg', 'center 5%'),
    ('tm-bb', 'Basanagouda.jpeg', 'center 15%'),
    ('tm-an', 'adesh-nayak.jpg', 'center 10%'),
    ('tm-sb', 'Sahil.jpeg', 'center 8%'),
    ('tm-as', 'Aditya-Sarawad.jpeg', 'center 12%'),
    ('tm-sj', 'Shilpa.jpeg', 'center 10%')
]

for tm_id, img, pos in team_members:
    card_match = re.search(r'id="' + tm_id + r'"[\s\S]*?</article>', html)
    assert card_match, f"Card {tm_id} not found"
    card_html = card_match.group(0)
    assert img in card_html, f"Image {img} not in {tm_id}"
    assert f'object-position:{pos}' in card_html, f"Position {pos} not in {tm_id}"
    assert "Photo to be provided" not in card_html, f"Found placeholder in {tm_id}"
print("[PASS] Team photo container height (300px) and individual crops verified!")

# 3. Verify No "Coming soon" in Insights or Home
assert "Coming soon" not in html, "Found 'Coming soon' remaining in the HTML!"
print("[PASS] All 'Coming soon' placeholders successfully removed!")

# 4. Verify 4 Insights Articles (No PDF viewer, full web articles)
insights_info = [
    ('art-insight-1', 'Outbound angel investing through GIFT IFSC', 'Why the question is being asked'),
    ('art-insight-2', 'University spin-outs as an asset class', 'A different starting point'),
    ('art-insight-3', 'Inside the LEADER themes', 'Why a thematic focus'),
    ('art-insight-4', 'How a Category I Angel Fund in IFSC works', 'Starting with the vocabulary')
]

for art_id, title, snippet in insights_info:
    assert f'id="{art_id}"' in html, f"Missing {art_id}"
    assert title in html, f"Missing title {title}"
    assert snippet in html, f"Missing snippet {snippet}"
print("[PASS] All 4 Insights articles verified as native web article pages!")

# 5. Verify 2 Policy Documents (No PDF viewer, full web articles)
policies_info = [
    ('doc-pane-grievance', 'Complaint Handling and Grievance Redressal Policy', '10. Escalation Matrix'),
    ('doc-pane-esg', 'ESG and Responsible Investment Policy', '5. Negative / Exclusion List')
]

for doc_id, title, snippet in policies_info:
    assert f'id="{doc_id}"' in html, f"Missing {doc_id}"
    assert title in html, f"Missing title {title}"
    assert snippet in html, f"Missing snippet {snippet}"
print("[PASS] Both Policy documents verified as native web article pages!")

# 6. Verify Quarterly status table in Complaint Handling Policy
doc_grievance_match = re.search(r'id="doc-pane-grievance"[\s\S]*?(?=<div id="doc-pane-esg"|\Z)', html)
assert doc_grievance_match, "doc-pane-grievance not found"
doc_g_html = doc_grievance_match.group(0)

assert "Quarterly status of investor complaints" in doc_g_html
table_headers = [
    "Quarter", "Pending at start", "Received", "Resolved",
    "Rejected", "Pending at end", "Average days to dispose"
]
for th in table_headers:
    assert f">{th}</th>" in doc_g_html, f"Missing header: {th}"

assert "Quarter ended 30 September 2026" in doc_g_html
assert "Quarter ended 31 December 2026" in doc_g_html
assert ">Nil</td>" in doc_g_html
print("[PASS] Quarterly status of investor complaints table verified in Complaint Handling Policy!")

# 7. Verify Review Notes and Top Draftbar are removed
body_idx = html.find('<body')
body_html = html[body_idx:]
assert '<div class="draftbar">' not in body_html, "Found draftbar in body"
assert '<span class="rv"' not in body_html, "Found rv note in body"
assert 'id="toggleNotes"' not in body_html, "Found toggleNotes button in body"
print("[PASS] All review notes and top draftbar verified removed from site!")

# 8. Verify Router Script
assert "'insight-1':'Outbound angel investing through GIFT IFSC'" in html
assert "'doc-grievance-policy':'doc-pane-grievance'" in html
assert "'doc-esg-policy':'doc-pane-esg'" in html
print("[PASS] Router script verified for dynamic pane switching and title updates!")

# 9. Verify LEADER Theme: Advanced Biotech (Task 1)
assert "Applied AI" not in html, "Found 'Applied AI' remaining in index.html!"
assert "Applied AI &amp; Data" not in html, "Found 'Applied AI &amp; Data' remaining in index.html!"
assert "<h3>Advanced Biotech</h3>" in html, "Missing '<h3>Advanced Biotech</h3>'!"
assert "Life-science platforms emerging from university labs." in html, "Missing Advanced Biotech description!"
leader_art3 = re.search(r'id="art-insight-3"[\s\S]*?(?=<div id="art-insight-4"|\Z)', html)
assert leader_art3, "art-insight-3 not found"
art3_html = leader_art3.group(0)
assert "Advanced Biotech" in art3_html, "Advanced Biotech not in art-insight-3!"
assert "Life-science platforms emerging from university labs." in art3_html, "Description not in art-insight-3 card!"
print("[PASS] LEADER theme 'Advanced Biotech' verified across cards and articles!")

# 10. Verify Terms of Use and Privacy Policy (Task 2)
terms_match = re.search(r'<section id="page-terms"[\s\S]*?</section>', html)
assert terms_match, "page-terms not found"
terms_html = terms_match.group(0)
for sec_num in range(1, 14):
    assert f">{sec_num}. " in terms_html, f"Missing section {sec_num} in Terms of Use"
assert re.findall(r'\[.*?\]', terms_html) == [], "Found bracketed placeholder in Terms of Use!"
assert '<span class="blank' not in terms_html, "Found blank placeholder in Terms of Use!"

privacy_match = re.search(r'<section id="page-privacy"[\s\S]*?</section>', html)
assert privacy_match, "page-privacy not found"
privacy_html = privacy_match.group(0)
for sec_num in range(1, 12):
    assert f">{sec_num}. " in privacy_html, f"Missing section {sec_num} in Privacy Policy"
assert re.findall(r'\[.*?\]', privacy_html) == [], "Found bracketed placeholder in Privacy Policy!"
assert '<span class="blank' not in privacy_html, "Found blank placeholder in Privacy Policy!"
print("[PASS] Complete Terms of Use (13 sections) and Privacy Policy (11 sections) verified without placeholders!")

# 11. Verify SEO Metadata and Robots Tag (Task 3)
assert '<meta name="robots" content="index, follow">' in html, "Missing or incorrect meta robots tag!"
assert '<meta name="google-site-verification" content="BH4OfpaIxzI56UK95HzHbWSpuBJ1oTx-FlmOw8x4BR4" />' in html, "Missing Google Search Console verification meta tag!"
assert 'noindex' not in html, "Found 'noindex' directive in HTML!"
assert 'nofollow' not in html, "Found 'nofollow' directive in HTML!"
assert 'noarchive' not in html, "Found 'noarchive' directive in HTML!"
assert '<link rel="canonical" href="https://www.globridgecapital.com/">' in html, "Missing canonical URL!"
assert '<meta property="og:title"' in html, "Missing Open Graph title!"
assert '<meta property="og:description"' in html, "Missing Open Graph description!"
assert '<meta property="og:url"' in html, "Missing Open Graph URL!"
print("[PASS] SEO metadata, canonical link, and public indexing directives verified!")

# 12. Verify robots.txt and sitemap.xml files (Task 3)
import xml.etree.ElementTree as ET

for robots_path in ['client/robots.txt', 'public/robots.txt']:
    assert os.path.exists(robots_path), f"Missing {robots_path}!"
    with open(robots_path, 'r', encoding='utf-8') as rf:
        rtxt = rf.read()
    assert "User-agent: *" in rtxt, f"Missing User-agent in {robots_path}"
    assert "Allow: /" in rtxt, f"Missing Allow in {robots_path}"
    assert "Sitemap: https://www.globridgecapital.com/sitemap.xml" in rtxt, f"Missing Sitemap in {robots_path}"

for sitemap_path in ['client/sitemap.xml', 'public/sitemap.xml']:
    assert os.path.exists(sitemap_path), f"Missing {sitemap_path}!"
    with open(sitemap_path, 'r', encoding='utf-8') as sf:
        tree = ET.parse(sf)
        root = tree.getroot()
        assert len(root) >= 10, f"Too few URLs in {sitemap_path}"
print("[PASS] robots.txt and sitemap.xml verified in both client/ and public/!")

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
