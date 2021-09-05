# import argv from sys module
from sys import argv

# save command arguments in variable 'script' & 'filename'
script, filename = argv

# open file and save it in variable 'txt'
txt = open(filename)

print("Here's your file %r:" % filename)

# read file content
print(txt.read())

print("Type the filename again:")
file_again = input(">")

text_again = open(file_again)

# text_again.close()

print(text_again.read())
