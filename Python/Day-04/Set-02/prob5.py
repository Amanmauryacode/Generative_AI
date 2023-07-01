list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range (0,max(len(list1),len(list2))):
    if(i < len(list1) and len(list2)):
        list3.append(list1[i]+list2[i])
    elif i < len(list1) :
        list3.append(list1[i])
    elif i < len(list2) :
        list3.append(list2[i])

print(list3)