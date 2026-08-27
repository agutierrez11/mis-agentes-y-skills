# 🎙️ Local Voice & Audio Personalization (`local-voice-cloning`)

Esta skill proporciona los patrones, flujos de trabajo e instrucciones para integrar **clonación de voz zero-shot, sintesis TTS y doblaje de audio 100% local** en pipelines de prospección B2B y demos de ventas, sin depender de servicios en la nube ni exponer datos de audio.

Inspirado en la arquitectura local de **`debpalash/OmniVoice-Studio`**.

---

## 📌 ¿Cuándo usar esta Skill?

- Al crear secuencias de prospección B2B outbound que requieran **notas de voz personalizadas en DMs (LinkedIn, WhatsApp, Email)**.
- Para generar locuciones y audios explicativos en demos interactivas o presentaciones ejecutivas (`huashu-design`).
- Cuando se requiera privacidad total (Zero-Knowledge) procesando archivos de audio sin enviar datos a APIs externas (ElevenLabs).

---

## 🛡️ Flujo de Trabajo para Prospección por Audio

```
[ Texto del Mensaje Personalizado (DM / Pitch) ]
                     │
                     ▼
       [ Muestra de Voz de Referencia ] (3-10 segundos .wav)
                     │
                     ▼
      [ Motor Local (OmniVoice / TTS) ]
                     │
                     ▼
  [ Audio Saliente Personalizado (.mp3 / .wav) ]
```

---

## ⚙️ Directrices de Implementación

### 1. Entorno de Ejecución Local
- Ejecutar motores TTS/Voice Cloning utilizando runtimes eficientes como **Bun** y gestores de paquetes Python ultrarápidos como **`uv`**.
- Mantener las muestras de voz de referencia localmente en el silo del usuario.

### 2. Formato de Notas de Voz B2B
- **Duración ideal:** 15 a 30 segundos máximo.
- **Estructura del Script:** 
  1. *Hook personal:* Mencionar nombre del prospecto y un logro reciente.
  2. *Propuesta de valor:* 1 oración sobre la solución.
  3. *Call to Action (CTA) de baja fricción:* "¿Vale la pena cruzarnos 5 min esta semana?".

### 3. Privacidad y Seguridad
- Nunca subir muestras de voz del usuario o clientes a servicios cloud no autorizados.
- Todos los archivos generados deben almacenarse localmente dentro del directorio de artefactos del proyecto.
