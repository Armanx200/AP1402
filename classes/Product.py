from random import randint

class product(): #Product
    def __init__(self, name, description="", image="Product.jpg"):   #must at least has a image
        self.ID = self.setid()
        self.Name = name
        self.Description = description
        self.image = image
        self.Images = []
        self.Rating = 0
        self.Rates = 0
    def __repr__(self):
        return f"Product: {self.Name}\nID: {self.ID}\nDescription: {self.Description}\nrating: {self.Rating}/5"
    def setid(self):
        return "PT"+str(randint(99999,999999))

    def RATE(self, rate):    #CALCULATE_RATE
        self.Rates += 1
        self.Rating = ((self.Rating * (self.Rates-1)) / self.Rates) + (rate/self.Rates)

    def CHANGE_NAME(self, name):
        self.Name = name

    def CHANGE_BIO(self, description):     #CHANGE_DESCRIPTION
        self.Description = description
        
    def CHANGE_IMAGE(self, image):
        self.Image = image

    def ADD_IMAGE(self, image):
        self.Images.append(image)

    def REMOVE_IMAGE(self, image):
        self.Images.remove(image)