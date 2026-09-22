# MarketIA — Sitio 1

IA aplicada al marketing de pequeños negocios. Sitio estático (HTML/CSS puro), sin build ni dependencias.

## Progreso de contenido: 11 / 30 artículos publicados

Meta de 30 artículos porque es el mínimo orientativo para que AdSense considere la solicitud. Los 19 restantes están mapeados en `index.html` (marcados "Próximamente") — se van escribiendo con el prompt de la sección 13 del plan, a un ritmo sostenido (no todos de golpe: publicar en bloque grande y sin cuidado es justo lo que penaliza el sistema de contenido útil de Google).

## Estructura

```
index.html                 → página de inicio
articulos/
  guia-ia-marketing-pequenos-negocios.html   → artículo pilar (publicado)
  articulo-plantilla.html                     → plantilla para artículos nuevos
sobre-nosotros.html
contacto.html
sitemap.xml
robots.txt
assets/styles.css
```

## Cómo publicar (ver también la sección 18 y 19 del documento del plan)

1. Crea un repositorio nuevo en GitHub y sube todo el contenido de esta carpeta.
2. En Cloudflare → Workers & Pages → Create → Pages → Connect to Git → elige el repositorio.
   - Framework preset: **None**
   - Comando de build: (vacío)
   - Carpeta de salida: `/` (raíz)
3. Compra el dominio en Cloudflare Registrar (o el que hayas elegido) y conéctalo en el proyecto de Pages, pestaña "Custom domains".
4. Antes de publicar de verdad:
   - Reemplaza `marketia.com` en todos los `<link rel="canonical">` y en `sitemap.xml`/`robots.txt` por tu dominio real si es distinto.
   - Reemplaza el correo de `contacto.html`.
5. Da de alta el dominio en Google Search Console y envía `sitemap.xml` (registro TXT vía Cloudflare DNS — ver sección 19).

## Publicar un artículo nuevo

1. Copia `articulos/articulo-plantilla.html`, renómbralo con el slug del nuevo artículo.
2. Usa el prompt de la sección 13 del plan para generar el contenido y pégalo en la plantilla.
3. Añade una tarjeta nueva en `index.html` (dentro de `.card-grid`) enlazando al artículo.
4. Añade la URL nueva a `sitemap.xml`.
5. Sube los cambios al repositorio — Cloudflare Pages lo publica automáticamente.
