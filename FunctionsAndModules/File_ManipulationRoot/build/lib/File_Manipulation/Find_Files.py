import os
import fnmatch
import argparse
import platform  # Import platform to detect the operating system

def find_files(files_to_find, search_all_drives=False, check_this_disk=None):
    """
    Search for files on the computer based on the specified pattern.

    :param files_to_find: The file name or pattern to search for (e.g., "*.txt", "*HelloWorld*").
    :param search_all_drives: If True, searches all drives on the computer.
    :param check_this_disk: Specifies the disk or directory to search. Defaults to the system root.
    :return: List of found file paths.
    """
    found_files = []

    def search_directory(directory):
        """Helper function to search within a directory."""
        for root, dirs, files in os.walk(directory, topdown=True, onerror=None):
            for file in fnmatch.filter(files, files_to_find):
                found_files.append(os.path.join(root, file))

    try:
        if search_all_drives:
            print("Searching all drives...")
            if platform.system() == "Windows":
                # Windows drive letters A-Z
                for drive in [f"{chr(letter)}:\\" for letter in range(65, 91)]:
                    if os.path.exists(drive):
                        print(f"Searching in: {drive}")
                        search_directory(drive)
            else:
                # On Linux, search from the root directory
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
    parser = argparse.ArgumentParser(description="Search for files on the computer based on the specified pattern.")
    parser.add_argument("-FilesToFind", required=True, help="The file name or pattern to search for (e.g., '*.txt').")
    parser.add_argument("-SearchAllDrives", action="store_true", help="Search all drives on the computer.")
    parser.add_argument("-CheckThisDisk", default=None, help="Specify the disk or directory to search. Defaults to the system root.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with parsed arguments
    files = find_files(
        files_to_find=args.FilesToFind,
        search_all_drives=args.SearchAllDrives,
        check_this_disk=args.CheckThisDisk
    )

    # Print the results
    for file in files:
        print(file)
