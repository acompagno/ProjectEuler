import random

def build(nums):
        num = 0
        for i in range (0,10):
                temp = nums[i] * (10**(9-i))
                num = num + temp
        return num

def unbuild(n):
        temp_str = str(n)
        q=[]
        if len(temp_str) == 9:
                q.append(0)
                for i in range (1,10):
                        temp = int(temp_str[i-1]) 
                        q.append(temp)
                q.sort()
                return q
        if len(temp_str) == 10:
                for i in range (0,10):
                        temp = int(temp_str[i]) 
                        q.append(temp)
                q.sort()
                return q




initial = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
nums = []
length = 999360
temp_num = []
x=2783014569
while length <1000000:
        temp_num = unbuild(x)
        if temp_num == initial:
                nums.append(x)
                length = length +1
        x=x+1


print(nums)

