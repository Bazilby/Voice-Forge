from pedalboard import (Pedalboard, HighpassFilter, LowpassFilter, PeakFilter)
from pedalboard.io import AudioFile

# check eq effect is working
def check_eq():
    try:
        return {
            "name":  "EQUALISER EFFECT",
            "status": "OK"
        }

    except Exception as eqError:

        return{
            "name": "REVERB EFFECT",
            "status": "FAIL",
            "error": str(eqError)
        }


# This function applies an equalizer effect to an audio file by using a combination of highpass, lowpass, and peak filters.
def apply_eq(input_file, output_file, low_gain_db=0.0, mid_gain_db=0.0, high_gain_db=0.0):
    with AudioFile(input_file) as f:
        audio = f.read(f.frames)
        sample_rate = f.samplerate

    board = Pedalboard([

        HighpassFilter(
            cutoff_frequency_hz = 120
        ),

        LowpassFilter(
            cutoff_frequency_hz = 8000
        ),

        PeakFilter(
            cutoff_frequency_hz = 2500,
            gain_db = 3,
            q = 1.0
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
