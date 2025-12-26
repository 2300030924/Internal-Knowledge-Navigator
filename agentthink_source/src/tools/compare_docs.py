import os
import google.generativeai as genai
from src.utils.file_utils import read_file
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def compare_documents(file1: str, file2: str, model_name="gemini-2.5-flash"):
    """
    Compares two documents and lists their key differences.
    Args:
        file1 (str): Path to first document
        file2 (str): Path to second document
        model_name (str): Gemini model
    Returns:
        str: Comparison summary
    """
    text1 = read_file(file1)
    text2 = read_file(file2)

    model = genai.GenerativeModel(model_name)

    prompt = f"""
    Compare the following two documents and summarize the key differences:
    --- Document 1: ---
    {text1}
    --- Document 2: ---
    {text2}
    Focus on risk clauses, policies, and any critical wording differences.
    """

    response = model.generate_content(prompt)
    comparison = response.text.strip()

    print(f"\n⚖️ Comparison between {os.path.basename(file1)} and {os.path.basename(file2)}:\n")
    print(comparison)
    return comparison


# -------------------------------
# Quick test
# -------------------------------
if __name__ == "__main__":
    doc1 = "data/hr/employment_contract_v1.txt"
    doc2 = "data/hr/employment_contract_v2.txt"
    compare_documents(doc1, doc2)
