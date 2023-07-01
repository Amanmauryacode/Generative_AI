def fibo(n):
    if n==1:
        return [0]
    if n==2 :
        return [0,1]
    if n==3 :
        return [0,1,1]
    
    list1 = [0,1,1]
    a =1
    b=1
    
    for i in range (3,n):
        list1.append(a+b)
        temp = a
        a = b
        b= temp+b
    
    return list1

s = input("Enter number  : ")
n = int(s)

print(fibo(n))