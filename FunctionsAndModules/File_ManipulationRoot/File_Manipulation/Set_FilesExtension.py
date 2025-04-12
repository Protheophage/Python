import os
import fnmatch
import argparse
import platform

def set_filesextension(files_to_find, new_extension, search_all_drives=False, check_this_disk=None):
    """
    Change the extension of files matching specific criteria.

    :param files_to_find: The file name or pattern to search for (e.g., "*.txt").
    :param new_extension: The new file extension to apply (e.g., ".log").
    :param search_all_drives: If True, searches all drives on the computer.
    :param check_this_disk: Specifies the disk or directory to search. Defaults to the system root.
    :return: Count of files whose extensions were changed.
    """
    changed_files_count = 0

    def search_and_rename(directory):
        """Helper function to search and rename files in a directory."""
        nonlocal changed_files_count
        for root, dirs, files in os.walk(directory, topdown=True, onerror=None):
            for file in fnmatch.filter(files, files_to_find):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.splitext(old_file_path)[0] + new_extension
                try:
                    os.rename(old_file_path, new_file_path)
                    changed_files_count += 1
                    print(f"Renamed: {old_file_path} -> {new_file_path}")
                except Exception as e:
                    print(f"Error renaming file {old_file_path}: {e}")

    try:
        if search_all_drives:
            print("Changing file extensions on all drives...")
            if platform.system() == "Windows":
                for drive in [f"{chr(letter)}:\\" for letter in range(65, 91)]:
                    if os.path.exists(drive):
                        print(f"Searching and renaming in: {drive}")
                        search_and_rename(drive)
            else:
                print("Searching and renaming from root directory '/'")
                search_and_rename("/")
        else:
            if not check_this_disk:
                check_this_disk = os.getenv("SystemDrive", "C:\\") if platform.system() == "Windows" else "/"
            print(f"Searching and renaming in: {check_this_disk}")
            search_and_rename(check_this_disk)
    except Exception as e:
        print(f"An error occurred during file renaming: {e}")

    print(f"Total files renamed: {changed_files_count}")
    return changed_files_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change the extension of files matching specific criteria.")
    parser.add_argument("-FilesToFind", required=True, help="The file name or pattern to search for (e.g., '*.txt').")
    parser.add_argument("-NewExtension", required=True, help="The new file extension to apply (e.g., '.log').")
    parser.add_argument("-SearchAllDrives", action="store_true", help="Search all drives on the computer.")
    parser.add_argument("-CheckThisDisk", default=None, help="Specify the disk or directory to search. Defaults to the system root.")

    args = parser.parse_args()

    count = set_filesextension(
        files_to_find=args.FilesToFind,
        new_extension=args.NewExtension,
        search_all_drives=args.SearchAllDrives,
        check_this_disk=args.CheckThisDisk
    )

    print(f"Total files renamed: {count}")
