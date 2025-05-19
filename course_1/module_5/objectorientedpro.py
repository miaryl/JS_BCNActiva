# what is object- priented programming?
 #object-oriented programming: a flexible, powerful paradigm where classes represent an define concepts, while objects are instances of classes
 # arributes are haracteristics associated with a type. 
 # methods are: functions associated with a type


# defining new classes
class Apple:
    pass

class Apple:
    color = "" 
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color, jonagold.flavor) # print: red sweet
  #dot notation:lets you access any of the abilities the object might have(called methods) or information it might store (called attributes)
print(jonagold.color.upper()) #print: RED

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"


#instance methods
  # methods: functions that operate on the attributes of a specific instance of a class
'''
class Piglet:
    def speak(self):
        print('oink oink')

hamlet = Piglet()
hamlet.speak() #print: oink oink
'''
'''
class Piglet:
   name = "piglet"
   def speak(self):
      print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak() #print: Oink! I'm Hamlet! Oink!

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak() #print: Oink! I'm Petunia! Oink!
'''
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
    
piggy = Piglet()
print(piggy.pig_years()) #print: 0
piggy.years = 2
print(piggy.pig_years()) #print: 36

'''
Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years()) #print: 21
'''