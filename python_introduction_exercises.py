"""
blah 
"""

# print("Hello World!")
# response = ''
# counter = 0
# while response != 'stop_please':
#     response = input("Say something: ")
#     counter += 1
#     if counter >= 5:
#         break

items = ['banana', 'apple', 'kiwi']
items_list = []
for i, item in enumerate (items):
    print(i, item)
    x = (i, item)
    items_list.append(x)

print(items_list)
# list(enumerate(items_list))
