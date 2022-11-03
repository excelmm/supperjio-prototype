from Item import Item
from Order import Order
from Jio import Jio

def main():

    jios = {}
    jio_id = 1
    
    while True:
        command = input("Hello, and welcome to Supper Jio! What would you like to do? (type \"help\" for a list of commands) ").strip().lower()

        if command == "newjio":

            username = input("To start, what is your name? ").strip()
            order = Order(username)

            restaurant = input(f"Great, {username}! Where would you like to order from? ").strip()
            jio = Jio(restaurant, jio_id)

            print("Okay, what would you like to order? (type y when done) ")
            item_no = 1
            while True:

                item_name = input("Item Name: ")
                if item_name == "y":
                    break

                price = input("Price: ")
                quantity = input("Quantity: ")
                item = Item(item_name, item_no, price, quantity)
                add_item_to_order(item, order)
                item_no += 1
            
            add_order_to_jio(order, jio)
            jios[jio_id] = jio
            jio_id += 1

            print("Jio created! Details:")
            print(jio)

        elif command == "joinjio":
            print(f"Ongoing Jios:\n{jios_string(jios)}")
            id = int(input("Which Jio would you like to join?"))
            if id in jios:

                username = input("To start, what is your name? ").strip()
                order = Order(username)

                jio = jios[id]
                print("Okay, what would you like to order? (type y when done) ")
                item_no = 1
                while True:

                    item_name = input("Item Name: ")
                    if item_name == "y":
                        break

                    price = input("Price: ")
                    quantity = input("Quantity: ")
                    item = Item(item_name, item_no, price, quantity)
                    add_item_to_order(item, order)
                    item_no += 1
                
                add_order_to_jio(order, jio)
            else:
                print("Jio not found")
                continue

        elif command == "showjios":
            print(f"Ongoing Jios:\n{jios_string(jios)}")

        elif command == "deleteitem":
            print(f"Ongoing Jios:\n{jios_string(jios)}")
            id = int(input("From which Jio would you like to delete? "))
            if id in jios:
                jio = jios[id]
                print(jio)
                order_username = input("Who's Order would you like to delete? ")
                order = None
                for i in jio.orders:
                    if order_username == i.username:
                        order = i
                
                print(order)
                item_id = int(input("Which item would you like to delete? "))
                order.delete(item_id)
                print("Item deleted!")

            else:
                print("Jio not found")
                continue

        elif command == "modifyitem":
            print(f"Ongoing Jios:\n{jios_string(jios)}")
            id = int(input("From which Jio would you like to modify? "))
            if id in jios:
                jio = jios[id]
                print(jio)
                order_username = input("Who's Order would you like to modify? ")
                order = None
                for i in jio.orders:
                    if order_username == i.username:
                        order = i
                
                print(order)
                item_id = int(input("Which item would you like to modify? "))
                item = order.get(item_id)

                item_name = input("Item Name: ")
                price = input("Price: ")
                quantity = input("Quantity: ")

                order.update(item_id, Item(item_name, item_id, price, quantity))
                print("Item updated!")

            else:
                print("Jio not found")
                continue

        elif command == "exit":
            print("Thank you for using Supper Jio!")
            break

        elif command == "help":
            print("Available commands: newjio, joinjio, showjios, deleteitem, modifyitem, exit, help")

        else: 
            print("Command not found.")
        
def add_item_to_order(item, order):
    order.add_order(item)

def add_order_to_jio(order, jio):
    jio.add_jio(order)

def jios_string(jios):
    return_string = ""
    for i in jios:
        return_string += f"{jios[i]}\n"
    return return_string

if __name__ == "__main__":
    main()