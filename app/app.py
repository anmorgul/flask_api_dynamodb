from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
from config import Config

import app.controller as controller

#status
@app.route('/status/', methods = ['POST', 'GET'])
def status():
    data = {"a": "i am ok"}   
    return make_response(jsonify(data), 200)

#addItem 
@app.route('/addItem/', methods = ['POST'])
def add_items():
    data = request.get_json()
    response = controller.addItem(data['id'], data['model'], data['color'])
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    }

#getItem 
@app.route('/getItem/', methods = ['POST'])
def get_item():
    data = request.get_json()
    response = controller.GetItem(data['id'])
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        
        if ('Item' in response):
            return { 'Item': response['Item'] }

        return { 'msg' : 'Item not found!' }

    return {
        'msg': 'Some error occured',
        'response': response
    }

#getItems
@app.route('/getItems/', methods = ['POST', 'GET'])
def get_items():
    response = controller.GetItems()

    return make_response(jsonify(response))

if __name__ == '__main__':
    app.run(debug=True)

