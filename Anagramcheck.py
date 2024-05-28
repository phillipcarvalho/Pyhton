s=input("Enter first word: ")
s1=input("Enter second word: ")
l=[i for i in s if 65<=ord(i)<=90 or 97<=ord(i)<=122]
l1=[i for i in s1 if 65<=ord(i)<=90 or 97<=ord(i)<=122]
a=""
a1=""
for i in l:
    a=a+i
for i in l1:
    a1=a1+i

if(sorted(a)==sorted(a1)):
    print("Yes")
else:
    print("No")

