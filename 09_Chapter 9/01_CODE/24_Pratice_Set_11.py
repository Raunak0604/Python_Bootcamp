import os

oldname = "25_Rename.txt"
newname = "25_Renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)