ip = input()
result = ''
while ip != 'quit':
    ip = ip.split()
    for word in ip:
        if word[0].isalpha():
            for l in word:
                if l != 'z' and l!='Z':
                    result+=chr(ord(l)+1)
                else:
                    result+=chr(ord(l) - 25)
        elif word[0].isdigit():
            ml = list(word)
            ml.reverse()
            result+=''.join(ml)
        else:
            for i in range(0,len(word)-1,2):
                result+=word[i+1]+word[i]
            if len(word)%2!=0:
                result+=word[-1]
        result+=" "

    result+="\n"
    ip = input()
print (result)
