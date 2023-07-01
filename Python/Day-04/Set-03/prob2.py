dic = {}

def Add(key,value):
    dic[key] = value
    print(dic)

def Update(key,value):
    dic[key] = value
    print(dic)

def Delete(key):
    dic.pop(key,"Unknown")
    print(dic)

Add("John",25)
Update("John",26)
Delete("John")