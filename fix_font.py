for path in ["/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", "/home/automatrix/Projects/social-media-ai-gigakit/public/en.html"]:
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace("--font-display: 'Syne', -apple-system, sans-serif;", "--font-display: 'Plus Jakarta Sans', -apple-system, sans-serif;")
    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
print("Font replaced with Plus Jakarta Sans")
