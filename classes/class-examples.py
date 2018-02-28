class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def define_restaurant(self):
        print("Name: " + self.restaurant_name + " | Type: " + self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name + "is open!")


class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type,flavor):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = flavor
    

ice_shop = IceCreamStand("Ice-Shop","icecream","vanilla")
ice_shop.define_restaurant()
print("Flavor: " + ice_shop.flavor)