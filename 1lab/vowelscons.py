ip = input()
v = 0
c = 0
for i in ip:
    if i in 'aeiou':
        v+=1
    elif i.isalpha(): c+=1
print ("Vowels:",v,"Consonants",c);
