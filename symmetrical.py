a=input("Enter the word: ")
l=len(a)
l2=l//2
if(a[0:l2]==a[l2:]):
    print("Symmetrical")
else:
    print("Not")