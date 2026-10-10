import re

def update_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Make the hero showcase card much more spacious, with aspect-ratio preservation and deep blue glassmorphism
    old_css = """.hero-holo-showcase {
      margin: 40px auto 60px;
      max-width: 1040px;
      border-radius: 20px;
      border: 1px solid var(--border-cyan);
      box-shadow: 0 0 60px rgba(6, 182, 212, 0.2), inset 0 0 40px rgba(6, 182, 212, 0.05);
      overflow: hidden;
      position: relative;
      background: #000;
    }
    .hero-holo-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: center;
    }
    @media (max-width: 860px) {
      .hero-holo-grid {
        grid-template-columns: 1fr;
      }
    }
    .hero-holo-img-wrap {
      position: relative;
      overflow: hidden;
      height: 100%;
      min-height: 440px;
    }
    .hero-holo-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .hero-holo-content {
      padding: 40px 36px;
      text-align: left;
      background: linear-gradient(135deg, rgba(13, 17, 28, 0.95) 0%, rgba(6, 8, 14, 0.98) 100%);
    }"""

    new_css = """.hero-holo-showcase {
      margin: 40px auto 60px;
      max-width: 1120px;
      border-radius: 24px;
      border: 1px solid rgba(0, 240, 255, 0.45);
      box-shadow: 0 0 80px rgba(13, 98, 254, 0.35), inset 0 0 50px rgba(0, 240, 255, 0.08);
      overflow: hidden;
      position: relative;
      background: rgba(3, 20, 50, 0.65);
      backdrop-filter: blur(24px);
    }
    .hero-holo-grid {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      align-items: center;
    }
    @media (max-width: 900px) {
      .hero-holo-grid {
        grid-template-columns: 1fr;
      }
    }
    .hero-holo-img-wrap {
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, rgba(13, 98, 254, 0.25) 0%, transparent 70%);
      padding: 16px;
    }
    .hero-holo-img-wrap img {
      width: 100%;
      height: auto;
      max-height: 620px;
      object-fit: contain;
      border-radius: 16px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(0, 240, 255, 0.25);
    }
    .hero-holo-content {
      padding: 48px 40px;
      text-align: left;
      background: linear-gradient(135deg, rgba(4, 25, 65, 0.9) 0%, rgba(2, 11, 30, 0.95) 100%);
    }"""

    content = content.replace(old_css, new_css)

    # Let's also adjust the typography to be cleaner and less stretched:
    content = content.replace("font-family: 'Syne', -apple-system, sans-serif;", "font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated", filepath)

update_file("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html")
update_file("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html")
