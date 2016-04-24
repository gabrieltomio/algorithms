def quick_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2

    left, right = [], []

    for value in values[:mid] + values[mid + 1:]:
        if value < values[mid]:
            left.append(value)
        else:
            right.append(value)

    return quick_sort(left) + [values[mid]] + quick_sort(right)

