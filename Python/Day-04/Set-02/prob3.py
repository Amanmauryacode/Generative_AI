s1 = "Ault"
s2 = "Kelly"

def joinMid(s1,s2):
    mid = len(s1)//2
    
    return s1[:mid]+s2+s1[mid:]
print(joinMid(s1,s2))