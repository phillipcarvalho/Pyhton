a=input("Enter the first sentence: ")
b=input("Enter the first sentence: ")
str1=""
if(len(a)>len(b)):
   for i in a:
      for j in b:
         str1=str1+i+j
elif(len(a)<len(b)):
   for j in b:
      for i in a:
         str1=str1+j+i
else:
   for i in a:
      for j in b:
         str1=str1+i+j

print(str1)
