# MVP: Code Prediction Engine using HuggingFace Transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class CodePredictor:
    def __init__(self, model_name="microsoft/CodeGPT-small-py"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.eval()

    def predict_next_token(self, code_snippet, max_new_tokens=1):
        inputs = self.tokenizer(code_snippet, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False
            )
        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated[len(code_snippet):]

if __name__ == "__main__":
    predictor = CodePredictor()
    code = input("Enter partial Python code: ")
    next_token = predictor.predict_next_token(code)
    print(f"Predicted next token: {next_token}")

