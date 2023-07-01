str1 = "PyNaTive"

def fun(str1):
    s1 = ""
    s2 = ""
    for s in str1:
        if s.islower() :
            s1+=s
        else:
            s2+=s
    
    return s1+s2

print(fun(str1))