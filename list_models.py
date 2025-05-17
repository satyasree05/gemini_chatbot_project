import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyDA654uiCITapRczZMt3lj0iVxQR5WyxqM")

# List available models
models = genai.list_models()

for model in models:
    print(f"Model name: {model.name}")
    print(f"Supports chat: {'generateContent' in model.supported_generation_methods}")
    print("-" * 40)
