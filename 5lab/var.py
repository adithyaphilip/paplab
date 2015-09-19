import sys
f = open(sys.argv[1])
d = {}
for l in f:
    for w in l.split():
        if(w[0] not in d): d[w[0]]=[w]
        else: d[w[0]].append(w)
for k in sorted(d.keys()):
    print(k,len(d[k]),list(set(d[k])))
