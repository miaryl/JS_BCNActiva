# data types
print(type("a")) # <class 'str'>
print(type(2))  # <class 'int'>

# Variables : names that we give to certain values in our programs
'''
length = 10
width = 2
area = length * width
print(area) # print: 20
'''

# expressions, numbers, and type conversions

base = 6
height = 3
area = (base*height) /2
print("the area of the triangle is: " + str(area))

'''
In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8.
 Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files.
 Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string. 
'''
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("the average size is: " + str(average))


hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests

print("each oerson needs to pay: " + str(share_per_person))


# practice quiz
'''
In this scenario, two friends are eating dinner at a restaurant.
 The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service.
 Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.
'''

bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2 

print("each person needs to pay: " + str(share))

