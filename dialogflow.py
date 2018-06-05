class GoogleAssistantList:
    def __init__(self, items, title=None):
        self.title = title
        self.items = items

    def json(self):
        list_items = {'listSelect': {'items': []}}
        for item in self.items:
            item_json = {
                "optionInfo": {
                    "key": str(item.id)
                },
                "description": item.description,
                "title": item.name
            }
            if self._image_url_ok(item.image_url):
                item_json.update({
                    "image": {
                        "url": item.image_url,
                        "accessibilityText": item.name
                    }
                })
            list_items['listSelect']['items'].append(item_json)
        if self.title:
            list_items['listSelect'].update({'title': self.title})

        return list_items

    @staticmethod
    def _image_url_ok(image_url):
        if not isinstance(image_url, str):
            return False
        return image_url.startswith('http://') or image_url.startswith('https://')


class DialogflowRequest:
    def __init__(self, fulfillment_request):
        self.action = fulfillment_request['queryResult']['action']
        self.parameters = fulfillment_request['queryResult']['parameters']


class DialogflowResponse:
    def __init__(self, speech):
        self.speech = speech

    def json(self):
        return {
            'fulfillmentText': self.speech
        }
