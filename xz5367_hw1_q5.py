def fibs(n):
    curr = 1
    next = 1
    for i in range(n):
        yield curr
        curr, next = next, curr + next