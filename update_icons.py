with open("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace instagram-logo.jpg with the crisp SVG version
html = html.replace('src="/instagram-logo.jpg"', 'src="/icons/instagram.svg"')

# In the brand marquee, add TikTok and YouTube as well
old_marquee = """      <div class="brand-pill"><img src="/icons/assemblyai.svg" alt="AssemblyAI">AssemblyAI</div>
      <!-- Loop clones -->"""

new_marquee = """      <div class="brand-pill"><img src="/icons/assemblyai.svg" alt="AssemblyAI">AssemblyAI</div>
      <div class="brand-pill"><img src="/icons/tiktok.svg" alt="TikTok">TikTok Flow</div>
      <div class="brand-pill"><img src="/icons/youtube.svg" alt="YouTube">YouTube Shorts</div>
      <!-- Loop clones -->"""

html = html.replace(old_marquee, new_marquee)

old_loop = """      <div class="brand-pill"><img src="/icons/assemblyai.svg" alt="AssemblyAI">AssemblyAI</div>
    </div>"""

new_loop = """      <div class="brand-pill"><img src="/icons/assemblyai.svg" alt="AssemblyAI">AssemblyAI</div>
      <div class="brand-pill"><img src="/icons/tiktok.svg" alt="TikTok">TikTok Flow</div>
      <div class="brand-pill"><img src="/icons/youtube.svg" alt="YouTube">YouTube Shorts</div>
    </div>"""

html = html.replace(old_loop, new_loop)

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html", "r", encoding="utf-8") as f:
    en_html = f.read()

en_html = en_html.replace('src="/instagram-logo.jpg"', 'src="/icons/instagram.svg"')
en_html = en_html.replace(old_marquee, new_marquee)
en_html = en_html.replace(old_loop, new_loop)

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html", "w", encoding="utf-8") as f:
    f.write(en_html)

print("Icons and brand marquees updated")
