import itertools
a=[1,9,8,2,3,1,9,8]
b=[57,76,89,43,57,89]
c=[4,5,6,10,7,6,5,10]
s=set()
duplicate=[]
for number in itertools.chain(a,b,c):
    if number in s:
        duplicate.append(number)
    else:
        s.add(number)
print("Duplicates in the list are:",duplicate)
