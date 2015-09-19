import sys
f = open(sys.argv[1])
a = f.readlines()
print("Total entries:",len(a),"\nEntries with /bin/bash as login shell: ",len(list(filter(lambda x: x.split(":")[-1].strip()=='/bin/bash', a))))
