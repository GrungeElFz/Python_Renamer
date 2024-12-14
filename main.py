# Python_Audio.Renamer

import os
from pathlib import Path

# def chdir_home():
#     # Get the user's home directory
#     home_directory = Path.home()

#     # Construct the path to the Desktop
#     desktop_directory = home_directory / "Desktop"

#     try:
#         os.chdir(desktop_directory)
#         print(f"Successfully changed directory to: {os.getcwd()}")
#     except FileNotFoundError:
#         print("Error: The Desktop directory does not exist.")
#     except PermissionError:
#         print("Error: You do not have permission to access this directory.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


def list_items(directories, files):
    # Clear lists to ensure they're empty before use
    directories.clear()
    files.clear()

    # Iterate over items in the current directory
    for item in os.listdir():
        # Skip .DS_Store and .localized files
        if item in {".DS_Store", ".localized"}:
            continue

        # Resolve full path
        full_path = os.path.join(os.getcwd(), item)

        # Check if the item is a directory or file
        if os.path.isdir(full_path):
            directories.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    # Print all directories
    print("\nDirectories:")
    for directory in directories:
        print(f"  • {directory}")

    # Print all files
    print("\nFiles:")
    for file in files:
        print(f"  • {file}")


def count_items(directories, files):
    # Print the total count of directories and files
    print(f"\nTotal Directories: {len(directories)}")
    print(f"Total Files: {len(files)}")


# Change to Desktop directory
# chdir_home()

# Create lists to hold directories and files
directories = []
files = []

# List items and count them
list_items(directories, files)
count_items(directories, files)
