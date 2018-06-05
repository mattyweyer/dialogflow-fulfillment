from flask import Flask, jsonify, request
from models import init_menu
from dialogflow import DialogflowRequest, DialogflowResponse, GoogleAssistantList

app = Flask(__name__)
menu = init_menu()


@app.route('/fulfillment', methods=['GET', 'POST'])
def fulfillment():
    fulfillment_request = request.get_json()
    action = fulfillment_request['queryResult']['action']
    parameters = fulfillment_request['queryResult']['parameters']

    if action == 'order_item.confirm':
        breakfast_name = parameters.get('breakfast-name')
        item = menu.find_items_by(name=breakfast_name)[0]
        success = item.order()
        if success:
            response_text = f'Great stuff! We\'ve placed the following order for you:\n{str(item)}'
        else:
            response_text = 'Sorry. Something went wrong with your order. Try again later.'
        return jsonify({'fulfillmentText': response_text})

    elif action == 'list_menu':
        items = [str(item) for item in menu.items]
        response_text = 'Here is QuickBytes breakfast menu:'
        response_text += '\n'.join(items)
        response_text += '\n\nWould you like to order something?'
        return jsonify({
            'fulfillmentText': response_text,
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": "Here is the QuickBytes menu."
                                }
                            }
                        ],
                    },
                    "systemIntent": {
                        "intent": "actions.intent.OPTION",
                        "data": {
                            "@type": "type.googleapis.com/google.actions.v2.OptionValueSpec",
                            **GoogleAssistantList(menu.items, title='QuickBytes Menu').json()
                        }
                    }
                }
            }
        })

    else:
        response_text = 'Sorry. QuickBytes wasn\'t sure what to do with your request.'
        return jsonify({'fulfillmentText': response_text})
