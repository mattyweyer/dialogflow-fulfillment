import requests
import datetime


class Item:
    def __init__(self, id, name, price, description, image_url=None):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url

    def __str__(self):
        return f'\nItem: {self.name}\nPrice: {self.price}\nDescription {self.description}'

    def order(
            self, vegan='0', vegetarian='0', halaal='0',
            egg_style='scrambled', egg_feel='medium soft', bacon_style='crispy',
            meal_special_considerations=''):
        order_json = {
            'order': {
                'meal_id': str(self.id),
                'date': datetime.datetime.now().strftime('%a, %d %b %Y'),
                'vegan': vegan,
                'vegetarian': vegetarian,
                'halaal': halaal,
                'egg_style': egg_style,
                'egg_feel': egg_feel,
                'bacon_style': bacon_style,
                'meal_special_considerations': meal_special_considerations,
            }
        }
        response = requests.post('http://d8da2d7b.ngrok.io/api/orders', json=order_json)
        return response.status_code == 200

    @classmethod
    def from_dict(cls, item_dict):
        image_url = item_dict.get('image_url')
        return cls(
            id=item_dict['id'], name=item_dict['name'],
            price=item_dict['price'], description=item_dict['description'],
            image_url=image_url)


class Menu:
    def __init__(self, items):
        self.items = items

    def find_items_by(self, **kwargs):
        allowed_kwargs = ['id', 'name', 'price', 'description']
        if not all(key in allowed_kwargs for key in kwargs.keys()):
            raise Exception('Illegal keyword argument for method Menu.find_items_by()')
        res = []
        for item in self.items:
            if all(getattr(item, key) == value for key, value in kwargs.items() if value is not None):
                res.append(item)
        return res


def init_menu():
    menu = requests.get('http://d8da2d7b.ngrok.io/api/orders/menu').json()
    return Menu([Item.from_dict(item) for item in menu])
