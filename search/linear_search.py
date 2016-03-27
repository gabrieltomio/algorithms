def linear_search(values, searched_value):

    for index in range(len(values)):
        if values[index] == searched_value:
            return index
    return None
