class Item:

    def __init__(self, item_name, item_no, price, quantity):
        self.item_name = item_name
        self.item_no = item_no
        self.price = float(price)
        self.quantity = int(quantity)

    def total_price(self):
        return (self.price * self.quantity)

    def __repr__(self):
        return f"[Item #{self.item_no}: {self.item_name}, Price: {self.price}, Quantity: {self.quantity}]"