import json
import urllib.request
import urllib.error

SESSION_FILE = "/home/automatrix/.config/ghl/session.json"

with open(SESSION_FILE, "r") as f:
    session = json.load(f)

loc = session.get("location_id")
token = session.get("auth_token")

print("Location:", loc)

# Data to set in Client Portal
portal_payload = {
    "name": "Social Media AI GigaKit",
    "description": "Comunidade oficial e hub de automação, repositórios, skills de NLE e aceleração multicanal com inteligência artificial.",
    "brandColor1": "#0D62FE",
    "brandColor2": "#00F0FF",
    "supportEmail": "lucas@automatrix-ia.com",
    "copyrightText": "© 2026 Automatrix IA. Todos os direitos reservados."
}

# Test backend client portal endpoints
test_endpoints = [
    f"https://backend.leadconnectorhq.com/memberships/client-portal/branding/{loc}",
    f"https://backend.leadconnectorhq.com/memberships/client-portal/{loc}",
    f"https://services.leadconnectorhq.com/memberships/client-portal/{loc}"
]

for url in test_endpoints:
    print(f"\nTesting GET {url}...")
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "channel": "app",
        "source": "web",
        "version": "2021-07-28",
        "Accept": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            print("Status:", r.status)
            print("Body:", r.read().decode()[:300])
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code, e.read().decode()[:200])
    except Exception as e:
        print("Error:", e)
