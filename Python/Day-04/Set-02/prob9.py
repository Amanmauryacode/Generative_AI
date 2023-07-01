sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dir = {}
for k in keys :
    dir[k] = sample_dict[k]
print(dir)