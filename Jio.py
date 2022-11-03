class Jio:

    def __init__(self, restaurant, jio_id):
        self.restaurant = restaurant
        self.orders = []
        self.jio_id = jio_id

    def add_jio(self, order):
        self.orders.append(order)

    def total_price(self):
        return sum([i.total_price() for i in self.orders]) 

    def __repr__(self):
        jios = f"Jio #{self.jio_id}:\n\n"
        jios += f"Restaurant: {self.restaurant}\n\n"
        for i in self.orders:
            jios += f"{i}\n"
            
        jios += f"Total Price: {self.total_price()}\n"
        jios += "-------------------------------------------------\n"
        return jios