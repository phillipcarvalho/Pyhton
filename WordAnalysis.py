name=(input("Enter the word:"))
c=0
v=0
for i in name:
    i=i.capitalize()
    if(i=='A' or i=='E' or i=='O' or i=='U' or i=='I'):
        v=v+1
    else:
        c=c+1

print("Number of vowels: ",v)
print("Number of consonants: ",c)