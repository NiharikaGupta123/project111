import os
import shutil

from_dir="C:/Users/Niharika/Downloads"
to_dir="C:/Users/Niharika/Desktop/python/project111/pdf"
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    shutil.move(from_dir,to_dir)