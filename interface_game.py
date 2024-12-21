import tkinter as tk
from tkinter import ttk, messagebox

class MedianGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Mediana")
        self.root.geometry("600x400")
        
        # Configuração do estilo
        self.style = ttk.Style()
        self.style.configure('TButton', padding=5, font=('Helvetica', 10))
        self.style.configure('TLabel', font=('Helvetica', 12))
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        self.title_label = ttk.Label(
            self.main_frame, 
            text="Bem-vindo ao Jogo da Mediana!",
            font=('Helvetica', 16, 'bold')
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Frame para entrada de números
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Digite um número", padding="10")
        self.input_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.number_entry = ttk.Entry(self.input_frame, width=20)
        self.number_entry.grid(row=0, column=0, padx=5)
        
        self.submit_button = ttk.Button(
            self.input_frame, 
            text="Enviar",
            command=self.placeholder_submit
        )
        self.submit_button.grid(row=0, column=1, padx=5)
        
        # Frame para informações do jogo
        self.info_frame = ttk.LabelFrame(self.main_frame, text="Informações do Jogo", padding="10")
        self.info_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.info_label = ttk.Label(
            self.info_frame, 
            text="Aguardando início do jogo...",
            wraplength=400
        )
        self.info_label.grid(row=0, column=0, pady=5)
        
        # Botão para iniciar novo jogo
        self.new_game_button = ttk.Button(
            self.main_frame,
            text="Novo Jogo",
            command=self.placeholder_new_game
        )
        self.new_game_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Configurar expansão de grid
        for i in range(2):
            self.main_frame.columnconfigure(i, weight=1)
        
    def placeholder_submit(self):
        messagebox.showinfo("Informação", "Função de envio será implementada em breve!")
        
    def placeholder_new_game(self):
        messagebox.showinfo("Informação", "Novo jogo será implementado em breve!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MedianGameGUI(root)
    root.mainloop()
