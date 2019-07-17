def summa(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + summa(arr)


print(summa([5, 6, 4, 15]))


def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])
print(count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))