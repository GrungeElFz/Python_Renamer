# Python_Renamer

import os
from pathlib import Path

def chdir_home():
    # Get the user's home directory
    home_directory = Path.home()

    # Construct the path to the Desktop
    desktop_directory = home_directory / "Desktop"

    try:
        os.chdir(desktop_directory)
        print(f"Successfully changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print("Error: The Desktop directory does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

chdir_home()

# Iterate over files in the current directory
for file in os.listdir():
    # Skip .DS_Store and .localized files
    if file in {".DS_Store", ".localized"}:
        continue
    print(file)
    