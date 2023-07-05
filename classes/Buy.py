import Customer
import Item

class buy():
    def __init__(self, item, customer, count, cost, situation=0):
        self.Item = item
        self.Count = int(count)
        self.Cost = int(cost)
        self.Customer = customer

    def __repr__(self):
        return f"Buyyy ===> Customer: {self.Customer} , Item: {self.Item} , Count: {self.Count}\n"
    


