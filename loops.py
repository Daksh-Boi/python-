# Incrementing values in for loop by 2 instead of 1:
for i in range(1,6,2):
    print(i)

# Getting an infinite for loop:
"""
list = [1]
for i in list:
    print(i)
    list.append(i+1)
"""

# One way to add values to a tuple: using lists
tuple_check = (1,2,[3,4])
tuple_check[2].append(5)
print(tuple_check)
