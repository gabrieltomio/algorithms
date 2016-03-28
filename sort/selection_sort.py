def selection_sort(values):

    length = len(values)

    for i in range(length):
        smaller = i
        for j in range(i + 1, length):
            if values[smaller] > values[j]:
                smaller = j

        tmp = values[i]
        values[i] = values[smaller]
        values[smaller] = tmp