a=[10,20,30,9]
for i in range(0,4):
   for j in range(1,4):
            for k in range(2, 4):
                if (a[i] + a[j] + a[k] == 59):
                    result=(a[i], a[j], a[k])
                    print("Triplet with sum equal to 59:",result)