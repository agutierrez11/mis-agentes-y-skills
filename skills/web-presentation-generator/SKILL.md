---
name: web-presentation-generator
description: Genera one-pagers y pitch decks comerciales interactivos en HTML/React/Tailwind para clientes B2B, integrando analíticas de Microsoft Clarity, tracking de lectura en tiempo real por sección y efectos parallax temáticos de alta conversión.
---

# Web Presentation & Pitch Deck Generator Skill

Esta skill enseña al agente de IA cómo crear y desplegar de forma autónoma one-pagers de venta y presentaciones comerciales interactivas en formato web para prospectos y clientes B2B.

---

## 🎨 1. Arquitectura y Diseño de la Presentación Web

Cada presentación comercial generada debe ser interactiva, premium y responsive:

* **Estructura visual:**
  * Fondo oscuro refinado (`slate-950` o `indigo-950`) con detalles de bordes y sombras brillantes (`border-indigo-500/20`, `shadow-indigo-500/10`).
  * Estructura por secciones o diapositivas bien definidas que representen la propuesta de valor, los beneficios, el modelo comercial y el llamado a la acción (CTA).
  * Uso de animaciones de entrada (`Framer Motion` o CSS Transitions) para dar sensación de aplicación web de alto valor.

---

## 🚀 2. Parallax de Fondo Temático
Inyectar un layer de elementos parallax flotantes y sutiles en el fondo que cambien su posición según el scroll del cliente para incrementar la tasa de retención:
* **Fijación:** Utilizar `position: fixed` para cubrir todo el viewport con un `zIndex: 1`.
* **Capas de velocidad (will-change: transform):**
  * Capa lenta (fondo): velocidad `-0.05` a `0.05`, tamaño grande (100px - 130px), opacidad `12%`.
  * Capa intermedia: velocidad `-0.15` a `0.15`, tamaño medio (75px - 90px), opacidad `16%`.
  * Capa rápida (frente): velocidad `-0.28` a `0.28`, tamaño pequeño (50px - 70px), opacidad `20%`.
* **Temática de Iconos:**
  * Para Fintech/Pagos: Bitcoin, Ethereum, tarjetas de crédito, terminales de cobro, códigos QR, USDC, USDT.
  * Para otros sectores: Iconos relevantes al negocio del cliente.

---

## 📊 3. Analíticas de Lectura y Comportamiento en Tiempo Real
El objetivo comercial de estas páginas es permitir al presentador saber si el prospecto realmente leyó la propuesta y qué partes le interesaron más.

### Inyección de Microsoft Clarity:
Agregar en un `useEffect` raíz de la presentación el script de Clarity usando la variable de entorno correspondiente o el ID del proyecto configurado:
```typescript
  useEffect(() => {
    const clarityId = import.meta.env.VITE_CLARITY_ID;
    if (clarityId && typeof window !== 'undefined') {
      (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      })(window,document,"clarity","script",clarityId);
    }
  }, []);
```

### Rastreador de Tiempos por Sección (IntersectionObserver):
Implementar un `IntersectionObserver` que mida cuántos segundos pasa el cliente leyendo cada sección clave de la presentación:
```typescript
  useEffect(() => {
    const activeSections: Record<string, number> = {};

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const id = entry.target.id;
        const now = Date.now();

        if (entry.isIntersecting) {
          activeSections[id] = now;
        } else if (activeSections[id]) {
          const durationSeconds = Math.round((now - activeSections[id]) / 1000);
          delete activeSections[id];

          if (durationSeconds >= 3) { // Ignorar scroll rápido accidental
            // Enviar evento personalizado a Clarity
            if ((window as any).clarity) {
              (window as any).clarity("event", "pitch_section_duration", {
                section: id,
                seconds: durationSeconds.toString()
              });
            }
          }
        }
      });
    }, { rootMargin: '-20% 0px -20% 0px', threshold: 0.15 });

    // Observar las secciones clave de la propuesta comercial
    ['introduccion', 'problema', 'solucion', 'precios', 'contacto'].forEach(id => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  }, []);
```

---

## 🚀 4. Flujo para crear un Pitch Deck Comercial Web
Cuando se solicite una nueva presentación:
1. **Recopilación:** Pedir al usuario el nombre del cliente B2B y el contenido de la propuesta.
2. **Generación:** Crear una plantilla interactiva estructurada con las secciones de la propuesta.
3. **Optimización:** Añadir los efectos visuales y el script de tracking de lectura por sección.
4. **Despliegue:** Proveer el comando de compilación y las instrucciones para que el usuario obtenga el link trackeable para enviar por correo.
