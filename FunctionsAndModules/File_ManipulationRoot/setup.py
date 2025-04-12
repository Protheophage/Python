from setuptools import setup, find_packages

setup(
    name="File_Manipulation",
    version="1.0.0",
    description="A package for performing various file operations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Protheophage",
    author_email="protheophage@gmail.com",
    url="https://github.com/Protheophage/Python/tree/main/FunctionsAndModules/File_Manipulation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "find_files=File_Manipulation.Find_Files:find_files",
            "remove_files=File_Manipulation.Remove_Files:remove_files",
            "get_filescount=File_Manipulation.Get_FilesCount:get_filescount",
            "find_filesbycontent=File_Manipulation.Find_FilesByContent:find_filesbycontent",
            "set_filesextension=File_Manipulation.Set_FilesExtension:set_filesextension",
        ]
    },
)