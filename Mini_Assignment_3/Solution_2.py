list1=[]
list2=[]

n = int(input("Enter number of elements for list1 : "))

# iterating till the range
for i in range(0, n):
    ele = input()
    list1.append(ele)
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]
n1 = int(input("Enter number of elements for list2 : "))
for j in range(0, n1):
    ele1 = input()
    list2.append(ele1)
list3 = [x + y for x in list1 for y in list2]
print(list3)