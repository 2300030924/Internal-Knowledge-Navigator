

import os
import google.generativeai as genai
from src.utils.file_utils import read_file

# Load Gemini API key
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_document(file_path: str, model_name="gemini-2.5-flash"):
    """
    Summarizes the content of a given document using the Gemini API.
    Args:
        file_path (str): Path to the document (txt/pdf)
        model_name (str): Gemini model name
    Returns:
        str: Summarized text
    """
    model = genai.GenerativeModel(model_name)

    text = read_file(file_path)
    if not text.strip():
        return f"[⚠️ Empty file: {file_path}]"

    prompt = f"Summarize this document in 5 concise bullet points:\n\n{text}"
    response = model.generate_content(prompt)
    summary = response.text.strip()

    print(f"\n📄 Summary for {os.path.basename(file_path)}:\n")
    print(summary)
    return summary


# -------------------------------
# Quick test
# -------------------------------
if __name__ == "__main__":
    test_file = "data/hr/employment_contract_v2.txt"
    summarize_document(test_file)
