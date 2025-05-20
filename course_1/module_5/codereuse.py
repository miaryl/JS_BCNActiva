#inheritance
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.color) #print: green
print(carnelian.flavor) #print: sweet

print("-----------------------------------------")

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))


class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak() #print: Oink! I'm Hamlet! Oink!


class Cow(Animal):
    sound = "Mooooo"

milky = Cow("Milky white")
milky.speak() #print: Mooooo I'm Milky white! Mooooo

'''
Let’s create a new class together and inherit from it. 
Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, 
that inherits methods from the Clothing class. Fill in the blanks to make it work properly.


class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

      	
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial() #print: This Polo is made of Cotton

'''

#Composition
'''always initialize mutable attributes in the constructor'''
class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result
    

'''
Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: 
Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. 
When you’re finished, the script should add up to 10 cotton clothing items.


class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

    
class shirt(Clothing):
  material="Cotton"

class pants(Clothing):
  material="Cotton"
  

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")

print(current_stock) #print: 10  

'''
#PYthon modules
import random
print(random.randint(1,50)) #print: random number from 1 to 50


import datetime
now = datetime.datetime.now()
print(type(now)) #print: <class 'datetime.datetime'>
print(now) #print: current time like : 2025-05-20 12:21:46.225874
print(now.year, now.day) #print: 2025 20
print(now + datetime.timedelta(days=28)) #print: 2025-06-17 12:24:49.607924 







    