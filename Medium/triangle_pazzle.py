n = int(input("Enter the number: "))

for i in range(n):
    for j in range(i + 1):
        print(int((j+1) + ((i-j)*n) - (((i-j) * ((i-j) - 1)) / 2)), end=" ")
    print()