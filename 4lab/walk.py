import os
dirs = 0
files = 0
for i in os.walk("."):
    print("Current:", i[0])
    print("Dirs:", i[1])
    print("Files:", i[2])
    print("-"*100)
    dirs+=len(i[1])
    files+=len(i[2])
print("Directories:", dirs, "Files", files)

