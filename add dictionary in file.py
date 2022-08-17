# define dict
dict1 = {'Python': '.py', 'C++': '.cpp', 'Java': '.java'}
dict2 = {'Python': '.py', 'jjjjjjj': '.cpp', 'Java': '.java'}

# open file for writing
f = open("dict.txt", "w")

# write file
f.write(str(dict))
f.write(str(dict1))

# close file
f.close()
