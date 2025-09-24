# Gradio or Streamlit app for web interface

# MVP: Simple Gradio Web UI for Code Prediction
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gradio as gr
from model.predict import CodePredictor

predictor = CodePredictor()

def predict_next_token_ui(code):
    return predictor.predict_next_token(code)

def main():
    iface = gr.Interface(
        fn=predict_next_token_ui,
        inputs=gr.Textbox(lines=5, label="Partial Python Code"),
        outputs=gr.Textbox(label="Predicted Next Token"),
        title="Code Next Token Predictor",
        description="Enter partial Python code. Get the next token prediction."
    )
    iface.launch()

if __name__ == "__main__":
    main()

