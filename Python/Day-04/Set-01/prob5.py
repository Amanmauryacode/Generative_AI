def reverseStr(string):
    str= ""
    for s in string:
        str= s+str
    return str

str1 = input("Enter your String: ")

print(str1)
print(reverseStr(str1))