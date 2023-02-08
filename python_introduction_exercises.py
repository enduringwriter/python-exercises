
print("Hello World!")

greeting = "Hello everyone!"
print(greeting)

items = ['banana', 'apple', 'kiwi']
items_list = []
for i, item in enumerate (items):
    print(i, item)
    x = (i, item)
    items_list.append(x)
print("items", items_list)


print(list(enumerate(items)))

x = enumerate(items)
print('dict', dict(x))
