import math

def permutations(array):

    if len(array) == 1:
        return [array]

    first_element = array[0]
    other_elements = array[1:]

    result = []

    for values_permuted in permutations(other_elements):
        for i in range(len(other_elements) + 1):
            result += [ values_permuted[:i] + [first_element] + values_permuted[i:] ]

    return result

def get_permutation(line, array):
    array_copy = []
    array_copy.extend(array)

    result = []

    for j in range(len(array), 0, -1):
        denominador = math.factorial(j - 1)
        posicao = line // denominador

        result.append(array_copy[posicao])
        del array_copy[posicao]

        line %= denominador

    return result

def iterative_permutations(array):

    result = []
    for i in range(math.factorial(len(array))):
        result.append(get_permutation(i, array))
    return result
