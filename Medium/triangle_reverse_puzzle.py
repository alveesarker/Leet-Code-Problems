n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print(int((i+1) + (j*n) - ((j*(j+1))/2)), end= ' ')
    print()
    