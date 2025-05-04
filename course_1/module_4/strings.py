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

print(new_message)

 # method
pets = "cats & Dogs"
print(pets.index("&"))


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email




