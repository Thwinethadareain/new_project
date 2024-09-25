nums = [2,5,6,4,7,9]
def mapFunction(num):
    return num*2

    
print(list(map(mapFunction,nums)))
nums = [num *2 for num in nums]
print(nums)