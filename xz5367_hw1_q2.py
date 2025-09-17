import copy

def shift(lst, k, dir = "left"):
    if (dir == "right"):
        k = -k
    lst_copy = copy.copy(lst)
    n = len(lst)
    for i in range(n):
        lst[(i - k) % n] = lst_copy[i]
    return lst

def main():
    lst = [1, 2, 3, 4, 5, 6]
    print(shift(lst, 2))

