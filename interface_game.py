import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jogo_mediana import JogoMediana

class MedianGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Mediana")
        self.root.geometry("800x600")
        
        # Instância do jogo
        self.jogo = JogoMediana()
        self.arr_atual = []
        self.k = 0

        self.style = ttk.Style()
        self.style.configure('TButton', padding=5, font=('Helvetica', 10))
        self.style.configure('TLabel', font=('Helvetica', 12))
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.title_label = ttk.Label(
            self.main_frame, 
            text="Jogo da Mediana",
            font=('Helvetica', 16, 'bold')
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Frame para array atual
        self.array_frame = ttk.LabelFrame(self.main_frame, text="Array Atual", padding="10")
        self.array_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.array_label = ttk.Label(
            self.array_frame,
            text="",
            wraplength=700
        )
        self.array_label.grid(row=0, column=0, pady=5)
        
        # Frame para entrada do pivô
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Escolha seu pivô", padding="10")
        self.input_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.number_entry = ttk.Entry(self.input_frame, width=20)
        self.number_entry.grid(row=0, column=0, padx=5)
        
        self.submit_button = ttk.Button(
            self.input_frame, 
            text="Enviar Pivô",
            command=self.processar_pivo
        )
        self.submit_button.grid(row=0, column=1, padx=5)

        self.info_frame = ttk.LabelFrame(self.main_frame, text="Informações do Jogo", padding="10")
        self.info_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.info_label = ttk.Label(
            self.info_frame, 
            text="Clique em 'Novo Jogo' para começar!",
            wraplength=700
        )
        self.info_label.grid(row=0, column=0, pady=5)
        
        # Estatísticas
        self.stats_frame = ttk.LabelFrame(self.main_frame, text="Estatísticas", padding="10")
        self.stats_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.stats_label = ttk.Label(
            self.stats_frame,
            text="Partições realizadas: 0",
            wraplength=700
        )
        self.stats_label.grid(row=0, column=0, pady=5)
        
        # Botão para iniciar novo jogo
        self.new_game_button = ttk.Button(
            self.main_frame,
            text="Novo Jogo",
            command=self.novo_jogo
        )
        self.new_game_button.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Configurar expansão de grid
        for i in range(2):
            self.main_frame.columnconfigure(i, weight=1)
            
    def novo_jogo(self):
        # Gerar array aleatório
        tamanho_array = random.randint(15, 25)
        self.arr_atual = random.sample(range(1, 101), tamanho_array)
        self.k = random.randint(1, len(self.arr_atual))
        
        # Resetar contadores
        self.jogo.particoes_usuario = 0
        
        # Atualizar interface
        self.array_label.config(text=f"Array: {self.arr_atual}")
        self.info_label.config(text=f"Encontre o {self.k}-ésimo menor elemento")
        self.stats_label.config(text="Partições realizadas: 0")
        self.number_entry.delete(0, tk.END)
        
    def processar_pivo(self):
        try:
            pivo = int(self.number_entry.get())
            if pivo not in self.arr_atual:
                messagebox.showwarning("Erro", "Por favor, escolha um número do array!")
                return
            
            esquerda, direita = self.jogo.particionar_com_pivo_usuario(self.arr_atual, pivo)
            self.jogo.particoes_usuario += 1
            
            # Atualizar estatísticas
            self.stats_label.config(text=f"Partições realizadas: {self.jogo.particoes_usuario}")
            
            if len(esquerda) == self.k - 1:
                messagebox.showinfo("Parabéns!", 
                    f"Você encontrou o {self.k}-ésimo menor elemento: {pivo}\n" +
                    f"Número de partições realizadas: {self.jogo.particoes_usuario}")
                self.novo_jogo()
            elif len(esquerda) > self.k - 1:
                self.info_label.config(text="Muitos elementos do lado esquerdo. Vamos continuar com a partição esquerda.")
                self.arr_atual = esquerda
                self.array_label.config(text=f"Array: {self.arr_atual}")
            else:
                self.info_label.config(text="Muitos elementos do lado direito. Vamos continuar com a partição direita.")
                self.k = self.k - len(esquerda) - 1
                self.arr_atual = direita
                self.array_label.config(text=f"Array: {self.arr_atual}")
                
            self.number_entry.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MedianGameGUI(root)
    root.mainloop()
