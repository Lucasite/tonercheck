class Toner:
    def __init__(self, id, name, ad_prints, cus_prints):
        self.id = id
        self.name = name
        self.ad_prints = ad_prints
        self.cus_prints = cus_prints

    def print(self):
        print('='*5)
        print('Id:', self.id)
        print('Name: ', self.name)
        print('Advertised Prints: ' , self.ad_prints)
        print('Customer Average: ', self.cus_prints)
        print('='*5)

    def findAveragePrint(self):
        #find the average of the submitted customer testimony
        return None