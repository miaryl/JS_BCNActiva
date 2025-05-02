# comparing thins

print("Yellow" > "Cyan" and "Brown" > "Magenta") # print: False


my_variable = 3*5
print(my_variable == 3*5) # frint: True

'''
The comparison operators greater than > and less than < can be used to alphabetize words in Python.
 The letters of the alphabet have numeric codes in Unicode (also known as ASCII values).
 The uppercase letters A to Z are represented by the Unicode values 65 to 90. The lowercase letters a to z are represented by the Unicode values 97 to 122.
'''
# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.
print("Wednesday" > "Friday")

# If the strings have the same first few letters, the comparison will 
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values. In this example, 
# both strings share the initial substring "sun", but then have 
# different letters with different Unicode values in the fourth place 
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan")

# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")



# This last example illustrates the result of trying to compare two
# items of different data types using the less than < operator. The 
# greater than > and less than operators < cannot be used to compare
# two different data types. 
     #print("Five" < 6)
'''
Error on line 1:
    print("Five" < 6)
TypeError: '<' not supported between instances of 'str' and 'int'
'''


# branching with if statements / else / elif
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else:
        print("valid username")

hint_username("li")
hint_username("Sally")
hint_username("iamalwayssleepyhelpmealsohungry")

# else does not need always 
def is_even(number):
    if number % 2 == 0:
        return True
    return False


def translate_error_code(error_code):
    if error_code == "401 Unauthorized":
         translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":
         translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
         translation = "Server request to close unused connection"
    else:
         translation = "Unknown error code"
    return translation

print(translate_error_code("404 Not Found"))

