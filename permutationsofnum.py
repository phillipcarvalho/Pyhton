n=input("Enter a three digit number:")
l=[[i,j,k] for i in n for j in n for k in n if i!=j if i!=k if j!=k]
for i in l:
    print(''.join(i))

