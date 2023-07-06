#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Transaction:
    def __init__(self, name):
        self.name = name
        self.items = {}
    
    def add_item(self, name, amount, price):
        self.items[name] = {"amount": amount, "price": price}
        
    def update_item_name(self, name, new_name):
        if name in self.items:
            self.items[new_name] = self.items.pop(name)
        else:
            print(f"Item '{name}' not found in the transaction.")

    def update_item_qty(self, name, amount):
        if name in self.items:
            self.items[name]["amount"] = amount
        else:
            print(f"Item '{name}' not found in the transaction.")

    def update_item_price(self, name, price):
        if name in self.items:
            self.items[name]["price"] = price
        else:
            print(f"Item '{name}' not found in the transaction.")    
            
    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"Item '{name}' not found in the transaction.")
            
    def reset_transaction(self):
        self.items = {}

    def check(self):
        total_price = 0
        for name, item in self.items.items():
            print(f"Name: {name}")
            print(f"Amount: {item['amount']}")
            print(f"Price: {item['price']}")
            
            if item['price'] is None:
                raise ValueError(f"Missing price for item '{name}'")
            if name is None:
                raise ValueError(f"Missing name for item '{name}'")
            if item['amount'] is None:
                raise ValueError(f"Missing amount for item '{name}'")
            
            total_price += item['price'] * item['amount']

        discount = 0
        if 200000 < total_price <= 300000:
            discount = 0.05 * total_price
            total_price -= discount
            print("Congratulations! You qualified for a 5% discount.")
        elif 300000 < total_price <= 500000:
            discount = 0.08 * total_price
            total_price -= discount
            print("Congratulations! You qualified for an 8% discount.")
        elif total_price > 500000:
            discount = 0.1 * total_price
            total_price -= discount
            print("Congratulations! You qualified for a 10% discount.")

        print(f"Your order is confirmed! The total price is Rp{total_price:.2f}")

