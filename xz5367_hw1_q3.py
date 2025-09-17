def square_sum(n):
    sum = 0
    for i in range(1, n):
        sum += i**2
    return sum

def square_sum_odd(n):
    sum = 0
    for i in range(1, n, 2):
        sum += i**2
    return sum

n = 5

# List comprehension form for square_sum()
sum([i**2 for i in range(1, n)])

# List comprehension form for square_sum_odd()
sum([i**2 for i in range(1, n, 2)])