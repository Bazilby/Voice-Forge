from pedalboard import (Pedalboard, Compressor, Distortion, HighpassFilter, LowpassFilter)
from pedalboard.io import AudioFile

# check radio effect is working
def check_radio():
    try:
        return {
            "name":  "RADIO EFFECT",
            "status": "OK"
        }

    except Exception as radioError:

        return{
            "name": "REVERB EFFECT",
            "status": "FAIL",
            "error": str(radioError)
        }

# This function applies a radio effect to an audio file by using a combination of highpass and lowpass filters, as well as a compressor and distortion effect.
def apply_radio(input_file, output_file):

    with AudioFile(input_file) as f:
        audio = f.read(f.frames)
        sample_rate = f.samplerate

    board = Pedalboard([
        HighpassFilter(
            cutoff_frequency_hz = 300
        ),

        LowpassFilter(
            cutoff_frequency_hz = 3500
        ),

        Compressor(
            threshold_db = -20,
            ratio = 4.0
        ),

        Distortion(
            drive_db = 8
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

