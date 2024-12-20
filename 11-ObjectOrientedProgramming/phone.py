import random
class Phone():
    def __init__(self, brand , price, Is_onsale):
        self.brand = brand
        self.price = price
        self.Is_onsale= Is_onsale
    def sale(self,sale):
        self.sale = random.randint(0,2)
        if sale == 1: self.Is_onsale = True
        else: self.Is_onsale = False

    def receipt(self):
        return f'This {self.brand} costs {self.price}$ and it {self.Is_onsale}'
    
def main():
    Phone1 = Phone("Samsung", "$500", )
    