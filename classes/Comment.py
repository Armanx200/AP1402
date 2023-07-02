import datetime

class Comment():
    def __init__(self,customer_id, item_id, comment):
        self.Date = datetime.datetime.now()
        self.Customer_ID = customer_id
        self.Item_ID = item_id
        self.Comment = comment
    def __repr__(self):
        return f"{self.Customer_ID} comment about {self.Item_ID} : \n {self.Comment}"