import os

def print_folder_structure(base_path, prefix=""):
    """
    Recursively prints the folder structure of a given path.
    """
    items = os.listdir(base_path)
    for i, item in enumerate(items):
        path = os.path.join(base_path, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            new_prefix = prefix + ("    " if i == len(items) - 1 else "│   ")
            print_folder_structure(path, new_prefix)


if __name__ == "__main__":
    base_folder = "data"
    print(f"\n📁 Folder structure for '{base_folder}':\n")
    print_folder_structure(base_folder)
