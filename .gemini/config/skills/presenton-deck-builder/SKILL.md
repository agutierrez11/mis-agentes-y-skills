---
name: presenton-deck-builder
description: Genera automáticamente presentaciones ejecutivas, pitch decks B2B y reportes en formato PowerPoint (.pptx), PDF o HTML utilizando la suite open-source Presenton (https://github.com/presenton/presenton), integrando llaves API propias (Gemini, OpenAI, Claude) y plantillas HTML/Tailwind.
---

# 📊 Presenton Deck Builder — Skill de Generación de Presentaciones IA

Esta Skill le permite al agente orquestar y utilizar la herramienta **Presenton** ([github.com/presenton/presenton](https://github.com/presenton/presenton)) para transformar documentos de estrategia, reportes Markdown y datos comerciales en presentaciones ejecutivas en **PowerPoint (.pptx)**, **PDF** o **HTML**.

---

## 🎯 Caso de Uso Principal
- **Transformación de Artefactos Markdown a PPTX:** Convertir planes de ventas, propuestas para clientes o análisis de mercado (ej. `STARPAGO_COMMERCIAL_ENGINEERING.md`) en diapositivas ejecutivas.
- **Generación Automática por API:** Crear scripts para generar Pitch Decks personalizados para prospectos B2B en segundos.
- **Privacidad Local (BYOK):** Ejecución 100% local o auto-hospedada usando llaves propias (Gemini Flash, OpenAI, Claude).

---

## ⚙️ Modos de Despliegue e Instalación

### Opción A: Vía Docker (Recomendado para Servidor / API)
```bash
# Clonar y levantar servidor local de Presenton
git clone https://github.com/presenton/presenton.git
cd presenton
docker-compose up -d
```
El servicio estará disponible en `http://localhost:3000` con documentación de API en `http://localhost:3000/docs`.

### Opción B: Aplicación de Escritorio Electron (Uso Local en Windows)
1. Descargar el ejecutable `.exe` desde las [Releases oficiales de Presenton](https://github.com/presenton/presenton/releases).
2. Configurar la clave API (Gemini o OpenAI) en el menú de Configuración (`Settings > API Keys`).

---

## 🛠️ Flujo de Trabajo para Generar un Deck (.pptx)

### Paso 1: Formatear la Fuente en Markdown Estructurado
Asegurarse de que el documento tenga encabezados claros por diapositiva:
```markdown
# Título del Slide
## Subtítulo o Mensaje Clave
- Punto 1: Métricas cuantitativas
- Punto 2: Propuesta de valor
- Punto 3: Call to action
```

### Paso 2: Llamada a la API de Presenton / Generador CLI
```python
import requests

url = "http://localhost:3000/api/v1/generate"
payload = {
    "title": "Starpago LATAM Strategy Pitch",
    "markdown_content": open("STARPAGO_COMMERCIAL_ENGINEERING.md").read(),
    "template": "corporate_dark",
    "export_format": "pptx",
    "api_provider": "gemini"
}

response = requests.post(url, json=payload)
with open("Starpago_Strategy_Deck.pptx", "wb") as f:
    f.write(response.content)
```

---

## 🎨 Estilos y Personalización
- **Temas HTML/Tailwind:** Soporta CSS/Tailwind para adaptar la paleta de colores a la identidad de la marca (ej. Dark mode con acentos de la marca).
- **Imágenes Integradas:** Soporta generación de imágenes complementarias con Gemini Flash / DALL-E o búsqueda en Unsplash/Pexels.

---

## 📌 Reglas de Calidad para la Generación de Slides
1. **Regla de 1 Idea por Slide:** No saturar la diapositiva; usar 3 a 4 puntos clave de soporte.
2. **Jerarquía Visual:** Encabezados cortos (H1/H2), seguidos de datos cuantitativos resaltados en negrita.
3. **Cero Texto de Relleno:** Reemplazar párrafos extensos por viñetas ejecutivas en inglés o español según el target.
