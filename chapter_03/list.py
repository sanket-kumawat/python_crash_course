# Appending Elements to the End of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'tvs')
print(motorcycles)

# Removing an Item Using the del Statement
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

# Popping Items from Any Position in a List
popped_motorcycle = motorcycles.pop(1)
print(popped_motorcycle)
print(motorcycles)

# Removing an Item by Value
motorcycles.remove('tvs')
print(motorcycles)

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
print(sorted(cars))
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# Finding the Length of a List
print(len(cars))
