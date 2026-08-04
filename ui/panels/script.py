import gradio as gr

def create_script_panel():

    with gr.Group(elem_classes=["vf-panel"]):

        gr.Markdown("### Script")

        filename_box = gr.Textbox(
            label = "Filename",
            lines = 1
        )

        script_box = gr.Textbox(
            label = "Script",
            lines = 8
        )

        return{
             "filename": filename_box,
             "script": script_box
        }