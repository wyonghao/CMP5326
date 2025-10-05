
Regex vs GPT Log Analysis Lab Dataset
=====================================

Files:
- logs/web.log    : Apache-like access log with embedded events (URLs, IPs, emails, credit cards incl. near-miss numbers)
- logs/auth.log   : SSH auth events (Accepted/Failed), IPs
- logs/app.log    : App/system events incl. emails, phone numbers, USB insert messages

Ground truth:
- ground_truth.csv: All target entities with file and line numbers (types: ip, url, email, credit_card, phone, login_success, login_fail, usb_insert)
