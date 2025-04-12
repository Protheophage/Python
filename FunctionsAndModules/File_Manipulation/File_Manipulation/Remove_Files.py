import os
import fnmatch
import argparse
import platform

def remove_files(files_to_delete, search_all_drives=False, check_this_disk=None):
    """
    Remove files matching specific criteria.

    :param files_to_delete: The file name or pattern to delete (e.g., "*.tmp").
    :param search_all_drives: If True, searches all drives on the computer.
    :param check_this_disk: Specifies the disk or directory to search. Defaults to the system root.
    :return: Count of deleted files.
    """
    deleted_files_count = 0

    def search_and_delete(directory):
        """Helper function to search and delete files in a directory."""
        nonlocal deleted_files_count
        for root, dirs, files in os.walk(directory, topdown=True, onerror=None):
            for file in fnmatch.filter(files, files_to_delete):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_files_count += 1
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

    try:
        if search_all_drives:
            print("Removing files on all drives...")
            if platform.system() == "Windows":
                for drive in [f"{chr(letter)}:\\" for letter in range(65, 91)]:
                    if os.path.exists(drive):
                        print(f"Searching and deleting in: {drive}")
                        search_and_delete(drive)
            else:
                print("Searching and deleting from root directory '/'")
                search_and_delete("/")
        else:
            if not check_this_disk:
                check_this_disk = os.getenv("SystemDrive", "C:\\") if platform.system() == "Windows" else "/"
            print(f"Searching and deleting in: {check_this_disk}")
            search_and_delete(check_this_disk)
    except Exception as e:
        print(f"An error occurred during file deletion: {e}")

    print(f"Total files deleted: {deleted_files_count}")
    return deleted_files_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove files matching specific criteria.")
    parser.add_argument("-FilesToDelete", required=True, help="The file name or pattern to delete (e.g., '*.tmp').")
    parser.add_argument("-SearchAllDrives", action="store_true", help="Search all drives on the computer.")
    parser.add_argument("-CheckThisDisk", default=None, help="Specify the disk or directory to search. Defaults to the system root.")

    args = parser.parse_args()

    count = remove_files(
        files_to_delete=args.FilesToDelete,
        search_all_drives=args.SearchAllDrives,
        check_this_disk=args.CheckThisDisk
    )

    print(f"Total files deleted: {count}")
