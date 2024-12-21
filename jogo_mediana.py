import random
from typing import List, Tuple

class JogoMediana:
    def __init__(self):
        self.particoes_usuario = 0
        self.particoes_algoritmo = 0
    
    def encontrar_mediana_das_medianas(self, arr: List[int], k: int) -> Tuple[int, List[int], List[int]]:
        
        if len(arr) <= 5:
            arr_ordenado = sorted(arr)
            pivo = arr_ordenado[k-1]
            esquerda = [x for x in arr if x < pivo]
            direita = [x for x in arr if x > pivo]
            return pivo, esquerda, direita

        grupos = [arr[i:i+5] for i in range(0, len(arr), 5)]
        
        medianas = []
        for grupo in grupos:
            grupo_ordenado = sorted(grupo)
            indice_mediana = (len(grupo) - 1) // 2
            medianas.append(grupo_ordenado[indice_mediana])
        
        if len(medianas) <= 5:
            pivo = sorted(medianas)[len(medianas)//2]
        else:
            pivo, _, _ = self.encontrar_mediana_das_medianas(medianas, len(medianas)//2 + 1)
        
        esquerda = [x for x in arr if x < pivo]
        direita = [x for x in arr if x > pivo]
        
        return pivo, esquerda, direita

    def particionar_com_pivo_usuario(self, arr: List[int], pivo: int) -> Tuple[List[int], List[int]]:
        """Particiona o array ao redor do pivô escolhido pelo usuário"""
        esquerda = [x for x in arr if x < pivo]
        direita = [x for x in arr if x > pivo]
        return esquerda, direita

    def executar_algoritmo(self, arr: List[int], k: int) -> None:
        """Executa o algoritmo da mediana das medianas para comparação"""
        arr_copia = arr.copy()
        
        while True:
            pivo, esquerda, direita = self.encontrar_mediana_das_medianas(arr_copia, k)
            self.particoes_algoritmo += 1
            
            if len(esquerda) == k - 1:
                break
            elif len(esquerda) > k - 1:
                arr_copia = esquerda
            else:
                k = k - len(esquerda) - 1
                arr_copia = direita

    def jogar(self):
        # Gerar array aleatório
        tamanho_array = random.randint(15, 25)
        arr = random.sample(range(1, 101), tamanho_array)
        k = random.randint(1, len(arr))
        
        print("\nBem-vindo ao Jogo de Adivinhação de Pivô para Quickselect!")
        print(f"\nArray: {arr}")
        print(f"Tarefa: Encontre o {k}-ésimo menor elemento")
        
        # Resetar contadores
        self.particoes_usuario = 0
        self.particoes_algoritmo = 0
        
        # Vez do usuário
        arr_atual = arr.copy()
        while True:
            print(f"\nArray atual: {arr_atual}")
            try:
                pivo_usuario = int(input("Escolha seu pivô do array acima: "))
                if pivo_usuario not in arr_atual:
                    print("Por favor, escolha um número do array!")
                    continue
                
                esquerda, direita = self.particionar_com_pivo_usuario(arr_atual, pivo_usuario)
                self.particoes_usuario += 1
                
                if len(esquerda) == k - 1:
                    print(f"\nParabéns! Você encontrou o {k}-ésimo menor elemento: {pivo_usuario}")
                    break
                elif len(esquerda) > k - 1:
                    print("Muitos elementos do lado esquerdo. Vamos continuar com a partição esquerda.")
                    arr_atual = esquerda
                else:
                    print("Muitos elementos do lado direito. Vamos continuar com a partição direita.")
                    k = k - len(esquerda) - 1
                    arr_atual = direita
                    
            except ValueError:
                print("Por favor, digite um número válido!")
        
        # Executar algoritmo para comparação
        print("\nAgora vamos ver como o algoritmo da Mediana das Medianas se sai...")
        self.executar_algoritmo(arr, k)
        
        # Mostrar resultados
        print(f"\nResultados:")
        print(f"Sua solução precisou de {self.particoes_usuario} partições")
        print(f"A Mediana das Medianas precisou de {self.particoes_algoritmo} partições")
        
        if self.particoes_usuario <= self.particoes_algoritmo:
            print("Ótimo trabalho! Você igualou ou superou o algoritmo!")
        else:
            print("O algoritmo foi mais eficiente desta vez. Continue tentando!")

if __name__ == "__main__":
    jogo = JogoMediana()
    while True:
        jogo.jogar()
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            break
    print("\nObrigado por jogar!")
