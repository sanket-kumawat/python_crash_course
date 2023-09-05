# for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Making Numerical Lists
# Using the range() Function
for value in range(6):
    print(value)
for value in range(1, 6):
    print(value)
for value in range(1, 11, 2):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
print(players[:4])
print(players[2:])
print(players[-2:])
print(players[1:5:2])

# Looping Through a Slice
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

# Tuples
dimensions = (200, 50)
print(dimensions[0])