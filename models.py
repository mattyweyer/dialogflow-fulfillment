items_json = [
    {
        'name': 'Cappucino',
        'price': 'R27.95',
        'description': 'A shitty flat white.',
    },
    {
        'name': 'Flat White',
        'price': 'R28.95',
        'description': 'Pretty much a cappucino.',
    },
    {
        'name': 'Americano',
        'price': 'R19.99',
        'description': 'Basically just dirty water.',
    },
    {
        'name': 'Macchiato',
        'price': 'R29.99',
        'description': 'No one is quite sure what this is.',
    },
    {
        'name': 'Hot Chocolate',
        'price': 'R25.56',
        'description': 'Like chocholate, but hotter.',
    },
    {
        'name': 'Vodka Shot',
        'price': 'R15.55',
        'description': 'A great way to start the day.',
    },
    {
        'name': 'Two Keys Whiskey',
        'price': 'R36.95',
        'description': 'For the connoisseur.',
    },
]


class Item:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'Item: {self.name}\nPrice: {self.price}\nDescription {self.description}'

    @classmethod
    def from_dict(cls, item_dict):
        return cls(**item_dict)


class Menu:
    def __init__(self, items):
        self.items = items

    def find_items_by(self, **kwargs):
        allowed_kwargs = ['name', 'price', 'description']
        if not all(key in allowed_kwargs for key in kwargs.keys()):
            raise Exception('Illegal keyword argument for method Menu.find_items_by()')
        res = []
        for item in self.items:
            if all(getattr(item, key) == value for key, value in kwargs.items()):
                res.append(item)
        return res


def init_menu():
    return Menu([Item.from_dict(item) for item in items_json])
