# https://www.geeksforgeeks.org/how-to-move-all-files-from-one-directory-to-another-using-python/
import os
import glob
import shutil

source = '/home/tuhingfg/Documents/source'
destination = '/home/tuhingfg/Documents/destination'
#
# gather all files
allfiles = glob.glob(os.path.join(source, '*_A_*'), recursive=True)
print("Files to move", allfiles)

# iterate on all files to move them to destination folder
for file_path in allfiles:
    dst_path = os.path.join(destination, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
    print(f"Moved {file_path} -> {dst_path}")