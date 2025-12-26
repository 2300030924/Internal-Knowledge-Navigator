import re
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Import your tools
from src.tools.search_docs import search_docs
from src.tools.summarize import summarize_document
from src.tools.compare_docs import compare_documents
from src.tools.folder_structure import print_folder_structure

# ---------------------------------------------------------------------
# 🧠 Simple Intent Parser
# ---------------------------------------------------------------------
def detect_intent(query: str):
    query_lower = query.lower()
    if "compare" in query_lower:
        return "compare"
    elif "summarize" in query_lower:
        return "summarize"
    elif "show" in query_lower and "folder" in query_lower:
        return "folder"
    elif "search" in query_lower or "find" in query_lower or "look for" in query_lower:
        return "search"
    else:
        return "general"

# ---------------------------------------------------------------------
# 🎯 Core Agent Logic
# ---------------------------------------------------------------------
def handle_query(query: str):
    intent = detect_intent(query)
    print(f"\n🧭 Detected Intent: {intent.upper()}\n")

    if intent == "compare":
        # Detect document names (like contract_v1, contract_v2)
        docs = re.findall(r"contract[_\s]?(\d+)", query.lower())
        if len(docs) >= 2:
            file1 = f"data/hr/employment_contract_v{docs[0]}.txt"
            file2 = f"data/hr/employment_contract_v{docs[1]}.txt"
            if os.path.exists(file1) and os.path.exists(file2):
                return compare_documents(file1, file2)
            else:
                return f"⚠️ Could not find both documents ({file1}, {file2})."
        else:
            return "⚠️ Please specify two contract versions to compare."

    elif intent == "summarize":
        # Summarize all docs with a specific keyword
        search_results = search_docs(query)
        summaries = []
        for res in search_results:
            print(f"\n🧾 Summarizing: {res['file_path']}")
            summaries.append(summarize_document(res["file_path"]))
        return "\n\n".join(summaries)

    elif intent == "folder":
        print_folder_structure("data")
        return "✅ Folder structure displayed above."

    elif intent == "search":
        results = search_docs(query)
        if results:
            return f"✅ Found {len(results)} related document(s)."
        else:
            return "❌ No matching documents found."

    else:
        return "🤖 I'm not sure what you meant. Try asking to summarize, compare, or show folder structure."

# ---------------------------------------------------------------------
# 🚀 Entry Point
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("\n🧠 Internal Knowledge Navigator - MCP Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_query = input("🗣️  Enter your query: ")
        if user_query.lower() in ["exit", "quit"]:
            print("👋 Goodbye, Bhavya!")
            break

        response = handle_query(user_query)
        print("\n" + "=" * 80 + "\n")
