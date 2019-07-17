def summa(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + summa(arr)


print(summa([5, 6, 4, 15]))
