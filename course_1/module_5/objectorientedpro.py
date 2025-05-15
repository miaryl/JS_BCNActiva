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