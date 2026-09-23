import json

SITE = "/private/tmp/claude-501/-Users-pablogonzalez-Library-Application-Support-Claude-scratch-workspaces-8fae79b1-0773-4441-bdcc-717619ad1a7f-db38853a-511e-4df2-a7d6-1447d5808f29-scratch-2026-09-21-0ccef2/1f06c324-02f3-4594-978a-f5209fde91ac/scratchpad/sitio1-marketia"
BASE = "https://iapracticaparanegocios.com"
OG = f"{BASE}/assets/og-image.png"

articles = {
  "cual-es-la-mejor-ia-para-tu-negocio.html": {"title": "Cuál es la mejor IA para tu negocio: comparativa 2026", "desc": "Comparamos ChatGPT, Claude y Gemini para decidir cuál conviene según el tamaño y el tipo de tu negocio.", "cat": "Primeros pasos"},
  "mejores-prompts-chatgpt-para-negocios.html": {"title": "Los mejores prompts de ChatGPT para negocios (con ejemplos)", "desc": "Colección de prompts de ChatGPT listos para copiar y adaptar a marketing, atención al cliente y ventas de tu negocio.", "cat": "Prompts y uso práctico"},
  "chatgpt-para-empresarios-usos.html": {"title": "ChatGPT para empresarios: 10 usos que sí funcionan", "desc": "Diez formas concretas en que dueños de negocio están usando ChatGPT hoy, más allá de redactar textos.", "cat": "Prompts y uso práctico"},
  "herramientas-ia-gratis-vs-pago.html": {"title": "Herramientas de IA gratis vs de pago: cuál elegir", "desc": "Cómo decidir cuándo una herramienta de IA gratuita es suficiente para tu negocio, y cuándo vale la pena pagar por más.", "cat": "Webs"},
  "guia-ia-marketing-pequenos-negocios.html": {"title": "Cómo usar la inteligencia artificial en el marketing de tu negocio", "desc": "Guía práctica y sin jerga sobre cómo usar la inteligencia artificial en el marketing de un negocio pequeño.", "cat": "Guía principal"},
  "como-usar-ia-para-tu-negocio-paso-a-paso.html": {"title": "Cómo usar la IA para tu negocio: guía paso a paso", "desc": "Guía práctica paso a paso para empezar a usar inteligencia artificial en tu negocio, aunque nunca hayas probado ninguna herramienta de IA.", "cat": "Primeros pasos"},
  "ia-para-pequenos-negocios-por-donde-empezar.html": {"title": "IA para pequeños negocios: por dónde empezar", "desc": "Guía de orientación para dueños de negocios pequeños que quieren empezar a usar IA pero no saben cuál es el primer paso.", "cat": "Primeros pasos"},
  "errores-comunes-ia-marketing.html": {"title": "Errores comunes al usar IA en marketing (y cómo evitarlos)", "desc": "Los errores más frecuentes al usar inteligencia artificial en el marketing de un negocio pequeño, y cómo evitar cada uno.", "cat": "Errores y buenas prácticas"},
  "como-saber-si-un-texto-suena-a-ia.html": {"title": "Cómo saber si un texto suena “a IA” (y evitarlo)", "desc": "Las señales más comunes de que un texto generado por IA suena genérico, y cómo corregirlas antes de publicar.", "cat": "Errores y buenas prácticas"},
  "mejores-herramientas-ia-redes-sociales.html": {"title": "Mejores herramientas de IA para redes sociales en 2026", "desc": "Herramientas de IA para planificar, escribir y diseñar contenido de redes sociales para tu negocio, con y sin costo.", "cat": "Redes sociales y contenido"},
  "calendario-contenido-con-ia.html": {"title": "Cómo crear un calendario de contenido con IA", "desc": "Cómo generar un calendario de publicaciones para un mes completo usando IA, adaptado a las fechas relevantes de tu negocio.", "cat": "Redes sociales y contenido"},
  "ia-marketing-tienda-pequena.html": {"title": "Cómo usar IA en marketing si tienes una tienda pequeña", "desc": "Aplicaciones concretas de IA para tiendas físicas u online pequeñas: descripciones de producto, promociones y atención al cliente.", "cat": "Casos prácticos"},
  "crear-pagina-web-gratis-con-ia.html": {"title": "Cómo crear una página web gratis para tu negocio con IA", "desc": "Cómo crear la web de tu negocio usando herramientas de IA, sin saber programar y sin gastar en un desarrollador.", "cat": "Webs y presencia online"},
  "promocionar-negocio-sin-presupuesto.html": {"title": "IA para promocionar tu negocio sin presupuesto grande", "desc": "Formas de usar IA para ganar visibilidad sin gastar en publicidad, aprovechando lo que ya tienes.", "cat": "Publicidad y promoción"},
  "como-hacer-publicidad-con-ia.html": {"title": "Cómo hacer publicidad para tu negocio con IA", "desc": "Cómo usar IA para escribir anuncios, elegir públicos y mejorar campañas de publicidad de un negocio pequeño con presupuesto limitado.", "cat": "Publicidad y promoción"},
  "chatbots-ia-para-pymes.html": {"title": "Chatbots con IA para pymes: cuánto cuestan y cómo elegir uno", "desc": "Guía práctica sobre chatbots de IA para pequeños negocios: qué hacen, cuánto cuestan y cómo elegir el adecuado para tu caso.", "cat": "Atención al cliente"},
  "como-responder-resenas-con-ia.html": {"title": "Cómo usar IA para responder reseñas de clientes", "desc": "Cómo responder reseñas positivas y negativas usando IA, sin sonar a plantilla ni perder el tono cercano de tu negocio.", "cat": "Atención al cliente"},
  "automatizar-atencion-cliente-sin-perder-cercania.html": {"title": "Cómo automatizar la atención al cliente sin perder cercanía", "desc": "Cómo usar IA para responder más rápido a tus clientes sin que tu negocio pierda el trato cercano que lo diferencia.", "cat": "Atención al cliente"},
  "ia-para-email-marketing.html": {"title": "IA para email marketing: plantillas y ejemplos reales", "desc": "Cómo usar IA para escribir correos de marketing que se abren y se leen, con plantillas reales que puedes adaptar.", "cat": "Email marketing y ventas"},
  "ia-seguimiento-clientes-potenciales.html": {"title": "IA para seguimiento de clientes potenciales (leads)", "desc": "Cómo usar IA para no perder el hilo de clientes interesados que todavía no compraron, sin necesidad de un CRM complejo.", "cat": "Email marketing y ventas"},
}

hubs = [
    {
        "slug": "herramientas-ia-para-negocios",
        "title": "Herramientas de IA para negocios: cómo elegir y comparar",
        "meta_desc": "Guía para comparar herramientas de IA generales (ChatGPT, Claude, Gemini) y elegir la más adecuada para tu negocio, con prompts y comparativas gratis vs. pago.",
        "intro": "Elegir una herramienta de IA para tu negocio no debería significar probar diez aplicaciones al azar. En esta guía reunimos las comparativas y recursos que necesitas para decidir con criterio: qué asistente conversacional conviene según tu caso, cómo sacarle partido con prompts ya probados, y cuándo tiene sentido pagar por una versión de pago en vez de quedarte con la gratuita. Si vienes de cero, empieza por la comparativa de asistentes; si ya usas una herramienta, los prompts y el análisis gratis vs. pago te ayudarán a exprimirla mejor.",
        "children": ["cual-es-la-mejor-ia-para-tu-negocio.html", "mejores-prompts-chatgpt-para-negocios.html", "chatgpt-para-empresarios-usos.html", "herramientas-ia-gratis-vs-pago.html"],
    },
    {
        "slug": "ia-para-empezar",
        "title": "IA para empezar: guía completa para tu negocio",
        "meta_desc": "Guía completa para empezar a usar inteligencia artificial en tu negocio desde cero: primeros pasos, errores comunes y cómo evitar que tus textos suenen a IA.",
        "intro": "Si nunca has usado inteligencia artificial en tu negocio, el mayor obstáculo no es la tecnología, es saber por dónde empezar. Este hub agrupa la guía completa de MarketIA sobre los primeros pasos: qué es realmente la IA aplicada al marketing, cómo dar tus primeros pasos sin perder tiempo probando herramientas al azar, y los errores más frecuentes que cometen los negocios que recién empiezan — incluyendo el error de publicar textos que “suenan a IA” y alejan a los clientes en vez de acercarlos. Empieza por la guía principal y sigue el orden sugerido si es tu primera vez.",
        "children": ["guia-ia-marketing-pequenos-negocios.html", "como-usar-ia-para-tu-negocio-paso-a-paso.html", "ia-para-pequenos-negocios-por-donde-empezar.html", "errores-comunes-ia-marketing.html", "como-saber-si-un-texto-suena-a-ia.html"],
    },
    {
        "slug": "ia-para-marketing-y-redes",
        "title": "IA para marketing y redes sociales",
        "meta_desc": "Cómo usar IA para redes sociales, calendarios de contenido, publicidad y páginas web de tu negocio: herramientas y guías prácticas sin presupuesto grande.",
        "intro": "El marketing de un negocio pequeño no tiene el presupuesto ni el equipo de una gran marca, y ahí es donde la IA marca más diferencia: permite planificar un mes de contenido en minutos, escribir anuncios sin agencia, o tener una web propia sin contratar a un desarrollador. En este hub reunimos las guías de MarketIA sobre redes sociales, calendario de contenido, publicidad y presencia online, con casos aplicados a negocios físicos como una tienda pequeña. Es el punto de partida si tu objetivo es ganar visibilidad con los recursos que ya tienes.",
        "children": ["mejores-herramientas-ia-redes-sociales.html", "calendario-contenido-con-ia.html", "ia-marketing-tienda-pequena.html", "crear-pagina-web-gratis-con-ia.html", "promocionar-negocio-sin-presupuesto.html", "como-hacer-publicidad-con-ia.html"],
    },
    {
        "slug": "ia-para-atencion-al-cliente-y-ventas",
        "title": "IA para atención al cliente y ventas",
        "meta_desc": "Guías prácticas de IA para atención al cliente, chatbots, respuesta a reseñas, email marketing y seguimiento de clientes potenciales en negocios pequeños.",
        "intro": "Responder rápido sin perder cercanía es el equilibrio más difícil de conseguir en la atención al cliente de un negocio pequeño, y es exactamente donde la IA puede ayudar sin sustituir el trato humano. Este hub agrupa las guías de MarketIA sobre chatbots, respuesta a reseñas, automatización de atención al cliente, email marketing y seguimiento de clientes potenciales — todo pensado para que la tecnología libere tiempo sin que tu negocio se sienta frío o impersonal.",
        "children": ["chatbots-ia-para-pymes.html", "como-responder-resenas-con-ia.html", "automatizar-atencion-cliente-sin-perder-cercania.html", "ia-para-email-marketing.html", "ia-seguimiento-clientes-potenciales.html"],
    },
]

hub_by_slug = {h["slug"]: h["title"] for h in hubs}

def render_hub(hub):
    slug = hub["slug"]
    canonical = f"{BASE}/{slug}.html"
    cards = []
    for fn in hub["children"]:
        a = articles[fn]
        cards.append(
            f'    <article class="card"><span class="cat">{a["cat"]}</span><h3><a href="articulos/{fn}">{a["title"]}</a></h3><p>{a["desc"]}</p></article>'
        )
    cards_html = "\n".join(cards)

    other_hubs = [h for h in hubs if h["slug"] != slug]
    other_links = "\n".join(
        f'      <li><a href="{h["slug"]}.html">{h["title"]}</a></li>' for h in other_hubs
    )

    breadcrumb_ld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": hub["title"], "item": canonical},
        ]
    }
    collection_ld = {
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": hub["title"], "description": hub["meta_desc"], "url": canonical,
        "isPartOf": {"@type": "WebSite", "name": "MarketIA", "url": f"{BASE}/"}
    }

    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{hub["title"]} — MarketIA</title>
<meta name="description" content="{hub["meta_desc"]}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{hub["title"]} — MarketIA">
<meta property="og:description" content="{hub["meta_desc"]}">
<meta property="og:type" content="website">
<meta property="og:image" content="{OG}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{OG}">
<meta name="author" content="Equipo MarketIA">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="assets/styles.css">
<script type="application/ld+json">
{json.dumps(breadcrumb_ld, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(collection_ld, ensure_ascii=False)}
</script>
<script defer src="assets/cookie-consent.js"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9723862717735653" crossorigin="anonymous"></script>
</head>
<body>
<div id="cookie-banner" class="cookie-banner" hidden>
  <p>Usamos cookies propias y de terceros (incluyendo anuncios) para mejorar tu experiencia. Puedes leer más en nuestra <a href="politica-privacidad.html">política de privacidad</a>.</p>
  <div class="cookie-actions"><button id="cookie-reject" type="button">Rechazar</button><button id="cookie-accept" type="button">Aceptar</button></div>
</div>
<header class="site-header"><div class="wrap"><a href="./" class="logo">Market<span>IA</span></a><nav class="site-nav"><a href="#articulos">Artículos</a><a href="sobre-nosotros.html">Sobre nosotros</a><a href="contacto.html">Contacto</a></nav></div></header>

<div class="article-header">
  <div class="wrap-narrow">
    <p class="breadcrumbs"><a href="./">Inicio</a> / {hub["title"]}</p>
    <span class="cat">Guía por tema</span>
    <h1>{hub["title"]}</h1>
  </div>
</div>

<div class="article-body">
  <p>{hub["intro"]}</p>
</div>

<div class="wrap-narrow">
  <h2 class="section-title">Artículos de esta guía</h2>
  <div class="card-grid">
{cards_html}
  </div>

  <div class="related">
    <h2>Explora las otras guías de MarketIA</h2>
    <ul>
{other_links}
    </ul>
  </div>
</div>

<footer class="site-footer"><div class="wrap"><p>© 2026 MarketIA — contenido sobre IA aplicada al marketing.</p><div class="footer-links"><a href="sobre-nosotros.html">Sobre nosotros</a><a href="contacto.html">Contacto</a><a href="politica-privacidad.html">Privacidad</a></div></div></footer>
</body>
</html>
"""

for hub in hubs:
    out = render_hub(hub)
    path = f"{SITE}/{hub['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", path)
