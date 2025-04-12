import os
import fnmatch
import argparse
import platform

def get_filescount(files_to_find, search_all_drives=False, check_this_disk=None):
    """
    Count the number of files matching specific criteria.

    :param files_to_find: The file name or pattern to search for (e.g., "*.txt").
    :param search_all_drives: If True, searches all drives on the computer.
    :param check_this_disk: Specifies the disk or directory to search. Defaults to the system root.
    :return: Count of matching files.
    """
    file_count = 0

    def search_directory(directory):
        """Helper function to count files in a directory."""
        nonlocal file_count
        for root, dirs, files in os.walk(directory, topdown=True, onerror=None):
            file_count += len(fnmatch.filter(files, files_to_find))

    try:
        if search_all_drives:
            print("Counting files on all drives...")
            if platform.system() == "Windows":
                for drive in [f"{chr(letter)}:\\" for letter in range(65, 91)]:
                    if os.path.exists(drive):
                        print(f"Counting files in: {drive}")
                        search_directory(drive)
            else:
                print("Counting files from root directory '/'")
                search_directory("/")
        else:
            if not check_this_disk:
                check_this_disk = os.getenv("SystemDrive", "C:\\") if platform.system() == "Windows" else "/"
            print(f"Counting files in: {check_this_disk}")
            search_directory(check_this_disk)
    except Exception as e:
        print(f"An error occurred during the file count: {e}")

    print(f"Total files found: {file_count}")
    return file_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of files matching specific criteria.")
    parser.add_argument("-FilesToFind", required=True, help="The file name or pattern to search for (e.g., '*.txt').")
    parser.add_argument("-SearchAllDrives", action="store_true", help="Search all drives on the computer.")
    parser.add_argument("-CheckThisDisk", default=None, help="Specify the disk or directory to search. Defaults to the system root.")

    args = parser.parse_args()

    count = get_filescount(
        files_to_find=args.FilesToFind,
        search_all_drives=args.SearchAllDrives,
        check_this_disk=args.CheckThisDisk
    )

    print(f"Total files matching criteria: {count}")
