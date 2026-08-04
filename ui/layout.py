import gradio as gr

from ui.components import panel
from ui.panels.script import create_script_panel

CSS = """
"""

def create_ui():

    with gr.Blocks(css=CSS) as app:

        gr.Markdown("# Black Loom Voice Forge")

        with gr.Row():

            with gr.Column():

                script_components = create_script_panel()

            with gr.Column():

                panel("Voice", lambda: None)

            with gr.Column():

                panel("Effects", lambda: None)

            with gr.Column():

                panel("Preview", lambda: None)

    return app