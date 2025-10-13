x = int(input("enter: "))

def function(x):
    low = 0
    high = x
    while low <= high:
        mid = (low + high)/2
        sqr = mid * mid
        if sqr > x:
            high = mid
        elif sqr < x:
            low = mid
        elif sqr == x:
            return int(mid)
            
print(function(x))