import functools
list=[9,8,3,5,6,2]
product = functools.reduce(lambda x, y: x * y, list)
print("Product of numbers in list:",product)

# list=[9,8,3,5,6,2]
# res=1
# for numbers in list:
#     res=numbers*res
# print(res)