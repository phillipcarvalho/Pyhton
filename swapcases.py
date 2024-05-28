a=input("")
a1=""
for i in a:
    if(65<=ord(i)<=90):
        a1=a1+i.lower()
    elif(97<=ord(i)<=122):
        a1=a1+i.upper()
    else:
        a1=a1+i

print(a1)