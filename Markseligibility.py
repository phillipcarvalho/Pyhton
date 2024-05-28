name=input("Enter the name:")
pmarks=int(input("Enter the Physics marks:"))


if(pmarks==0):
    print("Enter valid value")
    pmarks=int(input("Enter the Physics marks:"))

mmarks=int(input("Enter the math marks:"))

if(mmarks==0):
    print("Enter valid value")
    mmarks=int(input("Enter the Math marks:"))

cmarks=int(input("Enter the Chemistry marks:"))

if(cmarks==0):
    print("Enter valid value")
    cmarks=int(input("Enter the Chemistry marks:"))

sum=pmarks+mmarks+cmarks
avg=float(sum/3)
print(f"{avg:.2f}")

if(avg<98):
    print("Not-Eligible")
else:
    print("Eligible")

