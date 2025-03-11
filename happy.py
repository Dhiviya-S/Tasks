a=[10,501,22,37,100,999,87,351]
happy = []
count = 0
for number in a:
    num = number
    while(num>=10):
        sum = 0
        while (num > 0):
            n = num % 10
            sum = sum + (n * n)
            num = num // 10
        num=sum
    if (num == 1):
        happy.append(number)
        count = count + 1
    else:
        continue
print("Happy numbers count:", count)
print("Happy numbers are:", happy)
