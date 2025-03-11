a=[5,6,99,33,11,7,8,9,22,5,77,8,6]
s=[]
duplicate=[]
for number in a:
    if number in s:
        duplicate.append(number)
    else:
        s.append(number)
print("Duplicates in the list are:",duplicate)
newlist=list(s)
non=[]
for num in newlist:
    if num not in duplicate:
        non.append(num)
    else:
        s.append(number)
print("First Non Repeating Element:",non[0])