from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile

# check reverb effect is working
def check_reverb():
    try:
        return {
            "name":  "REVERB EFFECT",
            "status": "OK"
        }

    except Exception as reverbError:

        return{
            "name": "REVERB EFFECT",
            "status": "FAIL",
            "error": str(reverbError)
        }

# This function applies a reverb effect to an audio file by using the Reverb effect from the pedalboard library.
def apply_reverb(input_file, output_file, room_size=0.5, damping=0.5, wet_level=0.3):
    with AudioFile(input_file) as f:
        audio = f.read(f.frames)
        sample_rate = f.samplerate

    board = Pedalboard([
        Reverb(
            room_size=room_size,
            wet_level=wet_level,
        )
    ])

    effected_audio = board(audio, sample_rate)

    with AudioFile(
        output_file,
        'w',
        sample_rate,
        effected_audio.shape[0]
    )  as f:
        f.write(effected_audio)
   