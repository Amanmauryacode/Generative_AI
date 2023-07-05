import json
from flask import Flask,abort,jsonify
from flask import request

app = Flask(__name__)

def readData():
    with open("Day-06\db_zomato.json", "r") as file:
        data = json.load(file)
    return data

def writeData(existing_data):
    with open("Day-06\db_zomato.json", "w") as file:
        json.dump(existing_data, file)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        user = request.get_json()

        try:
            newUser = {
                "username":user["username"],
                "email":user["email"],
                "password":user["password"],
                "phone_number":user["phone_number"]
            }
            existing_data = readData()
            if len(existing_data["Users"]) !=0:
                for row in existing_data["Users"]:
                    if row["email"] == user["email"]:
                        return f"User exist with email : {user['email']}"
            
            existing_data["Users"].append(newUser)
            writeData(existing_data)
            return jsonify(newUser)
        except:
            return "Incomplete Data"

    else:
        abort(400)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            existing_data = readData()
            verify = False
            user = {}
            if len(existing_data["Users"]) !=0:
                    for row in existing_data["Users"]:
                        if row["email"] == data["email"] and row["password"] == data["password"]:
                            verify = True
                            user = row
                            break

            if verify and len(existing_data["Session"])!=0 and existing_data["Session"][0]["email"]==data["email"]:
                return "Already login..."
            elif verify:
                existing_data["Session"].append({"email":user["email"]})
                writeData(existing_data)
                return "Successfully Login..."
            else: 
                return "Wrong Credential"
        except Exception as e:
            print(str(e))
            return "Invalid Credential"
    else:
        return "fail"
    
if __name__ == '__main__':
    app.run()
