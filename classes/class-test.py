class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers = 0
    
    def define_restaurant(self):
        print("Name: " + self.restaurant_name + " | Type: " + self.cuisine_type)
    
    def open_restaurant(self):
        print(self.restaurant_name + "is open!")

    def set_customers(self,num_customers):
        self.customers = num_customers
    
    def increment_customers(self):
        self.customers+=10

restaurant_pizza = Restaurant("Pizza Planet","Italian food")
restaurant_burger = Restaurant("Burger Planet","Fast food")
restaurant_vegan = Restaurant("Pizza Planet","Vegan food")
restaurant_vegan.set_customers(20)
restaurant_vegan.increment_customers()

print("Number of customes : " + str(restaurant_vegan.customers))

restaurant_pizza.define_restaurant()
restaurant_burger.define_restaurant()
restaurant_vegan.define_restaurant()


class User():

    def __init__(self,userinfo):
        self.userinfo = userinfo
        self.login_attempts = 0

    def describe_user(self):
        for key,value in self.userinfo.items():
            self.userinfo[key] = value
        return self.userinfo

    def greet_user(self):
        print("Hello " + self.userinfo['name'])

    def increment_login_attempts(self):
        self.login_attempts+=1

    def decrement_login_attempts(self):
        self.login_attempts-=1   

    def reset_login_attempts(self):
        self.login_attempts=0


info_user1 = {'name':'Bartolo','lastname':'Hold','address':'C/Lagos','phone':'+4560978689'}
info_user2= {'name':'Carlos','lastname':'Malor','address':'C/Viñas','phone':'+60695312343'}

me = User(info_user1)
me.greet_user()
me.increment_login_attempts()
print("Attemps: " +str(me.login_attempts))
print(str(me.describe_user())+"\n")


you = User(info_user2)
you.greet_user()
print(you.describe_user())

