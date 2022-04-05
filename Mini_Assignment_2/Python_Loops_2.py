rows=int(input("Enter number of rows required: "))

for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*(i+1)-1))
for i in range(rows-1):
    print(" "*(i+1)+"*"*(2*(rows-i-1)-1))


print("_________________________________________________________________________________________")



row1 = int(input('Enter number of rows required: '))

for i in range(row1):
        for j in range(row1 - i):
            print(' ', end='')  # printing space required and staying in same line

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == row1 - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # printing new line

print("_________________________________________________________________________________________")

row2 = int(input('Enter number of rows required: '))
for i in range (0,row2):
    for j in range (0,row2):
        if i==0 or j==(row2-1) or i==j:
            print('*', end='')
        else:
            print(end=" ")
    print()

