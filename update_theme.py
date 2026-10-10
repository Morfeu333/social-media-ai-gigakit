import re

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update CSS variables to the exact palette extracted from the user's photo:
# Base background: #031432 / #020b1e
# Electric Blue glow: #0D62FE / #0070F3
# Hologram Cyan: #00F0FF / #38BDF8
# Instagram Magenta: #FF2D75 / #E1306C
# Deep Glass: rgba(3, 20, 50, 0.65) with 1px border rgba(0, 240, 255, 0.45)

new_root = """    :root {
      --bg-dark: #020B1E;
      --bg-deep: #031432;
      --bg-card: rgba(4, 25, 65, 0.72);
      --bg-card-hover: rgba(7, 38, 98, 0.85);
      --border-color: rgba(0, 240, 255, 0.18);
      --border-highlight: rgba(0, 240, 255, 0.6);
      --border-cyan: rgba(0, 240, 255, 0.5);
      --border-blue: rgba(13, 98, 254, 0.6);
      --electric-blue: #0D62FE;
      --electric-glow: rgba(13, 98, 254, 0.45);
      --cyan: #00F0FF;
      --cyan-glow: rgba(0, 240, 255, 0.35);
      --ig-magenta: #FF2D75;
      --ig-glow: rgba(255, 45, 117, 0.4);
      --emerald: #10B981;
      --emerald-glow: rgba(16, 185, 129, 0.3);
      --amber: #F59E0B;
      --text-main: #FFFFFF;
      --text-muted: #93C5FD;
      --text-dim: #60A5FA;
      --font-display: 'Syne', -apple-system, sans-serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }"""

html = re.sub(r':root\s*\{[^}]*\}', new_root, html, count=1)

# Update body background with deep oceanic cosmic blue gradients and floating neon orbits
new_body_bg = """      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(13, 98, 254, 0.35) 0%, transparent 60%),
        radial-gradient(circle at 80% 20%, rgba(0, 240, 255, 0.22) 0%, transparent 50%),
        radial-gradient(circle at 20% 40%, rgba(255, 45, 117, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 50% 70%, rgba(13, 98, 254, 0.25) 0%, transparent 60%),
        linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 100% 100%, 100% 100%, 48px 48px, 48px 48px;"""

html = re.sub(r'background-color:\s*var\(--bg-dark\);[\s\S]*?48px 48px;', new_body_bg, html, count=1)

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Theme updated successfully in index.html")
