print((lambda x: x + 1)(2))


square = lambda x: x**2
print(square(5))


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('sanket', 'kumawat'))


high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))