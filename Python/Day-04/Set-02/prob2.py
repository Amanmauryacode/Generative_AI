numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n >500:
        break
    elif n>150:
        continue
    elif n%5==0:
        print(n)
