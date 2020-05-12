#Wag.price('lowfuel')
#Bmw.price('manyfuel')



class Vehicle:

    def __init__(self, name):
        self.name = name
        pass

class Wag(Vehicle):

    def price(self):
        print(self.name +'low price')
    def type(self):
        print(self.name + "option coupe")
    def engy(self):
        print(self.name + "hybrid available now")


class Bmw(Vehicle):

    def price(self):
        print(self.name +'very expensive')
    def color(self):
        print(self.name + "can be any color for you")
    def dealers(self):
        print(self.name + "main dealer in Chisinau AVG Prem")

wag = Wag('WAG car ')
bmw = Bmw('BMW car ')

wag.price()
wag.type()
wag.engy()
bmw.price()
bmw.color()
bmw.dealers()

