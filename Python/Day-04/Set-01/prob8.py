def fact(num):
    if(num==0 or num==1):
        return 1
    return num*fact(num-1)

s = input("Enter number : ")
num = int(s)
print(f"factorinal of {num} is : ",fact(num))