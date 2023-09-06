message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Using int() to Accept Numerical Input
age = input("How old are you? ")
age = int(age)
print(age >= 18)

# while Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
