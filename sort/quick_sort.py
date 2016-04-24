def quick_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2

    left, right = [], []

    for i in range(values):
        if i != mid:
            if values[i] < values[mid]:
                left.append(values[i])
            else:
                right.append(values[i])

    return quick_sort(left) + [values[mid]] + quick_sort(right)

