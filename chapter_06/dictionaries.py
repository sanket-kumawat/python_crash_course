user = {'username': 'admin', 'password': 654321}
print(f"{user['username']} {user['password']}")

# Adding New Key-Value Pairs
user['first_name'] = 'Sanket'
user['last_name'] = 'Kumawat'
print(user)

# Removing Key-Value Pairs
del user['last_name']
print(user)

# Using get() to Access Values
print(user.get('first_name'))
print(user.get('last_name'), 'no last name available')

# Looping Through a Dictionary
for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping Through All the Keys in a Dictionary
for key in user.keys():
    print(key)
for key in user:
    print(key)

# Looping Through a Dictionary’s Keys in a Particular Order
for key in sorted(user.keys()):
    print(f"\nKey: {key}")

# Looping Through All Values in a Dictionary
for value in user.values():
    print(f"\nValue: {value}")

# print values without repetition
user['last_name'] = 'Sanket'
print(user)
for value in set(user.values()):
    print(f"\nValue: {value}")
