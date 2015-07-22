import shutil
import os
import glob
import PIL

userFile = raw_input("paste your source directory:")
outputDir = raw_input("paste your desired output directory:")

if userFile.index('"') >= 0:  
	folder = os.walk(userFile.replace('"',''))
else:
	folder = os.walk(userFile)

for folders in folder:
	for images in os.walk(folders[0]):
		print images[1:]