details=[{"name":"Anne","age":18},
    {"name":"Frank","age":20},
    {"name":"Tom","age":13},
    {"name":"Alice","age":25},
    {"name":"Bob","age":16}
         ]
print(details)
under_age=list(filter(lambda x:x["age"]<18,details))
print("Under 18:",under_age)
max_age=list(filter(lambda x:x["age"]>=18,details))
print("Above 18:",max_age)
