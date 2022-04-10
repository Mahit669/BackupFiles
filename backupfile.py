import os 
import shutil
source = input("Enter the source folder name")
destination = input("Enter the destination folder name")
source = source + "/"
destination = destination + "/"
listofiles = os.listdir(source)

for file in listofiles:
    shutil.copy((source+file),destination)