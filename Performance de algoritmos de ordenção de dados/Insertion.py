def insertion_sort(arrayValores):
    for p in range(0, len(arrayValores)):
        current_element = arrayValores[p]

        while p > 0 and arrayValores[p - 1] > current_element:
            arrayValores[p] = arrayValores[p - 1]
            p -= 1

        arrayValores[p] = current_element


