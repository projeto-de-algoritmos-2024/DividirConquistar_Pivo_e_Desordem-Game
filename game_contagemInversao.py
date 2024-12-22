def merge_and_count(left, right):
    merged = []
    i = j = 0
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # Todos os elementos restantes em 'left' são maiores que right[j]
            inversions += len(left) - i

    # Adiciona os elementos restantes de 'left' e 'right'
    merged.extend(left[i:])
    merged.extend(right[j:])

    return inversions, merged

