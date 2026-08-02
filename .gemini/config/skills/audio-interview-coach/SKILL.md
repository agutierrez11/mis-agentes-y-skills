---
name: audio-interview-coach
description: >
  Entrena respuestas orales ejecutivas en inglés para entrevistas de ventas B2B.
  Genera preguntas, evalúa respuestas (duración, numeración oral, muletillas),
  y entrega retroalimentación fonética y de estructura en tiempo real.
  Especializado en equipos de Asia (45-60s, numeración First/Second/Third, cero fillers).
---

# Audio Interview Coach — Entrenador de Entrevistas Ejecutivas en Inglés

## Cuándo usar esta Skill

- Usuario tiene una entrevista próxima en inglés (especialmente con equipos internacionales)
- Necesita practicar respuestas de 45-60 segundos con estructura STAR
- Quiere detección de muletillas y fillers en inglés
- Prepara un pitch de Full-Cycle Sales, alto riesgo (iGaming, Payments, Crypto)

---

## 🎯 Reglas de Comunicación Ejecutiva para Equipos en Asia

| Regla | ✅ Correcto | ❌ Evitar |
|-------|-----------|---------|
| Duración | 45-60 segundos | >90 segundos |
| Estructura | *1. First... 2. Second... 3. Third* | Narrativa libre sin numeración |
| Vocabulario | TPV, acquiring rate, FX fee | "a kind of", "how I say" |
| Inglés | /skrei-piŋ/ (scraping) | "scrapping" |
| Inicio | "My experience covers..." | "Ehhh well..." |

---

## 📋 Batería Maestra — 6 Preguntas Clave (Full-Cycle Sales / Payments)

### Q1. Tell me about yourself and your acquiring background.
> *My background spans the entire payment acquiring chain across three verticals:  
> First, merchant onboarding at Clip — 500 MIDs/month, 94% approval rate.  
> Second, enterprise integration at Fiserv — direct API connections to processors.  
> Third, cross-border acquiring — Pix, OXXO, PSE for high-risk merchants.  
> My north star metric has always been TPV growth. That's why I'm here — StarPago moves the needle in exactly that space.*

### Q2. Can you explain your Full-Cycle Sales experience in payments?
> *My Full-Cycle experience covers three phases:  
> First, Prospecting — Python data pipelines scraping 2,000+ merchants/month by MCC code.  
> Second, C-Level Pitching — negotiating authorization rates and FX fees with CFOs.  
> Third, Technical Onboarding — API integration activation to generate immediate TPV.  
> The result: I've onboarded merchants generating $3M+ TPV in the first 90 days.*

### Q3. How do you handle high-risk verticals (iGaming, Forex, Crypto)?
> *Three disciplines I apply every time:  
> First, pre-underwriting — reviewing chargeback ratios before pitch, typically below 0.9%.  
> Second, acquiring relationship management — knowing which BIN sponsors accept specific MCC codes.  
> Third, compliance packaging — presenting AML/KYC documentation proactively to speed approval.  
> High-risk is not a problem; it's a premium opportunity if you manage the risk architecture correctly.*

### Q4. How do you deal with technical API friction during closing?
> *I treat API friction as a sales blocker, not a technical issue. My approach is three steps:  
> First, identify the integration bottleneck early — before the contract is signed.  
> Second, deploy a sandbox environment with sample code in the merchant's language — Python or Node.  
> Third, escalate to a solutions engineer only if the blocker exceeds 48 hours.  
> Result: I reduce average integration time from 30 days to under 10 days.*

### Q5. What are your salary expectations?
> *My expectation is competitive with the cross-border payments market.  
> First, I'm looking for a base that reflects the full-cycle ownership of the role.  
> Second, I want performance incentives tied directly to TPV generated — that aligns our incentives.  
> Third, I'm flexible on structure if the upside potential is there.  
> I'm open to discussing a number once I understand the full compensation architecture.*

### Q6. What is your current employment situation?
> *I am currently between roles — intentionally.  
> First, I concluded my last assignment after successfully deploying a cross-border acquiring pipeline for 3 high-risk verticals.  
> Second, I took this period to sharpen my technical skills in payment integrations and API pipelines.  
> Third, I am now specifically targeting roles in cross-border payment sales where I can deploy that stack immediately.  
> StarPago is exactly that role.*

---

## 🔍 Filtro de Muletillas — Lista Negra

Detectar y eliminar **automáticamente** estas expresiones:

| Muletilla | Reemplazo ejecutivo |
|-----------|-------------------|
| `a kind of` | sustantivo directo ("a data pipeline", "an acquiring framework") |
| `how I say` | eliminar, reformular directo |
| `scrapping` | "scraping" /skrei-piŋ/ |
| `hair quake` | "earthquake" /ˈɜːrθkweɪk/ |
| `cause for example` | "for instance," |
| `slavo` | "I'd say" o eliminar |
| `basically` | eliminar o reemplazar con dato exacto |

---

## ⏱️ Evaluación Automática por Respuesta

```python
words = response.split()
word_count = len(words)
est_seconds = round(word_count / 2.3)  # ~140 wpm promedio

# Semáforo:
# ✅ 30-65s  → Duración perfecta
# ⚠️ 65-90s  → Demasiado largo, recortar
# ❌ >90s    → Monólogo, volver a escribir

has_numbering = any(n in response.lower() for n in ["first", "second", "third"])
fillers = ["a kind of", "how i say", "scrapping", "hair quake", "basically"]
found = [f for f in fillers if f in response.lower()]
```

---

## 🌐 Integración en HTML (Web Speech API — Gratis, Sin Backend)

```javascript
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';
recognition.continuous = true;
recognition.interimResults = true;

recognition.onresult = (event) => {
  const transcript = Array.from(event.results)
    .map(r => r[0].transcript).join('');
  // → Enviar a evaluador de muletillas y estructura
};

// TTS para retroalimentación de voz
const speak = (text) => {
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US'; u.rate = 0.95;
  speechSynthesis.speak(u);
};
```
