from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from audio.engines.kokoro_engine import check_kokoro
from  audio.effects.tunnel import  check_tunnel
from audio.effects.reverb import check_reverb
from audio.effects.eq import check_eq
from audio.effects.radio  import check_radio
from audio.diagnostics.signal_processor_check import check_signal_processor

app =  FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def get_status():

    return {
        "system": "BLACK LOOM VOICE FORGE MK.I",
        "checks": [
            check_kokoro(),
            check_tunnel(),
            check_reverb(),
            check_eq(),
            check_radio(),
            check_signal_processor()
        ]
    }