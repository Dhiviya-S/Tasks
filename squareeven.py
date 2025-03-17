list1=[3,4,8,2,9,12]

new_list=list(filter(lambda x:x%2==0,list1))
print(new_list)
# for numbers in new_list:
#     list2=numbers*numbers
#     a=str(list2)
#     print(list(a))

jan=[num*num for num in new_list]
print(jan)

# new_list=[num*num for num in filter(lambda x:x%2==0 ,list1)]
# print(new_list)
