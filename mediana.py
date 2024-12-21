from typing import List, Tuple

def encontrar_mediana_das_medianas(arr: List[int], k: int) -> Tuple[int, List[int], List[int]]:

    if len(arr) <= 5:
        arr_ordenado = sorted(arr)
        pivo = arr_ordenado[k-1]
        esquerda = [x for x in arr if x < pivo]
        direita = [x for x in arr if x > pivo]
        return pivo, esquerda, direita

    # Passo 1: Dividir array em grupos de 5
    grupos = [arr[i:i+5] for i in range(0, len(arr), 5)]
    
    # Passo 2: Encontrar mediana de cada grupo
    medianas = []
    for grupo in grupos:
        grupo_ordenado = sorted(grupo)
        indice_mediana = (len(grupo) - 1) // 2
        medianas.append(grupo_ordenado[indice_mediana])
    
    # Passo 3: Encontrar recursivamente a mediana das medianas
    if len(medianas) <= 5:
        pivo = sorted(medianas)[len(medianas)//2]
    else:
        pivo, _, _ = encontrar_mediana_das_medianas(medianas, len(medianas)//2 + 1)
    
    # Passo 4: Particionar ao redor do pivô (mediana)
    esquerda = [x for x in arr if x < pivo]
    direita = [x for x in arr if x > pivo]
    
    return pivo, esquerda, direita

# Teste simples do algoritmo
if __name__ == "__main__":

    arr_teste = [1, 5, 2, 8, 3, 9, 7, 6, 4]
    k = 5  # Procurando o 5º menor elemento
    pivo, esquerda, direita = encontrar_mediana_das_medianas(arr_teste, k)
    print(f"Array original: {arr_teste}")
    print(f"Procurando o {k}º menor elemento")
    print(f"Pivô escolhido: {pivo}")
    print(f"Elementos menores: {esquerda}")
    print(f"Elementos maiores: {direita}")
