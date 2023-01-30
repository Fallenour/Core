# Source: https://realpython.com/python-zipfile/
import zipfile

with zipfile.ZipFile("sample.zip", mode="r") as archive:
    for file in archive.namelist():
        if file.endswith(".md"):
            archive.extract(file, "output_dir/")