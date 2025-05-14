# what is a dictionary{}?
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
   # file_counts["text"] -> 14
   # "jpg" in file_counts -> True
   #"html" in fule_counts -> False
   # dictionaries are mutable
file_counts["cfg"] = 8
print(file_counts) # {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
del file_counts["cfg"]
print(file_counts) # {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}


# iterationg over the contents of a dictionary
for extension in file_counts:
   print(extension)
     #print:
      # jpg
      # txt
      # csv
      # py

for ext, amount in file_counts.items():
   print("there are {} file with the .{} extension". format(amount, ext))
'''
print:
there are 10 file with the .jpg extension
there are 14 file with the .txt extension
there are 2 file with the .csv extension
there are 23 file with the .py extension
'''
# print(file_counts.keys()) #print: dict_keys(['jpg', 'txt', 'csv', 'py'])
# print(file_counts.values()) #print: dict_values([10, 14, 2, 23])

for value in file_counts.values():
   print(value)

'''
   Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
   Remember that the items method returns a tuple of key, value for each element in the dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beasts, attacks in cool_beasts.items():
    print("{} have {}".format(beasts, attacks))
'''

def count_letters(text):
   result = {}
   for letter in text:
      if letter not in result:
         result[letter] = 0
      result[letter] += 1
   return result

print(count_letters("aaaaaa")) # print: {'a': 6}
print(count_letters("my favorite movie is... mmm....")) # print: {'m': 5, 'y': 1, ' ': 4, 'f': 1, 'a': 1, 'v': 2, 'o': 2, 'r': 1, 'i': 3, 't': 1, 'e': 2, 's': 1, '.': 7}


# dictionaries vs lists
 # SET: used when you want to store a bunch of elements and be vertain that they're only present once

# study guide
'''
pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  

print(pet_dictionary.get("dogs", 0)) # Should print ['Yorkie', 'Collie', 'Bulldog']
'''
