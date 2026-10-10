import os

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # When opening via file://, root-relative paths like /icons/... or /hero-ads/... fail to resolve.
    # Convert to relative paths: ./icons/ or ./hero-ads/ or ./automatrix-logo.svg
    # But for Cloudflare Workers they can be relative or root-relative. Relative paths (./) work BOTH in local file:/// and on the deployed web domain!
    content = content.replace('src="/', 'src="./')
    content = content.replace('href="/', 'href="./')
    
    # Fix the logo if needed
    content = content.replace('src="./automatrix-logo.svg"', 'src="./automatrix-logo.svg"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filepath}")

fix_file("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html")
fix_file("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html")
