'''
Lambda Functions
Also called anonymous functions
its syntax is as follows:
lamda arguments: expressions
They can take any number of arguments
lamda functions are created at runtime

'''
add = lambda x, y: x + y
print(add(2, 3))

i = 10
add = lambda x : x + i
print(add(8))

lamda_functions = [lambda x: x+j for j in range(10,100)]
first_lambda = lamda_functions[0]
print(first_lambda(5))
#the j will take the value of 99 cause lambda functions are executed at the runtime
#it will take the last value of j
#so here the output will be 5+99=104

mul = lambda x, y,z : x * y *z
print(mul(2,3,4))
