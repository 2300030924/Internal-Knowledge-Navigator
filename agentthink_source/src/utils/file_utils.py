import os
import fitz  # PyMuPDF
import pdfplumber

# -------------------------------
# Function 1: Read text files
# -------------------------------
def read_text_file(file_path: str) -> str:
    """Reads a .txt file and returns its content as a string."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text.strip()
    except Exception as e:
        print(f"[ERROR] Could not read text file {file_path}: {e}")
        return ""


# -------------------------------
# Function 2: Extract text from PDF
# -------------------------------
def read_pdf_file(file_path: str) -> str:
    """Extracts text from a PDF file using PyMuPDF (fitz) and pdfplumber fallback."""
    text = ""
    try:
        # Try PyMuPDF first (faster)
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text("text")
    except Exception as e:
        print(f"[WARN] PyMuPDF failed for {file_path}: {e}")
        try:
            # Fallback to pdfplumber
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        except Exception as e2:
            print(f"[ERROR] Could not read PDF file {file_path}: {e2}")
    return text.strip()


# -------------------------------
# Function 3: General file reader
# -------------------------------
def read_file(file_path: str) -> str:
    """Detects file type and reads text accordingly."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        return read_text_file(file_path)
    elif ext == ".pdf":
        return read_pdf_file(file_path)
    else:
        print(f"[WARN] Unsupported file type: {file_path}")
        return ""


# -------------------------------
# Function 4: Clean text
# -------------------------------
def clean_text(text: str) -> str:
    """Cleans up extracted text by removing extra whitespace, line breaks, etc."""
    text = text.replace("\n", " ").replace("\r", " ")
    text = " ".join(text.split())  # remove extra spaces
    return text.strip()


# -------------------------------
# Function 5: List all files in a folder
# -------------------------------
def list_files_in_folder(folder_path: str) -> list:
    """Returns a list of all PDF and TXT files in a folder (recursively)."""
    valid_files = []
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.lower().endswith((".txt", ".pdf")):
                valid_files.append(os.path.join(root, f))
    return valid_files


# -------------------------------
# Function 6: Quick test helper
# -------------------------------
# -------------------------------
# Function 6: Quick test helper
# -------------------------------
if __name__ == "__main__":
    # Use an absolute path instead of relative
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    folder = os.path.join(base_dir, "data")

    print(f"Looking in: {folder}")
    files = list_files_in_folder(folder)
    print(f"Found {len(files)} files:")
    for f in files:
        print("→", f)
        text = read_file(f)
        print("Preview:", text[:200], "\n")
