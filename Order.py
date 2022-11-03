class Order:

    def __init__(self, username):
        self.username = username
        self.items = []

    def add_order(self, item):
        self.items.append(item)

    def total_price(self):
        return sum([i.total_price() for i in self.items]) 

    def get(self, item_id):
        return self.items[item_id - 1]

    def update(self, item_id, item):
        self.items[item_id - 1] = item

    def delete(self, item_id):
        self.items.pop(item_id - 1)
        for index, i in enumerate(self.items):
            i.item_no = index + 1

    def __repr__(self):
        orders = f"{self.username}'s Order:\n"
        for index, i in enumerate(self.items):
            orders += f"{index + 1}. {i}\n"
        return orders