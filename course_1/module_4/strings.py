#the parts of a strings
 # string indexing

name = 'Jaylen'
print(name[1])

text = "random string with a lot of characters"
print(text[-1])
print(text[-2])

 # slice
color = "orange"
print(color[1:4]) # print: ran o is 0 and always numbers -1/ o-0, r-1, a-2, n-3, g-4, e-5

fruit = "Pineapple"
print(fruit[:4]) # print: Pine
print(fruit[4:]) # print: apple

# creating new strings
# string is inmutable
message = "a kong string with a silly typo"
   # message[2] = "l" it not work
new_message = message[0:2] + "l" + message[3:]

print(new_message) # print : a long string with a silly typo

 # method
pets = "cats & Dogs"
print(pets.index("&")) # print: 5


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email



# more string methods
answer = 'YES'
if answer.lower() == "yes":
    print("user said yes")

 #strip()
print(" yes ".strip()) # print: yes without space | also there are 'rstrip()' and 'lstrip()'
 #count()
print("the number of times e occurs in this string is 4".count("e")) #print: 4
 #endswith()
print("Forest".endswith("rest")) # print: True
 #isnumeric()
print("forest".isnumeric(), "12345".isnumeric()) # print: Flase True
       # 12345.isnumeric() will be syntax error
 #join()
words = " ".join(["this", "is", "a", "phrase", "joined", "by", "spaces"] ) 
print(words + ".") #print: all the words in [] with space
 #split
print("this is another example".split()) #print: ['this', 'is', 'another','example']



# formatting strings
name = "Manny"
number = len(name) *3
print("Hello {}, your lucky numebr is {}!".format(name, number)) #print: Hello Manny, your lucky number is 15!

print("-----------------------------------------------------------------------")
def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print("-----------------------------------------------------------------------")
price = 7.5
with_tax = price * 1.09
print(price, with_tax) #print: 7.5 8.175 
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax)) # f= float 
    #print: Base price: $7.50. With tax: $8.18
print("-----------------------------------------------------------------------")
def to_celsius(x):
    return (x-32) *5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
'''
In these two expressions we're using ">" operator to align text to the right so that the output is neatly aligned.
In the first expression we're saying we want the numbers to be aligned to the right for a total of three spaces. 
In the second expression we're saying we want the number to always have exactly two decimal places and we want to align it to the right at six spaces.
We can use string formatting like this to make the output of our program look nice and also to generate useful logging and debugging messages.
'''

#study guide
def mirrored_string(my_string):
    forwards = ""
    backwards = ""

    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
            print(backwards) #prints backwards because i don't understand well what is it happen "backwards"
    if forwards.lower() == backwards.lower():
        return True
    return False

print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True

print("-----------------------------------------------------------------------")

# This function generates a username using the first 3 letters of a
# user’s last name plus their birth year. 
def username(last_name, birth_year):
    
    # The .format() method will use the first 3 letters at index 
    # positions [0,1,2] of the "last_name" variable for the first
    # {} placeholder. The second {} placeholder concatenates the user’s
    #  "birth_year" to that string to form a new string username.
    return("{}{}".format(last_name[0:3],birth_year))


print(username("Ivanov", "1985")) 
# Should display "Iva1985" 
print(username("Rodríguez", "2000")) 
# Should display "Rod2000" 
print(username("Deng", "1991")) 
# Should display "Den1991"

print("-----------------------------------------------------------------------")

# This function checks a given schedule entry for an old date and, if 
# found, the function replaces it with a new date. 
def replace_date(schedule, old_date, new_date):

    # Check if the given "old_date" appears at the end of the given 
    # string variable "schedule". 
    if schedule.endswith(old_date):

        # If True, the body of the if-block will run. The variable "n" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "new_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the 
        # old date replaced by the new date. The schedule[:-p] part of 
        # the code trims the "old_date" substring from "schedule" 
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as 
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The 
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist.  
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)


        # Returns the schedule with the new date.
        return new_schedule
        
    # If the schedule does not end with the old date, then return the
    # original sentence without any modifications.
    return schedule
 
 
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"

