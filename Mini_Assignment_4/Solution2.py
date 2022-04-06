input_list  = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = input()

    input_list.append(ele)  # adding the element

print(input_list )
#input_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print( sum(map(lambda x: x[0] == 'A', input_list)))
print( sum(map(lambda x: x.lower().count("a"), input_list))-sum(map(lambda x: x[0] == 'A', input_list)))