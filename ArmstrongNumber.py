num=""

def armstrongcheck(num):
    sum=0
    l=len(num)
    for i in range(l):
        sum=int(num[i])**l +sum
    if int(num)==sum:
     print(num)
     
a=int(input("Enter the starting point:"))
b=int(input("Enter the end point:"))

for i in range(a,b+1):
    x=str(i)
    armstrongcheck(x)

    