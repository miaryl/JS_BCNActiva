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