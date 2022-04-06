# Take the first two values, run the function on them. Then take the result and the next value and
# have a multiplication between them. etc. When no more values are left, return the last result.
import functools
list  = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
output_reduce = functools.reduce(lambda x, y: x * y, list)
print(output_reduce)
print()