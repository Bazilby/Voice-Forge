from kokoro import KPipeline
import soundfile as sf
import gradio as gr
import time
import os
from characters import CHARACTERS
import json

with open("style.css", "r") as f:
    CSS =f.read()

with open("voices.json", "r") as f:
    VOICE_DATA =json.load(f)

pipeline = KPipeline(lang_code="a")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")

def generate(filename, text, character,  speed):

    character_data = CHARACTERS[character]

    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
    except OSError as e:
        raise gr.Error (f"Could not create Output folder: {e}")
    
    try:
        if not filename:
            filename = f"Output/kokoro_{int(time.time())}"

            filename = os.path.basename(filename)

        if not filename.endswith(".wav"):
            filename += ".wav"

        filepath = os.path.join(OUTPUT_DIR, filename)

        audio_chunks = []

        generator = pipeline(
            text, 
            voice=character_data["voice"],
            speed=character_data["speed"]
        )

        for _, _, audio in generator:
            audio_chunks.append(audio)
        
        import numpy as np
        final_audio = np.concatenate(audio_chunks)

        sf.write(
            filepath,
            final_audio,
            24000
        )

        return filepath
    
    except Exception as e:
        raise gr.Error(f"Generation failed: {e}")

def update_voice_info(character):

    character_data = CHARACTERS[character]
    voice_data = VOICE_DATA.get(character, {})

    return (
        character_data["gender"],
        str(voice_data.get("rating", "")),
        voice_data.get("notes")
    )

def save_voice_info(character, rating, notes):

    if character not in VOICE_DATA:
        VOICE_DATA[character] = {}

    VOICE_DATA[character]["rating"] = int(rating) if rating else 0
    VOICE_DATA[character]["notes"] = notes

    with open("voices.json", "w") as f:
        json.dump(
            VOICE_DATA,
            f,
            indent=4
        )

    return "Saved"






with gr.Blocks(css=CSS) as app:

    gr.Markdown("# Black Loom Voice Forge")

    with gr.Row():

        with gr.Column(scale=3):

            filename_box = gr.Textbox(
                lines=1,
                label="Filename",
                elem_id="filename-box"
            )

            script_box = gr.Textbox(
                lines=8,
                label="Script",
                elem_id="script-box"
            )

            speed_slider= gr.Slider(
                minimum=0,
                maximum=1.5,
                value=1.0,
                step=0.05,
                label="Speed",
                elem_id="speed-slider"
            )

            generate_btn = gr.Button(
                "Generate",
                elem_id="generate-btn",
                variant="primary"
            )

            audio_output = gr.Audio(
                label="Generated Audio",
                elem_id="audio-output"
            )
        
        with gr.Column(scale=1):

            voice_dropdown=gr.Dropdown(
                choices=list(CHARACTERS.keys()),
                value="Documentary Narrator",
                label="Voice",
                elem_id="voice-dropdown"
            )

            gender_box = gr.Textbox(
                label="Gender",
                interactive=False
            )

            rating_box = gr.Textbox(
                label="Rating",
                interactive=True
            )

            notes_box=gr.Textbox(
                label="Notes",
                lines=3,
                interactive=True
            )

            save_btn = gr.Button(
                "Save Voice Profile",
                variant="secondary"
            )

            save_status = gr.Textbox(
                label="Status",
                interactive=False
            )

   
    

    

    generate_btn.click(
        fn=generate,
        inputs=[
            filename_box,
            script_box,
            voice_dropdown,
            speed_slider
        ],
        outputs=audio_output
    )

    # on change of dropddown update these fields
    voice_dropdown.change(
        fn=update_voice_info,
        inputs=voice_dropdown,
        outputs=[
            gender_box,
            rating_box,
            notes_box
        ]
    )

    app.load(
        fn=update_voice_info,
        inputs=voice_dropdown,
        outputs=[
            gender_box,
            rating_box,
            notes_box
        ]
    )

    save_btn.click(
        fn=save_voice_info,
        inputs=[
            voice_dropdown,
            rating_box,
            notes_box
        ],
        outputs=save_status
    )


app.launch()