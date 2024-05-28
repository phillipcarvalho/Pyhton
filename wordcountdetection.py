s1=input("Enter the word: ").upper()
s2=input("Enter the phrase: ").upper()
c=0
if(1<=len(s1)<=200):
    for i in range(len(s1)):
            if(s2==s1[i:i+len(s2):]):
                  c=c+1

print("Number of times", c)