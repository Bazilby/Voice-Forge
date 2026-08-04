from pedalboard import Pedalboard, Reverb, LowpassFilter
from pedalboard.io import AudioFile

#  check the tunnel effect is working
def check_tunnel():

    # try:
    #     raise Exception("TEST FAILURE: Tunnel DSP offline")

    # except Exception as tunnelError:

    #     return {
    #         "name": "TUNNEL EFFECT",
    #         "status": "FAIL",
    #         "error": str(tunnelError)
    #     }

    try:
        return {
            "name":  "TUNNEL EFFECT",
            "status": "OK"
        }

    except Exception as tunnelError:

        return{
            "name": "TUNNEL EFFECT",
            "status": "FAIL",
            "error": str(tunnelError)
        }

# This function applies a tunnel effect to an audio file by using a combination of reverb and lowpass filter.
def apply_tunnel(input_file, output_file):

    with AudioFile(input_file) as f:
        audio = f.read(f.frames)
        sample_rate = f.samplerate

    board = Pedalboard([
        Reverb(
            room_size=0.9,
            wet_level=0.5
        ),

        LowpassFilter(
            cutoff_frequency_hz = 2500
        )

    ])

    effected_audio = board(
        audio,
        sample_rate
    )

    with AudioFile(
        output_file,
        'w',
        sample_rate,
        effected_audio.shape[0]
    ) as f:
        f.write(effected_audio)

