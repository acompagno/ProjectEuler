import random
def build(nums):
    num = 0
    for i in range (0,10):
        temp = nums[i] * (10**(9-i))
        num = num + temp
    return num

nums = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
random.shuffle(nums)
print(build(nums))
