# File_Manipulation Package

## SYNOPSIS

The `File_Manipulation` package provides a set of tools for performing various file operations, such as searching, deleting, counting, and modifying files. It is designed to work across multiple platforms and can be used programmatically or via the command line.

## DESCRIPTION

The package includes the following modules:

- **Find_Files**: Search for files based on patterns.
- **Remove_Files**: Delete files matching specific criteria.
- **Get_FilesCount**: Count files matching specific patterns.
- **Find_FilesByContent**: Search for files containing specific content.
- **Set_FilesExtension**: Change the extensions of files.

Each module provides a specific functionality and can be used independently or as part of the package.

---

## MODULES

### 1. Find_Files

#### Description
Search for files based on a specified pattern (e.g., `*.txt`, `*report*`).

#### Parameters
- `files_to_find` (str): The file name or pattern to search for (e.g., `*.txt`).
- `search_all_drives` (bool): If `True`, searches all drives on the computer.
- `check_this_disk` (str, optional): Specifies the disk or directory to search. Defaults to the system root.

#### Usage Examples
**Shell:**
```bash
find_files "*.txt" --search-all-drives
```

**Python:**
```python
from File_Manipulation import find_files
files = find_files("*.txt", search_all_drives=True)
print(files)
```

---

### 2. Remove_Files

#### Description
Delete files matching a specific pattern (e.g., `*.tmp`).

#### Parameters
- `files_to_delete` (str): The file name or pattern to delete (e.g., `*.tmp`).
- `search_all_drives` (bool): If `True`, searches all drives on the computer.
- `check_this_disk` (str, optional): Specifies the disk or directory to search. Defaults to the system root.

#### Usage Examples
**Shell:**
```bash
remove_files "*.tmp" --check-this-disk "C:\\"
```

**Python:**
```python
from File_Manipulation import remove_files
deleted_count = remove_files("*.tmp", check_this_disk="C:\\")
print(f"Deleted {deleted_count} files.")
```

---

### 3. Get_FilesCount

#### Description
Count the number of files matching a specific pattern (e.g., `*.log`).

#### Parameters
- `files_to_find` (str): The file name or pattern to search for (e.g., `*.log`).
- `search_all_drives` (bool): If `True`, searches all drives on the computer.
- `check_this_disk` (str, optional): Specifies the disk or directory to search. Defaults to the system root.

#### Usage Examples
**Shell:**
```bash
get_filescount "*.log" --search-all-drives
```

**Python:**
```python
from File_Manipulation import get_filescount
count = get_filescount("*.log", search_all_drives=True)
print(f"Found {count} log files.")
```

---

### 4. Find_FilesByContent

#### Description
Search for files containing specific content (e.g., files containing the word "error").

#### Parameters
- `string_to_find` (str): The string to search for within the files.
- `file_type_to_search` (str, optional): The file type to search (e.g., `.txt`). Defaults to `.txt`.
- `search_all_drives` (bool): If `True`, searches all drives on the computer.
- `check_this_disk` (str, optional): Specifies the disk or directory to search. Defaults to the system root.
- `max_file_size_kb` (int, optional): Maximum file size (in KB) to include in the search. Defaults to 100 KB.

#### Usage Examples
**Shell:**
```bash
find_filesbycontent "error" --file-type-to-search ".log" --max-file-size-to-search-in-kb 500
```

**Python:**
```python
from File_Manipulation import find_filesbycontent
files = find_filesbycontent("error", file_type_to_search=".log", max_file_size_kb=500)
print(files)
```

---

### 5. Set_FilesExtension

#### Description
Change the extensions of files matching a specific pattern (e.g., rename `*.txt` files to `*.bak`).

#### Parameters
- `files_to_find` (str): The file name or pattern to search for (e.g., `*.txt`).
- `new_extension` (str): The new file extension to apply (e.g., `.bak`).
- `search_all_drives` (bool): If `True`, searches all drives on the computer.
- `check_this_disk` (str, optional): Specifies the disk or directory to search. Defaults to the system root.

#### Usage Examples
**Shell:**
```bash
set_filesextension "*.txt" ".bak" --check-this-disk "D:\\"
```

**Python:**
```python
from File_Manipulation import set_filesextension
renamed_count = set_filesextension("*.txt", ".bak", check_this_disk="D:\\")
print(f"Renamed {renamed_count} files.")
```

---

## INSTALLATION

To use this package, install it using `pip` after cloning the repository:

```bash
pip install .
```

---

## LICENSE

This project is licensed under the **GNU General Public License v3 (GPLv3)**. See the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for details.

---

## AUTHOR

Developed by **Protheophage**  
Email: [protheophage@gmail.com](mailto:protheophage@gmail.com)