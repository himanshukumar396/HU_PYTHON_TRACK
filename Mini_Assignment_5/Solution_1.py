# Convert a number to positive if it's negative in the list. Only pass those that are converted
# from negative to positive to the new list.


input_list  = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    input_list.append(ele)  # adding the element

print(input_list )

output_filter = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, input_list)))
print(output_filter)
print()

