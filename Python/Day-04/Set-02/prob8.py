employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dir = {}

for emp in  employees:
    dir[emp] = defaults

print(dir)