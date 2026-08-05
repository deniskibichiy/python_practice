"""nums = [12, 8, 21, 3, 16]
new_nums = []
for num in nums:
    new_nums.append(num+1)
print(new_nums)
"""
nums2 = [12, 8, 21, 3, 16]
new_nums2 = [num + 1 for num in nums2]
#print(new_nums2)

pairs_1 = []
for num1 in range(0,2):
    for num2 in range(6,8):
        pairs_1.append((num1, num2))
#print(pairs_1)

pairs_2 = [(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
#print(pairs_2)

# Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.

sqd_values = [i*i for i in range(0,9)]
print(sqd_values)