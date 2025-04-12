import os
import fnmatch
import argparse
import platform

def find_filesbycontent(string_to_find, file_type_to_search=".txt", search_all_drives=False, check_this_disk=None, max_file_size_kb=100):
    """
    Search for files containing specific content.

    :param string_to_find: The string to search for within the files.
    :param file_type_to_search: The file type to search (e.g., ".txt").
    :param search_all_drives: If True, searches all drives on the computer.
    :param check_this_disk: Specifies the disk or directory to search. Defaults to the system root.
    :param max_file_size_kb: Maximum file size (in KB) to include in the search.
    :return: List of file paths containing the specified content.
    """
    found_files = []

    def search_directory(directory):
        """Helper function to search within a directory."""
        for root, dirs, files in os.walk(directory, topdown=True, onerror=None):
            for file in fnmatch.filter(files, f"*{file_type_to_search}"):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) / 1024 <= max_file_size_kb:
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            if string_to_find in f.read():
                                found_files.append(file_path)
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")

    try:
        if search_all_drives:
            print("Searching all drives...")
            if platform.system() == "Windows":
                for drive in [f"{chr(letter)}:\\" for letter in range(65, 91)]:
                    if os.path.exists(drive):
                        print(f"Searching in: {drive}")
                        search_directory(drive)
            else:
                print("Searching from root directory '/'")
                search_directory("/")
        else:
            if not check_this_disk:
                check_this_disk = os.getenv("SystemDrive", "C:\\") if platform.system() == "Windows" else "/"
            print(f"Searching in: {check_this_disk}")
            search_directory(check_this_disk)
    except Exception as e:
        print(f"An error occurred during the file search: {e}")

    print(f"Total files found: {len(found_files)}")
    return found_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for files containing specific content.")
    parser.add_argument("-StringToFind", required=True, help="The string to search for within the files.")
    parser.add_argument("-FileTypeToSearch", default=".txt", help="The file type to search (e.g., '.txt').")
    parser.add_argument("-SearchAllDrives", action="store_true", help="Search all drives on the computer.")
    parser.add_argument("-CheckThisDisk", default=None, help="Specify the disk or directory to search. Defaults to the system root.")
    parser.add_argument("-MaxFileSizeToSearchInKB", type=int, default=100, help="Maximum file size (in KB) to include in the search.")

    args = parser.parse_args()

    files = find_filesbycontent(
        string_to_find=args.StringToFind,
        file_type_to_search=args.FileTypeToSearch,
        search_all_drives=args.SearchAllDrives,
        check_this_disk=args.CheckThisDisk,
        max_file_size_kb=args.MaxFileSizeToSearchInKB
    )

    for file in files:
        print(file)
