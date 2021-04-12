# Let's give some methods to our Product class:

#     - update the product's price. If price is increased, it should increase by percentage provided. Else the price should lower based on percentage provided.
#     - print the name of the product, its category, and its price.

# Let's also give some methods to our Store class:

#     - take a product and add it to the store
#     - remove the product from the store's list of products given the id
#     - increase the price of each product by the percent_increase given
#     - update all the products matching the given category by reducing the price by the percent_discount given



class Store:
    items = []

    def __init__(self, name, products):
        self.name = name
        self.products = Product(name = "", price = 10, category = "consumable")

    def add_product(self, new_product):
        items.append(new_product)
    
    def sell_product(self, id):
        if id in items:
            items.pop(id)
        else:
            return "this item is not listed in the store."
    
    def inflation(self, percent_increase):
        self.price = self.products.update_price(1, ture)

    def set_clearance(self, category, percent_discount):
        self.price = self.products.update_price(1, false)


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased == true:
            self.price += percent_change
        elif is_increased == false:
            self.price -= percent_change
        else:
            return False

    def print_info(self):
        print(f'Name: {self.name}, Category: {self.category}, Price: {self.price}')
    
