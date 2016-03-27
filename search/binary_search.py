
def recursive_binary_search(values, searched_value, min, max):

    if max < min:
        return None

    mid = (max + min) // 2

    if searched_value > values[mid]:
        return recursive_binary_search(values, searched_value, mid + 1, max)

    if searched_value < values[mid]:
        return recursive_binary_search(values, searched_value, min, mid - 1)

    return mid

def interactive_binary_search(values, searched_value, min, max):

    while(max >= min):

        mid = (max + min) // 2

        if values[mid] == searched_value:
            return mid

        if searched_value > values[mid]:
            min = mid + 1
        else:
            max = mid - 1

    return None