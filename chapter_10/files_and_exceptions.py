import json
from pathlib import Path

path = Path('pi_digits.txt')
# print(path)
contents = path.read_text()
print(contents)

# Accessing a File’s Lines
lines = contents.splitlines()
for line in lines:
    print('new line: %s' % line)

# Working with a File’s Contents
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))


# Writing to a File
write_path = Path('write_message.txt')
write_path.write_text("I love programming")

write_contents = "I love programming.\n"
write_contents += "I love creating new games.\n"
write_contents += "I also love working with data.\n"
write_path.write_text(write_contents)


# Exceptions
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("success")


# Storing Data

numbers = [2, 3, 5, 7, 11, 13, 15]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)


path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
