def selection_sort(arrayValores):
    for index in range(0, len(arrayValores)):
        min_index = index

        for right in range(index + 1, len(arrayValores)):
            if arrayValores[right] < arrayValores[min_index]:
                min_index = right

        arrayValores[index], arrayValores[min_index] = arrayValores[min_index], arrayValores[index]
    return arrayValores