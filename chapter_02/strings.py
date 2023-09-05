name = "sanket kumawat"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "sanket"
last_name = "kumawat"

# f-strings
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.upper()}!"
print(message)

# add a tab
print(f"\t{first_name.title()} \t{last_name.title()}")

# add a new line
print(f"Name:\n{first_name.title()}\n{last_name.title()}")

# tab ans new line
print("List:\n\t1\n\t2\n\t3\n\t4")

# strip right side of a string
language = "Python  "
print(language.rstrip())

# strip left side of a string
language = "   Python"
print(language.lstrip())

# strip both side of a string
language = "   Python   "
print(language.strip())

# remove prefix
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

# remove suffix
file_name = 'program.py'
print(file_name.removesuffix('.py'))
