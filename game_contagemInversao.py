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

def sort_and_count(arr):
    # Caso base: lista com um único elemento
    if len(arr) <= 1:
        return 0, arr

    # Divide a lista ao meio
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conta as inversões nas duas metades
    left_inversions, sorted_left = sort_and_count(left)
    right_inversions, sorted_right = sort_and_count(right)

    # Conta as inversões entre as duas metades e as une
    split_inversions, sorted_arr = merge_and_count(sorted_left, sorted_right)

    # Soma todas as inversões
    total_inversions = left_inversions + right_inversions + split_inversions

    return total_inversions, sorted_arr
