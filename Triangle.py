a=input()
b=ord(a)
for i in range(5):
     for j in range(i+1):
          print(chr(b),end=" ")
     b=b+1
     print()
