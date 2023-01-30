# Source: https://realpython.com/python-zipfile/
'''
Creating ZIP files sequentially can be another common requirement in your day-to-day programming.
For example, you may need to create an initial ZIP file with or without content and then append
new member files as soon as they become available. In this situation, you need to open and
close the target ZIP file multiple times.

To solve this problem, you can use ZipFile in append mode ("a"), as you have already done.
This mode allows you to safely append new member files to a ZIP archive without truncating its current content:
'''
import zipfile

def append_member(zip_file, member):
    with zipfile.ZipFile(zip_file, mode="a") as archive:
        archive.write(member)

def get_file_from_stream():
    """Simulate a stream of files."""
    for file in ["hello.txt", "lorem.md", "realpython.md"]:
        yield file

for filename in get_file_from_stream():
    append_member("incremental.zip", filename)

with zipfile.ZipFile("incremental.zip", mode="r") as archive:
    archive.printdir()