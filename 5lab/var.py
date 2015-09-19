import sys
f = open(sys.argv[1])
d = {}
for l in f:
    for w in l.split():
        if(w[0] not in d): d[w[0]]=[w]
        else: d[w[0]].append(w)
f = open("output","w")
for k in sorted(d.keys()):
    f.write(" ".join((k,str(len(d[k])),str(list(set(d[k])))))+"\n")
f.close()
