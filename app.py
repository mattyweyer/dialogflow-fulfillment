from flask import Flask, jsonify, request
from models import init_menu

app = Flask(__name__)
menu = init_menu()


@app.route('/fulfillment', methods=['GET', 'POST'])
def fulfillment():
    fulfillment_request = request.get_json()
    action = fulfillment_request['queryResult']['action']
    parameters = fulfillment_request['queryResult']['parameters']

    return jsonify({'fulfillmentText': 'Hello'})
