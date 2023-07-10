import json
from pymongo import MongoClient
from flask import Flask,abort,jsonify,render_template
from flask import request
from flask_cors import CORS


client = MongoClient('mongodb+srv://amanmaurya8419:Aman1234@cluster0.cmojrdr.mongodb.net/?retryWrites=true&w=majority')

db = client['zomato_database']

User = db['Users']
Dish = db['Dish']
Orders = db['Orders']
Session = db['Session']

app = Flask(__name__)
CORS(app)
def readData():
    with open("Day-07_pre\Day-06\db_zomato.json", "r") as file:
        data = json.load(file)
    return data

def writeData(existing_data):
    with open("Day-07_pre\Day-06\db_zomato.json", "w") as file:
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
            existing_user = User.find_one({"email":user["email"]})
            
            if existing_user!=None:
                return jsonify({"message":"already exists email"})
            
            User.insert_one(newUser)
            return jsonify({"message":"Successfully registered..."})
        except:
            return jsonify({"message":"Incomplete Data"})
    else:
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            existing_user = User.find_one({"email":data["email"]})
            
            if existing_user==None:
                return jsonify({"message":"Wrong Credentials"})
            elif existing_user["password"] != data["password"]:
                return jsonify({"message":"Wrong Credentials"})
                
            return jsonify({"message":"Successfully login...","name":existing_user["username"]})
            
        except Exception as e:
            print(str(e))
            return jsonify({"message":"Invalid Credential"})
    else:
        return render_template("index.html")


@app.route("/dish",methods=["GET"])
def getAllDish():
    if request.method== "GET":
        try:
            projection = {'_id': False}
            data = Dish.find({},projection)
            dishData = list(data)
            return jsonify(dishData)
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
        projection = {'_id': False}
        data = Dish.find({},projection)
        existing_data = list(data)
        orderData = Orders.find({},projection)
        allOrders = list(orderData)
        items = []
        totalBill = 0
        for row in neworder["items"]:
            items.append(existing_data[int(row)-1]["name"])
            totalBill += int(existing_data[int(row)-1]["price"])
        neworder["items"] = items
        neworder["total_bill"] = totalBill
        neworder["id"] = len(allOrders)+1
        neworder["status"] = "preparing"
        Orders.insert_one(neworder)
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
        projection = {'_id': False}
        data = Orders.find({},projection)
        existing_data = list(data)
        return jsonify(existing_data)
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
