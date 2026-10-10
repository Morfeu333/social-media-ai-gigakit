with open("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the hero image with the newly uploaded image ad-creator-floating-blue.jpg
html = html.replace('src="/hero-ads/ad-floating-elements.jpg"', 'src="/hero-ads/ad-creator-floating-blue.jpg"')

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html", "r", encoding="utf-8") as f:
    en_html = f.read()

en_html = en_html.replace('src="/hero-ads/ad-floating-elements.jpg"', 'src="/hero-ads/ad-creator-floating-blue.jpg"')

with open("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html", "w", encoding="utf-8") as f:
    f.write(en_html)

print("Hero showcase image replaced in both files")
