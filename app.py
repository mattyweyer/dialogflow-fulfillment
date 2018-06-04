from flask import Flask, jsonify, request
from models import init_menu

app = Flask(__name__)
menu = init_menu()


@app.route('/fulfillment', methods=['GET', 'POST'])
def fulfillment():
    fulfillment_request = request.get_json()
    action = fulfillment_request['queryResult']['action']
    parameters = fulfillment_request['queryResult']['parameters']

    if action == 'userorder.userorder-yes':
        item = menu.find_items_by(name=parameters['drink'])[0]
        response_text = f'Great stuff! We\'ve placed the following order for you:\n{str(item)}'

    elif action == 'user.list_menu':
        items = [str(item) for item in menu.items]
        response_text = 'Here is Roxy\'s drinks menu:'
        response_text += '\n'.join(items)
        response_text += '\n\nWould you like to order something?'

    else:
        response_text = 'Sorry. Roxy\'s wasn\'t sure what to do with your request.'

    return jsonify({'fulfillmentText': response_text})
