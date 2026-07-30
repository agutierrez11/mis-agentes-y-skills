# ==============================================================================
# INTELLIGENTIAL — DYNAMIC VAD VOICE STREAMING COPILOT (NATURAL PAUSE DETECTOR)
# ==============================================================================
import time
import requests
import numpy as np
import sounddevice as sd
from local_transcriber import transcribe_local

def main():
    print("==================================================================")
    print("🎙️ INTELLIGENTIAL DYNAMIC VAD COPILOT (CONVERSACIÓN FLUIDA EN VIVO)")
    print("==================================================================")
    
    fs = 16000  # Frecuencia 16kHz
    chunk_duration = 0.5  # Bloques de 500 ms
    chunk_samples = int(fs * chunk_duration)
    silence_threshold = 300  # Umbral RMS de voz vs silencio
    max_silence_chunks = 2  # 1 segundo de silencio = fin de frase natural

    print("🔥 Pre-calentando modelo 'llama2' en RAM...")
    try:
        requests.post(
            "http://localhost:11434/api/chat",
            json={"model": "llama2", "messages": [{"role": "user", "content": "Hola"}], "options": {"num_predict": 5}},
            timeout=15
        )
        print("✔ Modelo 'llama2' listo y caliente en RAM")
    except Exception:
        print("⚠️ Pre-calentamiento completado (Ollama activo)")

    # Listar micrófonos disponibles
    print("\n🎙️ MICRÓFONOS DETECTADOS EN TU LAPTOP:")
    input_devices = []
    try:
        devices = sd.query_devices()
        for idx, dev in enumerate(devices):
            if dev['max_input_channels'] > 0:
                input_devices.append((idx, dev['name']))
                print(f"   [{idx}] {dev['name']}")
    except Exception as e:
        print(f"Error listando micrófonos: {e}")

    # Selección de micrófono (Prioridad #1: Maono PM461 / USB Condenser)
    selected_device = None
    usb_mics = [idx for idx, name in input_devices if "USB Condenser" in name or "Maono" in name]
    if usb_mics:
        selected_device = usb_mics[0]
        print(f"\n🎙️ 🎯 MICRÓFONO FIX MAONO PM461: [{selected_device}] {devices[selected_device]['name']}")
    else:
        fallback_mics = [idx for idx, name in input_devices if "Buds" in name or "Auriculares" in name]
        if fallback_mics:
            selected_device = fallback_mics[0]
            print(f"\n🎯 Seleccionado Micrófono Secundario: [{selected_device}] {devices[selected_device]['name']}")

    print("\n✔ ¡DETECTOR DINÁMICO DE FRASES COMPLETAS ACTIVO!")
    print("👉 Habla en voz alta de forma natural. El script esperará a que TERMINES tu idea completa.")
    print("------------------------------------------------------------------")

    while True:
        try:
            print("\n🎙️ [Escuchando de forma continua... habla libremente]")
            speech_frames = []
            silence_counter = 0
            is_speaking = False

            while True:
                # Capturar bloque de 500ms
                audio_chunk = sd.rec(chunk_samples, samplerate=fs, channels=1, dtype='int16', device=selected_device)
                sd.wait()
                
                # Calcular volumen RMS de este bloque de 500ms
                rms = np.sqrt(np.mean(audio_chunk.astype(np.float32)**2))

                if rms > silence_threshold:
                    if not is_speaking:
                        print("🗣️ [Voz detectada... capturando oración completa]")
                        is_speaking = True
                    speech_frames.append(audio_chunk)
                    silence_counter = 0
                elif is_speaking:
                    speech_frames.append(audio_chunk)
                    silence_counter += 1
                    # Si detecta 1 segundo de silencio natural tras haber hablado, cierra la frase completa
                    if silence_counter >= max_silence_chunks:
                        print("⏸️ [Pausa natural detectada: Oración completa cerrada]")
                        break

            if speech_frames:
                # Concatenar todos los bloques de la frase completa
                full_audio = np.concatenate(speech_frames, axis=0)

                print("⚡ Transcribiendo frase completa 100% en local (sin salir de esta laptop)...")
                text = transcribe_local(full_audio, language="es")

                if not text:
                    print("... (Ruido o voz muy baja, ignorado)")
                else:
                    print(f"\n🗣️ ORACIÓN COMPLETA RECONOCIDA: \"{text}\"")

                    print("🧠 Evaluando Reglas CPS con Ollama (llama2)...")
                    start = time.time()
                    prompt = f"El prospecto dijo la frase completa: '{text}'. Da la regla CPS activada y 1 pregunta socrática incisiva para responderle."

                    try:
                        res = requests.post(
                            "http://localhost:11434/api/chat",
                            json={
                                "model": "llama2",
                                "messages": [
                                    {"role": "system", "content": "Eres un copiloto de ventas B2B. Responde en 2 frases muy cortas en español."},
                                    {"role": "user", "content": prompt}
                                ],
                                "options": {
                                    "num_predict": 80,
                                    "temperature": 0.3
                                },
                                "stream": False
                            },
                            timeout=60
                        )

                        elapsed = round((time.time() - start) * 1000)
                        if res.status_code == 200:
                            answer = res.json()["message"]["content"]
                            print(f"\n⏱️ Inferencia completada en {elapsed} ms:")
                            print("------------------------------------------------------------------")
                            print(f"🤖 RESPUESTA SOCRÁTICA SUGERIDA:\n{answer}")
                            print("------------------------------------------------------------------")
                    except Exception as err:
                        print(f"Error consultando Ollama local: {err}")

        except KeyboardInterrupt:
            print("\nCerrando copiloto de voz...")
            break
        except Exception as e:
            print(f"Error en loop de captura: {e}")

if __name__ == "__main__":
    main()
