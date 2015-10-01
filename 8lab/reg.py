import re
print("a)")
word = "there"
string = "Hello there bob\nIt is a good day there\nThere is not here"
print(string,"\nEnd of Input")
for i in re.finditer(r"\b"+word+r"\b", string, re.I):
    print(i.group(), i.start())
print("b)")
string = "shorter than"
print("Input: ", string,"\n", re.findall("[^aeiou ]", string))
print("c)")
l = ['_hmm','9gag','terribly', 'improbable']
print(l,[i for i in l if re.match(r"[_\d]",i)!=None])

