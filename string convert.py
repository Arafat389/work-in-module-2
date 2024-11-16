a ="arafat islam"
print(a.upper())

b = "ARAFAT ISLAM"
print(b.lower())
print(a.capitalize())
# first letter capital  all world
print(a.title())
print(a.swapcase())
# replace
text = "hello world"
print(text.replace("world","python"))

# string to list

text = "hello-world-a"
print(text.split("-"))
#  list to string
text = ['hello', 'world', 'a']
print("-".join(text))


text = "   hello world  "

#left or right space remove
print(text.strip())
#left space remove
print(text.lstrip())
#right space remove
print(text.rstrip())
print(text.strip().upper())