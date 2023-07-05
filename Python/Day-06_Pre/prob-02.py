from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

data = {}

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data1 = request.get_json()
        for key,value in data1.items():
            data[key] = value
        return f"Entry created successfully!"
    return render_template('create.html')

@app.route('/read')
def read():
    return jsonify(data)

@app.route('/update', methods=['GET', 'PUT'])
def update():
    if request.method == 'PUT':
        data1 = request.get_json()
        try:

            for key,value in data1.items():
                if key in data:
                    data[key] = value
                else : 
                     return f"Entry {key} does not exist!"
            return f"Entry  updated successfully!"
        except:
            return f"Entry does not exist!"
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    if request.method == 'DELETE':
        data1 = request.get_json()
        for key,value in data1.items():
            if key in data:
                del data[key]
                return f"Entry '{key}' deleted successfully!"
            else:
                return f"Entry '{key}' does not exist!"
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
