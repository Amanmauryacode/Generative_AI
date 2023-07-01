def isPrime(num):
    if num <=1:
        return False
    
    for i in range(2,int(num**0.5) +1):
        if num%i==0:
            return False
    
    return True

str1 = input("Enter any Number : ")
num = int(str1)
print("Is Prime : ", isPrime(num))