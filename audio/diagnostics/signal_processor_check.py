from audio.effects.radio import check_radio
from audio.effects.reverb import check_reverb
from audio.effects.tunnel import check_tunnel
from audio.effects.eq import check_eq

def check_signal_processor():

    modules = [
        check_tunnel(),
        check_eq(),
        check_reverb(),
        check_radio()
    ]

    failed = [
        module for module in modules
        if module["status"] != "OK"
    ]

    if not failed:
        return {
            "name": "SIGNAL PROCESSOR",
            "status": "ALL OK"
        }

    return  {
        "name": "SIGNAL PROCESSOR",
        "status": "NOT  READY",
        "error": failed
    }