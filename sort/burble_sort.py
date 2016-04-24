def burble_sort(values):

    for i in range(len(values)):
        for j in range(1, len(values) - i):
            if values[j - 1] > values[j]:
                values[j], values[j - 1] = values[j - 1], values[j]

