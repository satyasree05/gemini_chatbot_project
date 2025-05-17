import time
import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
import re

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
print("Loaded API key:", GOOGLE_API_KEY)

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
chat = model.start_chat()

print("* Gemini Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        print("⚠️ Please enter a message.")
        continue

    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)

    except ResourceExhausted as e:
        # Parse retry delay from error message (fallback 60 seconds)
        retry_seconds = 60
        msg = str(e)
        match = re.search(r'retry_delay {\s*seconds: (\d+)', msg)
        if match:
            retry_seconds = int(match.group(1))
        print(f"⚠️ Quota exceeded. Waiting {retry_seconds} seconds before retrying...")
        time.sleep(retry_seconds)

    except Exception as e:
        print("Error:", e)
