# ==============================================================================
# INTELLIGENTIAL — TRANSCRIPCIÓN 100% LOCAL (FASTER-WHISPER, SIN SERVIDORES EXTERNOS)
# ==============================================================================
# Módulo de transcripción local de audio. Ni el audio ni la transcripción salen
# de la laptop en ningún momento.
#
# Instalación (una sola vez, con internet):
#   pip install faster-whisper --break-system-packages
#   (el modelo se descarga automáticamente la primera vez que corres el script;
#    después queda cacheado localmente en ~/.cache y ya no necesitas internet)
#
# MODEL_SIZE: "tiny" (más rápido/ligero) o "base" (más preciso, recomendado
# para jerga técnica como CNBV/PLD/SOFOM). Si notas que tu laptop se satura
# corriendo esto + Ollama al mismo tiempo durante 90 minutos, baja a "tiny".
# ==============================================================================
import numpy as np
from faster_whisper import WhisperModel

MODEL_SIZE = "base"
_model = None


def get_model():
    global _model
    if _model is None:
        print(f"🔒 Cargando modelo local Whisper ({MODEL_SIZE}) — 100% offline...")
        _model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")
        print("✔ Modelo local listo. Ningún audio saldrá de esta laptop.")
    return _model


def transcribe_local(audio_int16_array, language="es"):
    """Transcribe un array int16 (formato nativo de sounddevice) 100% en local."""
    model = get_model()
    audio_float = audio_int16_array.flatten().astype(np.float32) / 32768.0
    segments, _info = model.transcribe(
        audio_float, language=language, beam_size=1, vad_filter=True
    )
    return " ".join(seg.text.strip() for seg in segments).strip()
