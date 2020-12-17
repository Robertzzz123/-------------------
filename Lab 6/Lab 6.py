class Storage:
    def Storage_method(self):
        self.Storage = Storage
class Goods(Storage):
    '''Система складского учета'''
    def __init__(self, productname,weight, name):
        self.productname = productname
        self.weight = weight
        self.count = count
        self.dates = {}

    def reserv(self, date, places):
        reserved = instock
        if places + reserved > self.places:
            raise Exception
        else:
            instock = reserved + places

class Order(Storage):
    NEW = "New"
    RESERVED = "Reserved"
    COUNT = "Count"
    ABSENT = "Absent"

    def __init__(self, town, race, date, places, carrage):
        self.productname = productname
        self.weight = weight
        self.count = count
        self.date = date
        self.places = places
        self.state = Order.NEW

    def reserv(self):
        if self.state == Order.NEW:
            try:
                self.goods.reserv()
                self.state = Order.RESERVED
            except:
                 raise Exception
        else:
            raise Exception

class System:
    t1 = "Books"
    t2 = "Sugar"
    t3 = "Wine"

    gc1 = Goods(t1, 1, 3)
    gc2 = Goods(t2, 4, 1)
    gc3 = Goods(t3, 5, 20)

    orders = []

    def order(self, productname, weight, count, date, places):
        new_order = Order(weight, productname, count, date, places)
        self.orders.append(new_order)

    def reserv(self, order):
        order.reserv()
