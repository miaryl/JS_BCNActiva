# what is a list? -> [ , , ,]
x = ["Now", "we", "are", "cooking!"]
 # print(type(x)) # print: <class 'list'>
  # len(x) -> 4

  #print("are" in x) #print: True
  #print("today" in x) #print: False

  #print(x[1:3]) #print: ['we", "are"]

'''
using the "split" string method from the preceding lesson,
complete the 'get_word' function to return the {n}th word from a passed sectence.
for example, get_word("This is a lesson about lists", 4) should return "lesson",
which is the 4th word in this sentence.
'''
def get_word(sentence, n):
    # only proceed if n is positive
    if n > 0:
        words =  sentence.split()       #that's I think first->word.split(" ") in sentence 
        # only proceed if n is not more that the number of words
        if n <= len(words):
            return(words[n -1])
        return ("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


# modifying the contents of a list
fruits = ["pineapple", "banana", "apple", "melon"]
   # fruits.append("kiwi") -> add "kiwi" after the "melon"
   # fruits.incert(0, "orange") -> incert "orange" position 0, which mean before the "pineapple"
   # fruits.remove("melon") -> remove the first meets "melon", which mean if there are more than 1 only remove first one 
     # and if you want to remove the word does not exist, it will get an value error
    # also there is pop() fuirts.pop(3) -> remove the word that at the index you passed 
    #fruits[2] = "strawberry" # -> remove "apple" and replace "strawberry" -> ['pineapple', 'banana', 'strawberry', 'melon']


# List [] and tuples () 
  # strings: sequences of characters, and are immutable
  # list: sequences of elements of any type, and are mutable
  # tuples: sequences of elements of any type, that are immutable
fullname = ('Grace', 'M', 'Hopper')

'''
Let's use tuples to store information about a file: 
its name, its type and its size in bytes. 
Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 
'''
def file_size(file_info):
	file_name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


# iterating over lists and tuples
animals = ["lion", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
     chars += len(animal)
    
print("total characters: {}, average length: {}".format(chars, chars/len(animals)))
  # print: total characters: 22, average length: 5.5

print("----------------------------------------------")
  # enumerate()
winners = ["ash", "dylan", "reese"]
for index, person in enumerate(winners):
     print("{} - {}".format(index + 1, person))
print("----------------------------------------------")
def full_emails(people):
     result = []
     for email, name in people:
          result.append("{} <{}>".format(name,email))
     return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
print("----------------------------------------------")
'''
Try out the enumerate function for yourself in this quick exercise. 
Complete the skip_elements function to return every other element from the list, 
this time using the enumerate function to check if an element is in an even position or an odd position.
'''
'''
def skip_elements(elements):
	result = []
    for index, element in enumerate(elements):    #for index, element in elements:
        if index % 2 == 0:
            result.append(element)   #even_elements += element
    return result
'''

def skip_elements(elements):
	result = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


# list comprehensions : let us create new lists based on sequences or ranges
multiples = []
for x in range(1,11):
      multiples.append(x*7)
print(multiples)
  # with list comprehensions, code will be more clear
multiples = [ x*7 for x in range(1,11)] # it's same as avobe
print(multiples)

print("--MORE EXAMPLES--")

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths) # print: [6,4,4,2,4,1]

#  ---------------------------------------
z = [x for x in range(0, 101) if x % 3 == 0]
print(z) # print: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

#  ---------------------------------------

def odd_numbers(n):
	return [x for x in range(1,n + 1) if x % 2 != 0 ]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
