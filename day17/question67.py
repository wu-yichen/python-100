def binary_search(n, left, right, sorted_list):
    pos = int((left + right)/2)
    mid = sorted_list[pos]
    if n == mid:
        return pos

    if n > mid:
        return binary_search(n, pos+1, right, sorted_list)
    if n < mid:
        return binary_search(n, left, pos-1, sorted_list)
    return -1


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(5, 0, len(l)-1, l))
