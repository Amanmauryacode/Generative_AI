string = input("Enter the list : ")
string2 = string.split(" ")
list1 = [int(num) for num in string2]

sum = 0
for i in list1:
    sum+=i

print("Sum : ",sum)
print("Average : ",sum/len(list1))
