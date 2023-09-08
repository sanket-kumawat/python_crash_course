def squares(length):
    for n in range(length):
        yield n ** 2


for square in squares(5):
    print(square)


qubes = (n** 3 for n in range(5))

for qube in qubes:
    print(qube)