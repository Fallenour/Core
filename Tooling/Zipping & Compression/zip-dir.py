# Source: https://realpython.com/python-zipfile/
import pathlib
import zipfile

directory = pathlib.Path("root_dir/")

with zipfile.ZipFile("directory_tree.zip", mode="w") as archive:
    for file_path in directory.rglob("*"):
        archive.write(
            file_path,
            arcname=file_path.relative_to(directory)
        )


with zipfile.ZipFile("directory_tree.zip", mode="r") as archive:
    archive.printdir()