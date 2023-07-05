import json
from tabulate import tabulate
from colorama import Fore, Style

def readData():
    with open("Day-05.py\db.json", "r") as file:
        data = json.load(file)
    return data

def writeData(existing_data):
    with open("Day-05.py\db.json", "w") as file:
        json.dump(existing_data, file)

def View_Dish_List():
    data = readData()
    
    table_data = [[item.get("id", ""),item.get("name", ""), item.get('price', ''), item.get("availability", "")] for item in data["Dish"]]

    for row in table_data:
        available = row[3]
        
        if available == "Yes":
            row[3] = f"\033[32m{available}\033[0m"
        else :
            row[3] = f"\033[31m{available}\033[0m"

    # Display the table
    headers = ["Id", "Name","Price","Availability"]
    table = tabulate(table_data, headers, tablefmt="grid")
    print(table)


def Add_Dish_To_Menu():
    
    existing_data = readData()

    newDish = {
        "id" : len(existing_data["Dish"])+1,
        "name" : input(Fore.LIGHTYELLOW_EX+"Enter dish name : "+Style.RESET_ALL),
        "price" : "$"+input(Fore.LIGHTYELLOW_EX+"Enter dish price : "+Style.RESET_ALL),
        "availability" : input(Fore.LIGHTYELLOW_EX+"Enter dish availability(Yes/No) : "+Style.RESET_ALL)
    }

    existing_data["Dish"].append(newDish)

    # Write the modified Python object back to the JSON file
    writeData(existing_data)
    print()
    print(Fore.GREEN+"Dish Successfully Added..."+Style.RESET_ALL)
    print()

def Remove_Dish_From_List():
    try:
        id = int(input(Fore.LIGHTYELLOW_EX+"Enter dish id : "+Style.RESET_ALL))
        existing_data = readData()
        data = existing_data["Dish"][id-1]
        existing_data["Dish"].remove(data)
        for row in range(0,len(existing_data["Dish"])):
            existing_data["Dish"][row]["id"] = row+1
        writeData(existing_data)
        print()
        print(Fore.GREEN+"Dish Successfully Removed..."+Style.RESET_ALL)
        print()
    except ValueError:
        print(Fore.RED+"Please enter valid id "+Style.RESET_ALL)
    
def Update_Availability():
    try:
        id = int(input(Fore.LIGHTYELLOW_EX+"Enter dish id : "+Style.RESET_ALL))
        existing_data = readData()
        existing_data["Dish"][id-1]["availability"] = input(Fore.LIGHTYELLOW_EX+"Enter dish availability(Yes/No) : "+Style.RESET_ALL)
        writeData(existing_data)
        print()
        print(Fore.GREEN+"Dish Availability Successfully Updated..."+Style.RESET_ALL)
        print()
    except ValueError:
        print(Fore.RED+"Please enter valid id "+Style.RESET_ALL)

def New_Order():
    try :
        existing_data = readData()
        name = input(Fore.LIGHTYELLOW_EX+"Enter customer name : "+Style.RESET_ALL)
        dishId = input(Fore.LIGHTYELLOW_EX+"Enter a list of numbers, separated by spaces: "+Style.RESET_ALL)

        dish_list = list(map(int, dishId.split()))
        
        items = []
        totalBill = 0
        for row in dish_list:
            if existing_data["Dish"][row-1]["availability"]== "No":
                print()
                print(Fore.RED+existing_data["Dish"][row-1]["name"]+" is not availability..."+Style.RESET_ALL)
                print()
                return
            items.append(existing_data["Dish"][row-1]["name"])
            
            totalBill += int(existing_data["Dish"][row-1]["price"][1:])
        
        newOrder = {
            "id" : len(existing_data["Orders"])+1,
            "name" : name,
            "items" : items,
            "total_bill": "$"+str(totalBill),
            "status": "Preparing"
        }
        existing_data["Orders"].append(newOrder)
        writeData(existing_data)
        print()
        print(Fore.GREEN+"Successfully Ordered..."+Style.RESET_ALL)
        print()
        
    except:
        print(Fore.RED+"Invalid Input"+Style.RESET_ALL)

def Update_Order_Status():
    
    try:
        id = int(input(Fore.LIGHTYELLOW_EX+"Enter dish id : "+Style.RESET_ALL))
        existing_data = readData()
        existing_data["Orders"][id-1]["status"] = input(Fore.LIGHTYELLOW_EX+"Enter updated order status(received/preparing/delivered) : "+Style.RESET_ALL) 
        writeData(existing_data)
        print()
        print(Fore.GREEN+"Successfully Updated..."+Style.RESET_ALL)
        print()
    except:
        print(Fore.RED+"Invalid Input"+Style.RESET_ALL)

def View_Orders():
    data = readData()
    
    table_data = [[item.get("id", ""),item.get("name", ""), item.get('items', ''), item.get("total_bill", ""), item.get("status", "")] for item in data["Orders"]]

    for row in table_data:
        status = row[4]
        row[2] = ", ".join(row[2])
        
        if status.lower() == "received":
            row[4] = f"\033[32m{status}\033[0m"
        elif status.lower() == "preparing" :
            row[4] = "\033[33m" + status + "\033[0m"
        else :
            row[4] = "\033[34m" + status + "\033[0m"

    # Display the table
    headers = ["Id", "Name","Items","Total_Bill","Status"]
    table = tabulate(table_data, headers, tablefmt="grid")
    print(table)

def main():

    while True:

        print("1. View all dish list.")
        print("2. Add a delicious new dish to the menu.")
        print("3. Remove a dish that is no longer served.")
        print("4. Update the availability of a dish.")
        print("5. Take a new order from a ravenous customer.")
        print("6. Update the status of an order.")
        print("7. Review all the orders.")
        print("0. Exit")

        choice = input(Fore.LIGHTYELLOW_EX+'Enter Your Choice : '+Style.RESET_ALL)

        if choice == '1':
            View_Dish_List()
        elif choice == '2':
            Add_Dish_To_Menu()
        elif choice == '3':
            Remove_Dish_From_List()
        elif choice == '4':
            Update_Availability()
        elif choice == '5':
            New_Order()
        elif choice == '6':
            Update_Order_Status()
        elif choice == '7':
            View_Orders()
        elif choice == '0':
            print(Fore.GREEN+"Thanku for using Zest Zomato Application..."+Style.RESET_ALL)
            break
        else:
            print(Fore.RED+"Please Enter Correct option"+Style.RESET_ALL)

main()
        