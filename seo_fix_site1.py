import re, os, glob, json

SITE = "/private/tmp/claude-501/-Users-pablogonzalez-Library-Application-Support-Claude-scratch-workspaces-8fae79b1-0773-4441-bdcc-717619ad1a7f-db38853a-511e-4df2-a7d6-1447d5808f29-scratch-2026-09-21-0ccef2/1f06c324-02f3-4594-978a-f5209fde91ac/scratchpad/sitio1-marketia"
BASE_URL = "https://iapracticaparanegocios.com"
OG_IMAGE = f"{BASE_URL}/assets/og-image.png"

article_files = [f for f in glob.glob(os.path.join(SITE, "articulos", "*.html")) if "plantilla" not in f]

changed = []
skipped = []

for path in article_files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    orig = content

    m = re.search(r'<p class="breadcrumbs"><a href="\.\./">Inicio</a> / ([^<]+)</p>', content)
    if not m:
        skipped.append((path, "no breadcrumb match"))
        continue
    category = m.group(1).strip()

    m2 = re.search(r'<link rel="canonical" href="([^"]+)">', content)
    if not m2:
        skipped.append((path, "no canonical"))
        continue
    canonical = m2.group(1)

    m3 = re.search(r'<h1>([^<]+)</h1>', content)
    title = m3.group(1).strip() if m3 else ""

    article_ld_pattern = re.compile(r'(<script type="application/ld\+json">\s*\{"@context":"https://schema\.org","@type":"Article".*?</script>\n)', re.DOTALL)
    m4 = article_ld_pattern.search(content)
    if not m4:
        skipped.append((path, "no Article JSON-LD found"))
        continue

    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": category, "item": f"{BASE_URL}/#articulos"},
            {"@type": "ListItem", "position": 3, "name": title, "item": canonical},
        ]
    }
    breadcrumb_script = f'<script type="application/ld+json">\n{json.dumps(breadcrumb_ld, ensure_ascii=False)}\n</script>\n'

    if "BreadcrumbList" not in content:
        content = content[:m4.end()] + breadcrumb_script + content[m4.end():]

    ogtype_pattern = re.compile(r'(<meta property="og:type" content="article">\n)')
    m5 = ogtype_pattern.search(content)
    if m5 and 'og:image' not in content:
        social_meta = (
            f'<meta property="og:image" content="{OG_IMAGE}">\n'
            f'<meta property="og:url" content="{canonical}">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:image" content="{OG_IMAGE}">\n'
            f'<meta name="author" content="Equipo MarketIA">\n'
        )
        content = content[:m5.end()] + social_meta + content[m5.end():]

    if content != orig:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        changed.append(path)
    else:
        skipped.append((path, "no changes made (already present?)"))

print(f"Changed: {len(changed)}")
for p in changed:
    print(" +", os.path.basename(p))
print(f"\nSkipped: {len(skipped)}")
for p, reason in skipped:
    print(" -", os.path.basename(p), reason)
