import json
from flask import Flask,abort,jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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
            return jsonify({"message":"Incomplete Data"})
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
                user["message"] = "Already login..."
                return jsonify(user)
            elif verify:
                existing_data["Session"].append({"email":user["email"]})
                writeData(existing_data)
                user["password"] = "NA"
                user["message"] = "Successfully login..."
                return jsonify(user)
            else: 
                return jsonify({"message":"Wrong Credential"})
        except Exception as e:
            print(str(e))
            return jsonify({"message":"Invalid Credential"})
    else:
        return jsonify({"message":"fail"})


@app.route("/dish",methods=["GET"])
def getAllDish():
    if request.method== "GET":
        try:
            data = readData()
            return jsonify(data["Dish"])
        except Exception as e:
            print(e)
            return jsonify([])


@app.route("/add",methods=["POST"])
def addDish():
    if request.method=="POST":
        try:
            data = request.get_json()
            existing_data = readData()
            data["id"] = len(existing_data["Dish"])+1
            existing_data["Dish"].append(data)
            writeData(existing_data)
            return jsonify({"message":"Successfully added..."})
        except:
            return jsonify({"message":"fail"})
    else:
        return jsonify({"message":"Request Failed"})
    
@app.route("/remove/<id>",methods=["DELETE"])
def removeDish(id):
    if request.method=="DELETE":
        try:
            existing_data = readData()
            data = existing_data["Dish"][int(id)-1]
            existing_data["Dish"].remove(data)
            for row in range(0,len(existing_data["Dish"])):
                existing_data["Dish"][row]["id"] = row+1
            writeData(existing_data)
            return jsonify({"message":"Successfully removed..."})
        except:
            return jsonify({"message":"Failed"})
    else:
        return jsonify({"message":"Request Failed"})
    
@app.route("/update/<id>",methods=["PUT"])
def updateDish(id):
    if request.method=="PUT":
        try:
            newData = request.get_json()
            existing_data = readData()
            newData["id"] =id
            existing_data["Dish"][int(id)-1] = newData
            writeData(existing_data)
            return jsonify({"message":"Successfully updated..."})
        except Exception as e:
            print(e)
            return jsonify({"message":"Failed"})
    else:
        return jsonify({"message":"Request Failed"})


@app.route("/neworder",methods=["POST"])
def newOrder():
    try:
        neworder = request.get_json()
        existing_data = readData()
        items = []
        totalBill = 0
        for row in neworder["items"]:
            items.append(existing_data["Dish"][row-1]["name"])
            totalBill += int(existing_data["Dish"][row-1]["price"][1:])
        neworder["items"] = items
        neworder["total_bill"] = totalBill
        neworder["id"] = len(existing_data["Orders"])+1
        neworder["status"] = "preparing"
        existing_data["Orders"].append(neworder)
        writeData(existing_data)
        return jsonify({"message":"Successfully ordered..."})
    except Exception as e:
        print(e)
        return jsonify({"message":"Failed"})


@app.route("/updateOrder/<id>",methods=["PUT"])
def updateOrder(id):
    try:
        neworder = request.get_json()
        existing_data = readData()
        existing_data["Orders"][int(id)-1]["status"] = neworder["status"]
        writeData(existing_data)
        return jsonify({"message":"Successfully updated..."})
    except Exception as e:
        print(e)
        return jsonify({"message":"Failed"})





@app.route("/orders",methods=["GET"])
def getOrders():
    try:
        existing_data = readData()
        return jsonify(existing_data["Orders"])
    except Exception as e:
        print(e)
        return jsonify({"message":"Failed"})


@app.route("/order/<name>",methods=["GET"])
def getOrderByName(name):
    try:
        existing_data = readData()
        data = []
        for row in existing_data["Orders"]:
            if row["name"] == name:
                data.append(row)
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({"message":"Failed"})









if __name__ == '__main__':
    app.run()
