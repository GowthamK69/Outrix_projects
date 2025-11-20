import os
import shutil
from datetime import datetime

# =====================================================
# 🐐 GOAT LEVEL FILE ORGANIZER
# Author : Gowtham (Python Developer Intern)
# Features:
# - Auto categorization
# - Duplicate file protection
# - Dynamic folder creation
# - Logging system
# - Clean professional structure
# =====================================================


# ---------- CONFIG ----------
TARGET_FOLDER = r"C:\Users\mrgow\OneDrive\Desktop"


FILE_CATEGORIES = {
    "Images":  [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Programming": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Others": []
}


# ---------- UTILITY FUNCTIONS ----------
def log(message):
    """Logs events to both console and a log file."""
    log_file = os.path.join(TARGET_FOLDER, "organizer_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"[{timestamp}] {message}"

    # Print to terminal
    print(entry)

    # Write into log file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def create_folders():
    """Creates main category folders if not already present."""
    for folder in FILE_CATEGORIES.keys():
        path = os.path.join(TARGET_FOLDER, folder)
        os.makedirs(path, exist_ok=True)


def resolve_duplicate(destination_path):
    """Adds number to file if duplicate exists."""
    base, ext = os.path.splitext(destination_path)
    counter = 1

    while os.path.exists(destination_path):
        destination_path = f"{base} ({counter}){ext}"
        counter += 1
    
    return destination_path


def get_category(extension):
    """Finds the correct category based on file extension."""
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def move_file(file_name):
    """Moves a single file to its appropriate folder."""
    file_path = os.path.join(TARGET_FOLDER, file_name)
    ext = os.path.splitext(file_name)[1]

    # Skip system/hidden/log files
    if file_name in ("organizer_log.txt",) or file_name.startswith("."):
        return

    category = get_category(ext)

    destination_folder = os.path.join(TARGET_FOLDER, category)
    destination_path = os.path.join(destination_folder, file_name)

    # Prevent overwriting duplicates
    destination_path = resolve_duplicate(destination_path)

    shutil.move(file_path, destination_path)
    log(f"Moved: {file_name}  →  {category}")


# ---------- MAIN ----------
def organize_files():
    print("\n📁  STARTING GOAT FILE ORGANIZER...\n")

    if not os.path.exists(TARGET_FOLDER):
        print("❌ ERROR: Target folder does not exist.")
        return

    create_folders()

    for file_name in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file_name)

        if os.path.isfile(file_path):
            move_file(file_name)

    print("\n✅ DONE! Your folder is clean and perfectly organized.\n")
    print("📄 Log saved as: organizer_log.txt")


if __name__ == "__main__":
    organize_files()
