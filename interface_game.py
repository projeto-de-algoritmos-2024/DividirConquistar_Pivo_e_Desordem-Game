import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jogo_mediana import JogoMediana

class MedianGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Mediana")
        self.root.geometry("1000x800")
        
        # Cores e estilos
        self.cores = {
            'bg_principal': '#f0f0f0',
            'bg_frame': '#ffffff',
            'destaque': '#4a90e2',
            'texto': '#333333',
            'sucesso': '#2ecc71',
            'erro': '#e74c3c'
        }
        
        # Configurar tema
        self.root.configure(bg=self.cores['bg_principal'])
        self.style = ttk.Style()
        self.style.configure('Frame.TFrame', background=self.cores['bg_frame'])
        self.style.configure('TButton', padding=10, font=('Helvetica', 11))
        self.style.configure('TLabel', font=('Helvetica', 11), background=self.cores['bg_frame'])
        self.style.configure('Title.TLabel', font=('Helvetica', 24, 'bold'))
        self.style.configure('Subtitle.TLabel', font=('Helvetica', 14))
        
        # Instância do jogo e variáveis
        self.jogo = JogoMediana()
        self.arr_atual = []
        self.k = 0
        self.historico_particoes = []
        
        self.criar_interface()
        
    def criar_interface(self):
        # Container principal
        self.main_container = ttk.Frame(self.root, padding="20", style='Frame.TFrame')
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(
            self.main_container,
            text="Jogo da Mediana",
            style='Title.TLabel'
        ).grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        ttk.Label(
            self.main_container,
            text="Encontre o k-ésimo elemento usando o mínimo de partições possível!",
            style='Subtitle.TLabel'
        ).grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Frame esquerdo - Jogo
        self.game_frame = ttk.LabelFrame(
            self.main_container,
            text="Área do Jogo",
            padding="15"
        )
        self.game_frame.grid(row=2, column=0, padx=(0, 10), sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Array atual
        self.array_label = ttk.Label(
            self.game_frame,
            text="",
            wraplength=400
        )
        self.array_label.grid(row=0, column=0, pady=(0, 10))
        
        # Entrada do pivô
        ttk.Label(
            self.game_frame,
            text="Escolha seu pivô:"
        ).grid(row=1, column=0, pady=(10, 5))
        
        self.number_entry = ttk.Entry(self.game_frame, width=20)
        self.number_entry.grid(row=2, column=0, pady=(0, 10))
        
        self.submit_button = ttk.Button(
            self.game_frame,
            text="Enviar Pivô",
            command=self.processar_pivo
        )
        self.submit_button.grid(row=3, column=0, pady=(0, 10))

        self.info_label = ttk.Label(
            self.game_frame,
            text="Clique em 'Novo Jogo' para começar!",
            wraplength=400
        )
        self.info_label.grid(row=4, column=0, pady=10)
        
        # Frame direito - Estatísticas e Histórico
        self.stats_frame = ttk.LabelFrame(
            self.main_container,
            text="Estatísticas e Histórico",
            padding="15"
        )
        self.stats_frame.grid(row=2, column=1, padx=(10, 0), sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Estatísticas
        self.stats_label = ttk.Label(
            self.stats_frame,
            text="Partições realizadas: 0\nMelhor possível (Mediana das Medianas): -",
            wraplength=400
        )
        self.stats_label.grid(row=0, column=0, pady=(0, 10))
        
        # Histórico de partições
        ttk.Label(
            self.stats_frame,
            text="Histórico de Partições:",
            font=('Helvetica', 11, 'bold')
        ).grid(row=1, column=0, pady=(10, 5))
        
        self.historico_text = tk.Text(
            self.stats_frame,
            width=40,
            height=15,
            wrap=tk.WORD,
            font=('Helvetica', 10)
        )
        self.historico_text.grid(row=2, column=0, pady=(0, 10))

        self.buttons_frame = ttk.Frame(self.main_container)
        self.buttons_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.new_game_button = ttk.Button(
            self.buttons_frame,
            text="Novo Jogo",
            command=self.novo_jogo
        )
        self.new_game_button.grid(row=0, column=0, padx=5)
        
        self.solution_button = ttk.Button(
            self.buttons_frame,
            text="Ver Solução do Algoritmo",
            command=self.mostrar_solucao_algoritmo
        )
        self.solution_button.grid(row=0, column=1, padx=5)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.columnconfigure(1, weight=1)
        
    def novo_jogo(self):
        # Gerar array aleatório
        tamanho_array = random.randint(15, 25)
        self.arr_atual = random.sample(range(1, 101), tamanho_array)
        self.k = random.randint(1, len(self.arr_atual))
        
        # Resetar contadores e histórico
        self.jogo.particoes_usuario = 0
        self.historico_particoes = []
        
        # Calcular solução do algoritmo
        arr_temp = self.arr_atual.copy()
        self.jogo.particoes_algoritmo = 0
        pivo, _, _ = self.jogo.encontrar_mediana_das_medianas(arr_temp, self.k)
        particoes_algoritmo = self.jogo.particoes_algoritmo
        
        # Atualizar interface
        self.array_label.config(
            text=f"Array Atual: {self.arr_atual}\n\nEncontre o {self.k}-ésimo menor elemento"
        )
        self.info_label.config(text="Escolha um pivô do array acima")
        self.stats_label.config(
            text=f"Partições realizadas: 0\nMelhor possível (Mediana das Medianas): {particoes_algoritmo}"
        )
        self.historico_text.delete(1.0, tk.END)
        self.number_entry.delete(0, tk.END)
        
    def adicionar_ao_historico(self, pivo: int, resultado: str):
        self.historico_particoes.append(f"Pivô: {pivo} - {resultado}")
        self.historico_text.delete(1.0, tk.END)
        for entrada in self.historico_particoes:
            self.historico_text.insert(tk.END, entrada + "\n")
        self.historico_text.see(tk.END)
        
    def processar_pivo(self):
        if not self.arr_atual:
            messagebox.showwarning("Aviso", "Inicie um novo jogo primeiro!")
            return
            
        try:
            pivo = int(self.number_entry.get())
            if pivo not in self.arr_atual:
                messagebox.showwarning("Erro", "Por favor, escolha um número do array!")
                return
            
            esquerda, direita = self.jogo.particionar_com_pivo_usuario(self.arr_atual, pivo)
            self.jogo.particoes_usuario += 1
            
            # Atualizar estatísticas
            self.stats_label.config(
                text=f"Partições realizadas: {self.jogo.particoes_usuario}\n" +
                     f"Melhor possível (Mediana das Medianas): {self.jogo.particoes_algoritmo}"
            )
            
            if len(esquerda) == self.k - 1:
                self.adicionar_ao_historico(pivo, "CORRETO! ✓")
                messagebox.showinfo("Parabéns!", 
                    f"Você encontrou o {self.k}-ésimo menor elemento: {pivo}\n" +
                    f"Número de partições realizadas: {self.jogo.particoes_usuario}\n" +
                    f"Algoritmo da Mediana das Medianas: {self.jogo.particoes_algoritmo} partições")
            elif len(esquerda) > self.k - 1:
                self.adicionar_ao_historico(pivo, "Muitos elementos à esquerda →")
                self.info_label.config(text="Muitos elementos do lado esquerdo. Vamos continuar com a partição esquerda.")
                self.arr_atual = esquerda
            else:
                self.adicionar_ao_historico(pivo, "Muitos elementos à direita ←")
                self.info_label.config(text="Muitos elementos do lado direito. Vamos continuar com a partição direita.")
                self.k = self.k - len(esquerda) - 1
                self.arr_atual = direita
                
            self.array_label.config(
                text=f"Array Atual: {self.arr_atual}\n\nEncontre o {self.k}-ésimo menor elemento"
            )
            self.number_entry.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido!")
            
    def mostrar_solucao_algoritmo(self):
        if not self.arr_atual:
            messagebox.showwarning("Aviso", "Inicie um novo jogo primeiro!")
            return
            
        # Executar o algoritmo da mediana das medianas
        arr_temp = self.arr_atual.copy()
        k_temp = self.k
        passos = []
        
        while True:
            pivo, esquerda, direita = self.jogo.encontrar_mediana_das_medianas(arr_temp, k_temp)
            passos.append(f"Pivô escolhido: {pivo}")
            
            if len(esquerda) == k_temp - 1:
                passos.append(f"Elemento encontrado: {pivo}")
                break
            elif len(esquerda) > k_temp - 1:
                passos.append("Continuando com a partição esquerda")
                arr_temp = esquerda
            else:
                passos.append("Continuando com a partição direita")
                k_temp = k_temp - len(esquerda) - 1
                arr_temp = direita
        
        # Mostrar os passos em uma nova janela
        solucao_window = tk.Toplevel(self.root)
        solucao_window.title("Solução do Algoritmo")
        solucao_window.geometry("500x400")
        
        ttk.Label(
            solucao_window,
            text="Passos do Algoritmo da Mediana das Medianas",
            font=('Helvetica', 14, 'bold')
        ).pack(pady=10)
        
        text_widget = tk.Text(
            solucao_window,
            wrap=tk.WORD,
            width=50,
            height=15,
            font=('Helvetica', 11)
        )
        text_widget.pack(padx=20, pady=10)
        
        for i, passo in enumerate(passos, 1):
            text_widget.insert(tk.END, f"{i}. {passo}\n")
        
        text_widget.config(state='disabled')
        
        ttk.Button(
            solucao_window,
            text="Fechar",
            command=solucao_window.destroy
        ).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MedianGameGUI(root)
    root.mainloop()
