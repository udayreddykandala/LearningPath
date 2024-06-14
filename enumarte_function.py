from enum import Enum
fruits = ['apple', 'pear', 'orange', 'banana']
enumerated = enumerate(fruits)
print(list(enumerated))

enumerated = enumerate(fruits,start=100)
print(list(enumerated))

for index,value in enumerate(fruits):
    filename = f"filename{index}.jpeg"
    print(filename)