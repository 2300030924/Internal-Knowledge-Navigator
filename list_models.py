import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Fetch all available models
models = genai.list_models()

print("✅ Available Gemini Models:\n")
for m in models:
    print(f"- {m.name}")
