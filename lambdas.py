# def add(n1,n2):
#     return n1+n2
# print(add(4,5))

# add=lambda n1,n2: n1+n2
# print(add(4,5))

nums = [1,2,3,4,5,6,7,8]

# nums=[num for num in nums if (num%2)==0]
# print(nums)


print(list(filter(lambda num: num%2 == 0,nums)))
print(list(map(lambda num: num*2,nums)))