import shutil
import os

file_source = './Split_CustomData/val/images/'
file_destination = './Split_CustomData/val/'
 
get_files = os.listdir(file_source)
 
for g in get_files:
    if g.split('.')[-1] == 'png':
        try:
            shutil.move(file_source + g, file_destination)
        except:
            pass
