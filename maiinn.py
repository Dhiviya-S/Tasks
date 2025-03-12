#ODD AND EVEN NUMBERS LIST##
given=[10,501,22,37,100,999,87,351]
e=[] #Creating empty list to append the values
o=[]
for num in given: #Each number in 'a' list will be passed
    if (num%2==0): #modulus of 2 returns 0 then it is even else odd
        e.append(num)
    else:
        o.append(num) #Appending values to new list
print("Even numbers:",e)
print("Odd Numbers:" ,o)
print()
##PRIME NUMBERS##
def prime(n): #defining a function with parameter 'n'
 if n<2:
  return False #if n is less than then it is not prime
 for i in range(2,int(n**0.5)+1): #For n=501, Instead of checking from 2 to 501,here we check in range of 2 to sqrt(n)+1
  if n%i==0: # if modulus value returns 0, then it is not prime.
   return False
 return True #This returns prime numbers

a_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_num=[num for num in a_list if prime(num)]#Passing list of values through for loop in function calling and 'num' is argument
print("Prime numbers in list:",prime_num)
print("Count of prime number:",len(prime_num)) #len is used to count the prime numbers in list
print()
##HAPPY NUMBERS IN LIST##
given_list=[10,501,22,37,100,999,87,351]
happy = [] #Empty list to append the happy numbers
count = 0 #To count the total number of happy numbers in list
for number in given_list:
    num = number
    while(num>=10): #To repeat the inner loop if num value is greater than 10.Loop repeats until sum reaches 1
        sumof = 0
        while (num > 0): #Checks whether the given value is greater than zero(n=100)
            n = num % 10 #Checks the modulus value like 100 mod 10=0
            sumof = sumof + (n * n)#Sum of the square of the digit [0+(0*0)]
            num = num // 10#Floor division 100//10= 10
        num=sumof
    if (num == 1): #if num returns 1 then it is a happy number
        happy.append(number)
        count = count + 1
    else:
        continue #continues the while loop again
print("Happy numbers are:", happy)
print("Happy numbers count:", count)
print()
##SUM OF FIRST AND LAST DIGIT OF AN INTEGER##
n=int(input("Enter any integer:")) #Get any integer as an input
n=str(n) #Converts integer to string for indexing purpose
c=int(n[0]) #To access the first element
d=int(n[-1]) #-1 represents the last element
summ=c+d #Sums up first and last
print("Sum of first and last digit of number:",summ)
print()
##DUPLICATES IN THE LIST###
import itertools #To import itertools files
a1=[1,9,8,2,3,1,9,8]
b2=[57,76,89,43,57,89]
c3=[4,5,6,10,7,6,5,10]
s=set() #creates empty set
duplicate=[] #Creates empty list
for number in itertools.chain(a1,b2,c3): #To iterate through a,b and c list we use itertools.chain()
    if number in s: #To check, if number is already present in set
        duplicate.append(number) #If already available in set, then it is added to duplicates list
    else:
        s.add(number) #Else added to set s
print("Duplicates in the lists are:",duplicate)
print()
##FIRST NON-REPEATING ELEMENT IN LIST###
r=[5,6,99,33,11,7,8,9,22,5,77,8,6]
s=[]
duplicate=[]#App
for number in r:
    if number in s:
        duplicate.append(number) #Append the duplicate values in list 'duplicate'
    else:
        s.append(number) #Append the values in list 's'
newlist=list(s) #List without any duplicates
non=[]
for num in newlist:
    if num not in duplicate: #Check if number is not in duplicate list
        non.append(num) #Then added to non repeating element list 'non'
    else:
        s.append(number) #else added to list 's'
print("First Non Repeating Element in the list:",non[0]) #Prints first non repeating element
print()
##MINIMUM ELEMENT IN RATED AND SORTED LIST##
min=[]
rating=int(input("Enter the total rating elements in list:"))#Total elements of list
for lis in range(rating):
    lis=int(input("Enter rated list of numbers:"))#Each element in list is given by user as input
    min.append(lis) #Each element will be appended to new list 'a'
print(min)
min.sort() #Sorts in ascending order
print("The minimum element in the given list:",min[0])#using indexing to find minimum element
print()
##TRIPLET IN LIST WHOSE SUM=59##
a=[10,20,30,9]
for ii in range(0,4):#loops through i=0 to 3
   for jj in range(1,4):#loops through j=0 to 3
            for kk in range(2, 4):#loops through k=2 to 3
                if (a[ii] + a[jj] + a[kk] == 59): #In each looping it checks sum=59
                    result=(a[ii], a[jj], a[kk]) #prints three values which sums to 59
print("Triplet with sum equal to 59:",result)
print()
## SUB-LIST WITH SUM EQUAL TO ZERO##
aa = [4, 2, -3, 1, 6]
for x in range(0, 5):
    for y in range(x + 1, 6):
        sub = sum(aa[x:y])  #Sums up each sublist
        if (sub == 0): #if sum is zero then it prints the particular sublist
            print("Sublist with sum equal to zero:\n",aa[x:y])