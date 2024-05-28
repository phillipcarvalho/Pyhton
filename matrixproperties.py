m=int(input(""))
n=int(input(""))
l=[]
l1=[]
for i in range(m):
    l1=list(map(int,(input("").split())))
    l.append(l1)
    l1=[]

max1=0
min1=(l[0])[0]
print("Matrix:")
for i in range(m):
    for j in range(n):
        print((l[i])[j],end=" ")
    
        if max1<(l[i])[j]:
            max1=(l[i])[j]
        if min1>(l[i])[j]:
            min1=(l[i])[j]
    print()   

print("\nMaximum value in the function:",max1)
print("Minimum value in the function:",min1)
print("\nTransposed Matrix:")
for i in range(m):
    for j in range(n):
        print((l[j])[i],end=" ")
    print()




