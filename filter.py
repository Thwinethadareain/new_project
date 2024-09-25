nums =[1,2,3,4,5,6,7,8,9,10]
def even(num):
    return (num%2) == 0

print(list(filter(even,nums)))



#---------------------comprehension way---------------------------#

nums=[num for num in nums if (num%2)==0]
print(nums)

#----------------------traditional for loop way-----------------------#


# evenNumber=[]
# for num in nums:
#     if num%2 == 0:
#         evenNumber.append(num)
# print(evenNumber)        