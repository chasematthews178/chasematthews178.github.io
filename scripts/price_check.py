import requests, sys, os
from datetime import datetime

KNOWN_PRICES = {
    "Jasper AI":         {"price_str":"39",  "check_url":"https://www.jasper.ai/pricing"},
    "Notion AI":         {"price_str":"10",  "check_url":"https://www.notion.so/pricing"},
    "Canva Magic":       {"price_str":"15",  "check_url":"https://www.canva.com/pricing/"},
    "Semrush":           {"price_str":"139", "check_url":"https://www.semrush.com/prices/"},
    "Tidio":             {"price_str":"29",  "check_url":"https://www.tidio.com/pricing/"},
    "Zapier":            {"price_str":"20",  "check_url":"https://zapier.com/pricing"},
    "Kit (ConvertKit)":  {"price_str":"25",  "check_url":"https://kit.com/pricing"},
}
HEADERS = {"User-Agent":"Mozilla/5.0 (compatible; PriceBot/1.0)"}

def check_tool(name, info):
    try:
        resp = requests.get(info["check_url"], headers=HEADERS, timeout=15, allow_redirects=True)
        page = resp.text.lower()
        known = info["price_str"]
        if f"${known}" in page or f"${known}/" in page:
            return True, f"✓ {name}: ${known} confirmed"
        return False, f"⚠️  {name}: ${known}/mo NOT found — manual check needed\n   {info['check_url']}"
    except Exception as e:
        return None, f"⚡ {name}: Could not reach pricing page ({e})"

def main():
    results, has_alert = [], False
    for name, info in KNOWN_PRICES.items():
        ok, msg = check_tool(name, info)
        print(msg); results.append(msg)
        if ok is False: has_alert = True
    with open("price-report.txt","w") as f:
        f.write(f"# Price Report — {datetime.utcnow().strftime('%Y-%m-%d')}\n\n" + "\n".join(results))
    sys.exit(1 if has_alert else 0)

if __name__ == "__main__":
    main()
