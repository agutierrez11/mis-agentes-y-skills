# ==============================================================================
# INTELLIGENTIAL — 60-SECOND ROLLING WINDOW AUDIO COPILOT (NEAR REAL-TIME)
# ==============================================================================
import time
import requests
import numpy as np
import sounddevice as sd
from local_transcriber import transcribe_local

def main():
    print("==================================================================")
    print("🎙️ INTELLIGENTIAL 60-SEC ROLLING WINDOW COPILOT (NEAR REAL-TIME)")
    print("==================================================================")
    
    fs = 16000  # Frecuencia 16kHz
    window_duration = 30  # Ventana rodante de 30 a 60 segundos para bloque de párrafo

    print("🔥 Pre-calentando modelo 'llama2' en la RAM...")
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
        print(f"\n🎙️ 🎯 MICRÓFONO MAONO PM461 FIJADO: [{selected_device}] {devices[selected_device]['name']}")
    else:
        fallback_mics = [idx for idx, name in input_devices if "Buds" in name or "Auriculares" in name]
        if fallback_mics:
            selected_device = fallback_mics[0]
            print(f"\n🎯 Seleccionado Micrófono Secundario: [{selected_device}] {devices[selected_device]['name']}")

    print(f"\n✔ ¡MODO VENTANA RODANTE NEAR REAL-TIME ({window_duration} SEC) ACTIVO!")
    print(f"👉 Captura bloques completos de {window_duration}s para análisis de contexto profundo.")
    print("------------------------------------------------------------------")

    block_count = 1

    while True:
        try:
            print(f"\n🎙️ [Capturando Bloque #{block_count} ({window_duration} segundos de conversación)... habla naturalmente]")
            recording = sd.rec(int(window_duration * fs), samplerate=fs, channels=1, dtype='int16', device=selected_device)
            sd.wait()  # Captura bloque completo de 30-60s

            print(f"⚡ Transcribiendo Bloque #{block_count} 100% en local (sin salir de esta laptop)...")
            text = transcribe_local(recording, language="es")

            if not text:
                print(f"... (Sin voz clara detectada en el Bloque #{block_count}, continuando captura)")
            else:
                print(f"\n🗣️ PARRAFO TRANSCRITO DE BLOQUE #{block_count}:\n\"{text}\"")

                print("\n🧠 Evaluando Reglas CPS y Atractores con Ollama (llama2)...")
                start = time.time()
                prompt = f"El prospecto dijo el siguiente bloque de conversación: '{text}'. Identifica la regla CPS activada, el atractor de resistencia y 1 pregunta socrática incisiva para responderle en la reunión."

                try:
                    res = requests.post(
                        "http://localhost:11434/api/chat",
                        json={
                            "model": "llama2",
                            "messages": [
                                {"role": "system", "content": "Eres un copiloto de ventas B2B para SOFOMes. Responde en 2 a 3 frases estructuradas en español."},
                                {"role": "user", "content": prompt}
                            ],
                            "options": {
                                "num_predict": 120,
                                "temperature": 0.3
                            },
                            "stream": False
                        },
                        timeout=60
                    )

                    elapsed = round((time.time() - start) * 1000)
                    if res.status_code == 200:
                        answer = res.json()["message"]["content"]
                        print(f"\n⏱️ Inferencia de Bloque #{block_count} completada en {elapsed} ms:")
                        print("==================================================================")
                        print(f"🤖 ESTRATEGIA Y PREGUNTA SOCRÁTICA SUGERIDA:\n{answer}")
                        print("==================================================================")
                except Exception as err:
                    print(f"Error consultando Ollama local: {err}")

            block_count += 1

        except KeyboardInterrupt:
            print("\nCerrando copiloto de ventana rodante...")
            break
        except Exception as e:
            print(f"Error en loop de ventana rodante: {e}")

if __name__ == "__main__":
    main()
