# 📦 Guía de Migración Bulletproof: Todo Antigravity a tu Laptop Nueva
> **Protocolo de Respaldos & Transición de Hardware (Zero-Downtime)**  
> *Para migrar todo tu entorno, 24 skills, reglas globales y proyectos a tu nueva Dell*

---

## 📌 ¿Qué compone tu Entorno de Antigravity?

Todo tu conocimiento, tus agentes, tus proyectos y tus configuraciones viven en **3 lugares específicos** de tu equipo actual:

1. **Configuración Global (`C:\Users\Antonio\.gemini\config\`):** Contiene tus reglas globales, tus 24 habilidades agénticas personalizadas y tus plugins.
2. **Proyectos Locales (`C:\Users\Antonio\.gemini\antigravity-ide\scratch\`):** Contiene el código fuente de Radar Comercial, Paymind, Toku, Incode y tus bóvedas.
3. **Repositorios Centrales en GitHub:**
   - [`agutierrez11/mis-agentes-y-skills`](https://github.com/agutierrez11/mis-agentes-y-skills) (El respaldo de todas tus habilidades).
   - [`agutierrez11/Radar-comercial-linkedin`](https://github.com/agutierrez11/Radar-comercial-linkedin) (Tu proyecto principal).

---

## 🛠️ PASO 1: En tu Laptop Actual (Antes de cambiar) — 5 Minutos

1. **Asegurar que todo esté en GitHub:**
   Corres este comando o nos pides hacer el último commit:
   `git add . && git commit -m "backup final laptop anterior" && git push`
2. **Copiar las 2 Carpetas de Oro a una Memoria USB o Google Drive / OneDrive:**
   - 📁 **Carpeta A:** `C:\Users\Antonio\.gemini\config\`
   - 📁 **Carpeta B:** `C:\Users\Antonio\.gemini\antigravity-ide\scratch\`

---

## 🛠️ PASO 2: En tu Laptop Nueva (Al desempaquetar) — 10 Minutos

1. **Instalar programas base (Gratis):**
   - Instalas **Git para Windows** ([git-scm.com](https://git-scm.com/)).
   - Instalas **Antigravity IDE** ([antigravity.google.com](https://antigravity.google.com)).
2. **Abrir sesión en Antigravity IDE:**
   - Inicias sesión con tu misma cuenta.

---

## 🛠️ PASO 3: Restaurar tu Entorno (Cero Errores) — 3 Minutos

1. Cierras Antigravity por un momento.
2. **Copias la Carpeta A** y la pegas en:
   `C:\Users\Antonio\.gemini\config\`
3. **Copias la Carpeta B** y la pegas en:
   `C:\Users\Antonio\.gemini\antigravity-ide\scratch\`
4. *(Alternativa opcional con Git)*: En lugar de copiar la carpeta B, simplemente abres una terminal en la laptop nueva y clonas tus repos de GitHub:
   ```bash
   cd C:\Users\Antonio\.gemini\antigravity-ide\scratch\
   git clone https://github.com/agutierrez11/mis-agentes-y-skills.git
   git clone https://github.com/agutierrez11/Radar-comercial-linkedin.git
   ```

---

## 🎉 PASO 4: ¡Abrir Antigravity y Listo!

Al abrir Antigravity IDE en tu laptop nueva:
* Todos tus **790 skills** y **24 habilidades personalizadas** aparecerán automáticamente activos.
* Tus reglas globales (`user_global`) seguirán vigentes.
* Tu **Dashboard de Radar Comercial** abrirá con toda tu data local e historial intacto.
* Cero pérdida de información, cero scripts rotos y cero reconfiguraciones.
