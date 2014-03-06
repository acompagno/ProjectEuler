import math

sum_squares = 0
sum_sum = 0
for i in range(1,101):
    sum_squares = sum_squares + math.pow(i,2)
    sum_sum = sum_sum + i

power_sum = math.pow(sum_sum,2)
diff = power_sum - sum_squares
print(diff)
