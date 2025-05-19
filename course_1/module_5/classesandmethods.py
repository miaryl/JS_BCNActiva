# constructors and other special methods
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "this apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color) #print: red
print(jonagold) # call __str__ function  | print: this apple is red and its flavor is sweet



'''
Want to see this in action?
 
 In this code, there's a Person class that has an attribute name, which gets set when constructing the object. 
Fill in the blanks so that 1) when an instance of the class is created,
the attribute gets set correctly, and 2) when the greeting() method is called, 
the greeting states the assigned name.

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new innce with a name of your choice
some_person = Person("John")  
# Call the greeting method
print(some_person.greeting())   #first try, i forgot to put () after some_person.greeting and got error

'''


# documenting functions, classes, and methods
   # docstring: a brief text that explains what something does -> """ """
