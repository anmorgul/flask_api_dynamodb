from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/status/', methods = ['POST', 'GET'])
def status():
    data = {"a": "i am ok"}   
    return make_response(jsonify(data), 200)

#addItem 
@app.route('/addItem/',methods = ['PUT'])
def add_items():
    data = {"a": "item added"}   
    return make_response(jsonify(data), 200)
    # return jsonify(aws_controller.get_items())

#getItem 
@app.route('/getItem/', methods = ['POST'])
def get_item():
    id = request.json
    data = {"a": "id"}   
    return make_response(jsonify(id), 200)

#getItems
@app.route('/getItems/', methods = ['POST', 'GET'])
def get_items():
    data = {"a": "items "}   
    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run(debug=True)

