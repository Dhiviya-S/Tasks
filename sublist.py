a = [4, 2, -3, 1, 6]
sublist = []
for i in range(0, 5):
    for j in range(i + 1, 6):
        sublist.append(a[i:j])
        sub = sum(a[i:j])
        if (sub == 0):
            print("Sublist with sum equal to zero:\n", a[i:j])
print("Sublist of a:\n", sublist)