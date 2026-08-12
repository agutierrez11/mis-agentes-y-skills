---
name: personal-brand-deck
display_name: Crear presentaciones de marca personal estilo Genspark (Fintech LATAM)
description: |
  Genera presentaciones de marca personal con la misma disciplina visual y narrativa que Genspark usa en sus slides ejecutivos — sistema tipográfico consistente, datos con contexto, narrativa en primera persona, y jerarquía visual clara. Diseñado específicamente para el perfil de Antonio Gutiérrez: Sales Executive en Fintech / Merchant Acquiring / LATAM GTM. Produce decks para thought leadership en LinkedIn, pitches de job interview, one-pagers ejecutivos y decks de propuesta comercial. Reglas irrompibles: una paleta de 3 colores máximo, datos con fuente citada, primera slide siempre con un insight no obvio, última slide siempre con un CTA específico.
metadata:
  short-description: Datos + narrativa + sistema visual = marca personal que se recuerda.
lang: es-MX
category: personal-branding
tags:
  - presentaciones
  - marca-personal
  - fintech
  - latam
  - linkedin
  - thought-leadership
  - genspark
  - sales-executive
canvas:
  width: 1920
  height: 1080
---

# Presentaciones de Marca Personal estilo Genspark — Fintech LATAM

> Datos + narrativa de primera persona + sistema visual consistente = marca que se recuerda.

## Por qué este skill existe

Genspark genera presentaciones ejecutivas con una disciplina específica:
- **Dato primero, contexto después** — nunca dato flotante sin marco
- **Una idea por slide** — sin slides-panfleto con 7 bullets
- **Narrativa de primera persona** — el presentador es el protagonista
- **Consistencia tipográfica** — mismo sistema de jerarquía en cada slide
- **Visualización honesta** — los gráficos reflejan la historia, no la adornan

Este skill aplica esa disciplina al perfil de un Sales Executive senior en Fintech / Merchant Acquiring operando en LATAM.

---

## Sistema de Diseño (no negociable)

### Tokens de color (extraídos del HTML real de Genspark)
```css
:root {
  --ink:    #0A0A0A;  /* texto principal — casi negro */
  --paper:  #F8F8F6;  /* fondo — blanco cálido */
  --accent: #0066FF;  /* azul eléctrico — datos, CTA, líneas */
  --mute:   #6E6E6E;  /* labels secundarios, footers */
  --line:   #E4E4E1;  /* divisores, bordes */
}
```
**Regla**: el ámbar/rojo solo para 1 número crítico por deck. Nunca decorativo.

### Tipografía real de Genspark
```css
--sans: 'Manrope', ui-sans-serif, system-ui, sans-serif;
--mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
```
- **Headlines**: Manrope 700, 80-132px, letter-spacing -0.04em
- **Body**: Manrope 400, 20-24px, line-height 1.45
- **Labels/Tags**: JetBrains Mono 400, 12-15px, letter-spacing 0.08-0.12em, UPPERCASE
- **Datos destacados**: Manrope 800, 48-80px, color var(--accent)

### Grid real de Genspark (1920×1080)
- Canvas: `1920px × 1080px`, overflow hidden
- Márgenes laterales: **96px** (no 80px)
- Margen superior: **72px**
- Zona footer: `top: 984px` — línea divisora + texto 13px
- Número de slide: bottom-right `left: 1700px`
- Zona de respiro: mínimo 40% del canvas vacío
- Posicionamiento: absoluto con `data-object="true"` por elemento

---

## Arquitectura de Slides por tipo de deck

### Deck de Thought Leadership (LinkedIn / Conferencias)
```
Slide 1 — INSIGHT OPENER
  • Un dato contraintuitivo del sector
  • Subtítulo: la tensión o paradoja
  • Sin logo ni nombre — el dato entra primero

Slide 2 — CONTEXTO REGIONAL
  • Tabla comparativa LATAM (máx 5 países)
  • Fuente citada en footer 10pt

Slide 3 — EL PROBLEMA REAL
  • El comportamiento humano, no la tecnología
  • Primera persona: "He visto esto en campo..."

Slide 4 — MI PERSPECTIVA
  • Tesis en 1 oración, negrita, centrada, 36pt
  • 3 bullets de evidencia (no más)

Slide 5 — IMPLICACIÓN PARA EL MERCADO
  • ¿Qué cambia si esto es cierto?
  • Marco temporal: "En los próximos 18-24 meses..."

Slide 6 — CTA
  • Pregunta de engagement específica y abierta
```

### Deck de Entrevista / Pitch Ejecutivo
```
Slide 1 — QUIÉN SOY EN UNA ORACIÓN
  • Formato: Nombre | Rol | Resultado más relevante

Slide 2 — EL PROBLEMA QUE RESUELVO
  • El dolor del hiring manager, no el job description

Slide 3 — MIS NÚMEROS (solo los 3 mejores)
  • Formato: [Número] vs [Benchmark] — [Qué significó]

Slide 4 — MI MÉTODO (diferenciador)
  • El framework nombrable y repetible que uso

Slide 5 — 30-60-90 DÍAS
  • 3 columnas con acciones concretas y mensurables

Slide 6 — POR QUÉ AQUÍ, POR QUÉ AHORA
  • Conexión entre tu tesis de mercado y la empresa
```

### One-Pager Ejecutivo (WhatsApp / Email)
```
Layout: 4 cuadrantes en una sola slide

Q1 (top-left):    Titular + subtítulo de posicionamiento
Q2 (top-right):   3 métricas clave en grande
Q3 (bottom-left): Contexto de mercado (1 dato LATAM)
Q4 (bottom-right): CTA + datos de contacto

Regla: debe leerse en 8 segundos. Si no, elimina.
```

---

## Reglas editoriales (nunca violar)

1. **Dato primero** — nunca empieces con opinión sin respaldo
2. **Fuente siempre** — todo número lleva fuente en footer
3. **Una idea por slide** — dos ideas = dos slides
4. **Primera persona** — "yo hice", "yo vi en campo" — no corporativismo
5. **Máximo 3 bullets** — si tienes más, reorganiza
6. **El título es la conclusión** — el cuerpo es solo la evidencia
7. **Sin stock photos** — datos visualizados, íconos simples, o nada
8. **Termina con acción** — último slide siempre con next step específico

---

## Datos de referencia del perfil

```yaml
perfil:
  nombre: Antonio Gutiérrez Jiménez
  rol: Sales Executive | Fintech | Merchant Acquiring
  especialidad: GTM LATAM, SMB Acquisition, Canal Outbound

metricas_clave:
  - label: TPV gestionado
    valor: $69M
    contexto: Adquisición outbound Clip 2022
  - label: Mix outbound
    valor: 75.3%
    contexto: vs promedio industria ~40-50%
  - label: Ticket outbound vs inbound
    valor: 2.8x
    contexto: Cuentas hospitality y gasolineras

sectores_foco:
  - Hospitalidad (restaurantes, hoteles)
  - Gasolineras y estaciones de servicio
  - Retail PyME
  - eCommerce LATAM

tesis_de_mercado:
  - "El QR en México está frenado por confianza, no por infraestructura"
  - "El outbound data-driven supera al inbound en ticket en B2B fintech"
  - "El comercio mexicano necesita un interlocutor que entienda finanzas Y operación"

herramientas_diferenciadoras:
  - NERV (GTM intelligence engine propietario)
  - LeadTrack con Supabase (pipeline tracker propio)
  - SPIN Selling + Socratic Selling
  - Data enrichment: DENUE, Google Maps scraping, Lusha
```

---

## Cómo invocar este skill

### Para thought leadership:
> "Crea un deck de thought leadership sobre [tema] usando personal-brand-deck.
> Usa los datos de referencia de mi perfil donde aplique.
> 6 slides, paleta azul marino / azul eléctrico / blanco roto."

### Para una entrevista:
> "Crea un deck de entrevista para [empresa] en el rol de [puesto].
> El problema que resuelven: [descripción].
> Usa mis 3 métricas clave y NERV como diferenciador."

### Para un one-pager:
> "Crea un one-pager ejecutivo para compartir con [audiencia].
> Énfasis en: [métrica o diferenciador específico]."

---

## Referencias del sistema visual

- Genspark: metodología observada en executive deck generation (jerarquía, dato-primero, breathing room)
- Datos de Antonio Gutiérrez: análisis propio y auditoría Clip 2022
- Benchmarks QR LATAM: cronista.com, colombiafintech.co, abc.com.py, iproup.com
- Framework tipográfico: principios Vignelli de restricción (máx 2 pesos)
