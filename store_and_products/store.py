from decimal import Decimal
class Product:
    def __init__(self, item_name, price, category):
        self.item_name = item_name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            percent_change += 1
            new_price = Decimal(percent_change * self.price).quantize(Decimal('0.01'))
            self.price = float(new_price)
            return self
        elif is_increased == False:
            new_price = Decimal(self.price - (percent_change * self.price)).quantize(Decimal('0.01'))
            self.price = float(new_price)
            return self
        else:
            return self
    def print_info(self):
        print(f"Product Name: {self.item_name}, Price: ${Decimal(self.price).quantize(Decimal('0.01'))}, Category: {self.category}")
        return self
class Store:
    def __init__(self, name, product):
        self.name = name
        self.product_list = [{"Item name": product.item_name, "Price": product.price, "Category": product.category}]
        self.product = product
    def add_product(self, new_product):
        self.product = new_product
        self.product_list.append({"Item name": new_product.item_name, "Price": new_product.price, "Category": new_product.category})
        return self
    def sell_product(self, id):
        for i in range(len(self.product_list)):
            self.product_list.pop(id)
            return self
    def display_products(self):
        print(f"Products: {self.product_list}")
        return self

product1 = Product("Skim Milk", 3.00, "Food") 
product2 = Product("Bike for racing", 150.00, "Sports") 
product3 = Product("Chair for home", 55.00, "House Decor")

store1 = Store("Walmart", product1)
store1.add_product(product2).add_product(product3)
product2.update_price(0.50, False).print_info()
product3.update_price(0.50, True).print_info()
product3.update_price(0.25, False).print_info()

store1.display_products()

store1.sell_product(1)
store1.sell_product(0)
store1.display_products()


