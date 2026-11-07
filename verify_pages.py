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

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
