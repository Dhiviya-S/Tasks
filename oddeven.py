a=[10,501,22,37,100,999,87,351]
e=[]
o=[]
for num in a:
    if (num%2==0):
        e.append(num)
    else:
        o.append(num)
print("Even numbers:",e)
print("Odd Numbers:" ,o)