n=int(input("Enter the number of terms in the series"))
l=[0,1]

for i in range(2,n):
    a=l[i-1]+l[i-2]
    l.append(a)

print(l)