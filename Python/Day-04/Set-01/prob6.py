def vovel(str1):
    count =0
    vovels = ['a','e','i','o','u']
    for s in str1:
        if s.lower() in vovels:
            count+=1

    return count

str1 = input("Enter any string : ")
print("Number of vovels : ",vovel(str1))