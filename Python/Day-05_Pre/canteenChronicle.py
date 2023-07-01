inventory = {}

def add():
    try:
        id = int(input("Enter Snack Id : "))
    except ValueError as e:
        print("Invalid Id")
        return
    if id in inventory:
        print("Id is already used")
        return
    name = input("Enter Snack Name : ")
    while True:
        try:
            price = float(input("Enter Snack Price : "))
            break
        except ValueError as e:
            print("Invalid Price Value")
    Snack = {"Name":name,"Price":price,"availability":"Yes"}
    inventory[id] = Snack
    print("Successfully Added...")


def update():
    try:
        id = int(input("Enter Snack Id : "))
    except ValueError as e:
        print("Invalid Id")
        return
    try:
        availability = input("Enter Snack availability (Yes/No)")
        inventory[id]["availability"] = availability
        print(f"availability of {inventory[id]['Name']} is Successfully Updated...")
    except KeyError:
        print("Invalid Snack Id")

def remove():
    try:
        id = int(input("Enter Snack Id : "))
    except ValueError as e:
        print("Invalid Snack Id")
        return
    try:
        name = inventory[id]['Name']
        inventory.pop(id)
        print(f"{name} Successfully Removed...")
    except KeyError:
        print("Invalid Snack Id")


def record():
    try:
        id = int(input("Enter Snack Id : "))

    except ValueError as e:
        print("Invalid Snack Id")
        return
    if id not in inventory:
        print("Invalid Snack Id")
    elif id in inventory and inventory[id]["availability"] == "Yes":
        inventory[id]["availability"] = "No"
        name = inventory[id]["Name"]
        print(f"Successfully sold {name}...")
    else:
        name = inventory[id]["Name"]
        print(f"{name} is not available...")   


def main():

    while True:
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack")
        print("4. Record Snack")
        print("5. Exit")

        choice = input('Enter Your Choice ')

        if choice == '1':
            add()
        elif choice == '2':
            remove()
        elif choice == '3':
            update()
        elif choice == '4':
            record()
        elif choice == '5':
            break
        else:
            print("Please Enter Correct option")

main()