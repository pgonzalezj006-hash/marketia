# MarketIA — iapracticaparanegocios.com

Sitio estático (HTML + CSS) publicado con **GitHub Pages** y dominio en **Cloudflare**.
Versión de septiembre de 2026 con todas las mejoras del plan SEO aplicadas.

## Cómo publicarlo

1. Sustituye el contenido de tu repositorio por el de este ZIP (todo en la raíz del repo).
   Conserva el archivo `CNAME` (contiene `iapracticaparanegocios.com`) y `.nojekyll`.
2. `git add -A && git commit -m "Mejoras SEO septiembre 2026" && git push`
3. En GitHub → Settings → Pages, comprueba que la fuente es la rama principal, carpeta `/ (root)`,
   y que el dominio personalizado sigue siendo `iapracticaparanegocios.com`.
4. En Cloudflare, purga la caché (Caching → Configuration → Purge Everything) para que se vean los cambios al momento.
5. En Google Search Console: envía de nuevo `https://iapracticaparanegocios.com/sitemap.xml`
   y solicita la indexación de la home, los 4 hubs y los 6 artículos nuevos.

## Imágenes (Gemini)

La web ya lleva imágenes provisionales con la marca, así que funciona desde el primer momento.
Para sustituirlas por ilustraciones de Gemini:

1. Abre `IMAGENES-PROMPTS.md`: hay un prompt por imagen con el nombre de archivo exacto.
2. Genera cada imagen en Gemini y guárdala en la carpeta `_imagenes-gemini/` (en la raíz del repo)
   con ese nombre, por ejemplo `_imagenes-gemini/chatbots-ia-para-pymes.png`.
3. En un Mac, desde la raíz del repo: `bash _herramientas/preparar-imagenes.sh`
   (recorta a 1200×630, crea la miniatura 480×252, convierte a JPG y sustituye la provisional).
4. Haz commit y push. La carpeta `_imagenes-gemini/` está en `.gitignore` y no se sube.

## Estructura

- `index.html` — portada
- `herramientas-ia-para-negocios.html`, `ia-para-empezar.html`, `ia-para-marketing-y-redes.html`,
  `ia-para-atencion-al-cliente-y-ventas.html` — las 4 páginas hub
- `articulos/` — 26 artículos (20 ampliados + 6 nuevos)
- `recursos/prompts-ia-para-negocios.pdf` — descargable con 60 prompts
- `assets/` — estilos, script de cookies, logo, favicon e imágenes (`img/` y `img/thumb/`)
- `sitemap.xml` (con `lastmod` e imágenes), `robots.txt`, `ads.txt`, `CNAME`, `404.html`

## Mantenimiento

- **Precios:** las tablas de precios indican «revisado en septiembre de 2026». Revísalas cada mes
  y actualiza la fecha «Actualizado» del artículo y el `<lastmod>` del sitemap cuando cambies algo.
- **Cookies y AdSense:** AdSense solo se carga tras pulsar «Aceptar» (ver `assets/cookie-consent.js`).
  El enlace «Configurar cookies» del pie permite cambiar la elección.
