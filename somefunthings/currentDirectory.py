from pathlib import Path
import os

#This function show us our current position
path = Path.cwd()
print(path)

os.chdir('/home/miguelprogram/Desktop')
path = Path.cwd()
print(path)

#This funtion show us the directory home

pathHome = Path.home()
print(pathHome)

