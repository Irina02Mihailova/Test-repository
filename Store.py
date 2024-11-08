class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, add_name, price):
        self.items[add_name] = price
        print(f'Добавили новый товар {add_name} по цене {price}')

    def remove(self, add_name):
        if add_name in self.items:
            del self.items[add_name]
            print(f'Удален товар {add_name}')
        else:
            print(f'Товар {add_name} не найден')

    def get_price(self, add_name):
        return self.items.get(add_name, None)

    def update_price(self, add_name, new_price):
        if add_name in self.items:
            self.items[add_name] = new_price
            print(f'Цена товара {add_name} обновлена на {new_price}')
        else:
            print(f'Товар {add_name} не найден')


store1 = Store(name="Магазин 1", address="Улица 1, дом 1")
store2 = Store(name="Магазин 2", address="Улица 2, дом 2")


store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
