class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return(f"{self.name} : {self.price}")
class Inventory:
    def __init__(self): 
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)
        print(f"{product.name} is added to the inventory")

    def show_inventory(self):
        for inv in self.inventory:
            print(inv)

def main():
    p1 = Product("apple", 30)
    p2 = Product("banana", 20)

    store_inventory = Inventory()

    store_inventory.add_product(p1)
    store_inventory.add_product(p2)

    store_inventory.show_inventory()

if __name__ == "__main__":
    main()

