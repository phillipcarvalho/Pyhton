def palindrome(x):
    a=x.lower()
    s=""
    for i in reversed(a):
        s=s+i

    if(s==a):
        return True
    else:
        return False

a=input("Enter the word: ")
print(palindrome(a))