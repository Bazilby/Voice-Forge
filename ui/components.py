import gradio as gr

def panel(title, content):
    with gr.Group(elem_classes=["vf-panel"]):
        gr.Markdown(f"### {title}")

        content()