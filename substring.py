s=input("Enter a word: ")
l=[s[i:j:] for i in range(len(s)) for j in range(len(s)+1)  if i<j]
l.sort()
for i in l:
    print(i)