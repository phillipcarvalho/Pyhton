s=input("Enter the word: ")
l=list(map(str,input("Enter index and character separated by space: ").split()))
l1=[]
for i in s:
    l1.append(i)

if len(s)>int(l[0]):
    l1[int(l[0])]=l[1]

a=""
for i in l1:
    a=a+i

print(a)