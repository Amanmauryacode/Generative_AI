from flask import Flask,request,jsonify

app = Flask(__name__)

post_list = []

@app.route('/createPost' , methods = ["POST"])
def createPost():
    try:
        post = request.get_json()
        post["id"] = len(post_list)+1
        post_list.append(post)
        return jsonify({"message":"Successfully Created..."})
    except Exception as e:
        print(e)
        return jsonify({"message":"Error"})
    
@app.route('/viewPost',methods=["GET"])
def view_post():
    if len(post_list) == 0:
        return "No post found..."
    else :
        return jsonify(post_list)


@app.route('/deletePost/<id>',methods=["DELETE"])
def delete_post(id):
    try:
        if int(id) <= len(post_list):
            del post_list[int(id)-1]
            return jsonify({"message":"Successfully Deleted..."})
        else:
            return f"No post associate with id : {id}"

    except Exception as e:
        print(e)
        return e

if __name__ == '__main__':
    app.run()

