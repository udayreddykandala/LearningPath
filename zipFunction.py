'''
The zip function
1.Lists
takes iterables(lists,dict,tup,strings) and "zips" them into tuples
it is used for parallel iteration
Returns a zip object which is an iterator of tuples
'''

countries = ["india","columbia","usa"]
capitals = ["delhi","bogota","washington"]
cities = ["newyork","hyderabad","texas"]
countries_and_capitals = zip(countries,capitals,cities)
print(list(countries_and_capitals))
print(countries_and_capitals)
print(type(countries_and_capitals))
'''
print(countries_and_capitals.__next__())
print(countries_and_capitals.__next__())
print(countries_and_capitals.__next__())
# print(countries_and_capitals.__next__()) #Gives an error
'''


for country,capitals in countries_and_capitals:
    print(country,capitals)

'''
2.Dictionaries
'''
products = {"apple" :0.5,"pinapple": 1}
tech_products = {"india" :100, "columbia" :100,}
print(zip(products,tech_products))
print(list(zip(products,tech_products)))
print(list(zip(products.values(),tech_products.values())))

for product,tech_product in zip(products.values(),tech_products.values()):
    print(product,tech_product)
    print(product)
    print(tech_product)
'''
3.Tuples
'''

countries = ("india","columbia","usa")
capitals = ("delhi","bogota","washington")
cities = ("newyork","hyderabad","texas")
countries_and_capitals = zip(countries,capitals,cities)
print(list(countries_and_capitals))
print(list(zip(countries_and_capitals,capitals,cities)))

for country,capitals in countries_and_capitals:
    print(country,capitals)
    print(capitals)
    print(type(country))

'''
4.Strings
'''
countries ="india"
capitals ="delhi"
countries_and_capitals = zip(countries,capitals)
print(list(countries_and_capitals))

for country,capitals in countries_and_capitals:
    print(country,capitals)


