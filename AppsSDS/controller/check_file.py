

from pathlib import Path
import platform

my_file = Path("/home/binakarir/Projects/PySDS/run.py")
print (my_file)

print (platform.system())

if platform.system() == "Windows":
    if my_file.is_file():
        print ("file ada")

    else : 
        print ("file tidak ada")

