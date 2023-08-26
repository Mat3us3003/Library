import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk

class JanelaPrincipal:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry('800x800')
        self.style = Style(theme="solar")

        self.frame_central = tk.Frame(self.janela)
        self.frame_central.pack(expand=True)

        self.centralizar_elementos()

    def centralizar_elementos(self):
        self.logo_path = "img/biblio.png"
        self.carregar_imagem()
        self.exibir_imagem()

        self.lbl_texto = ttk.Label(self.frame_central, text='Library')
        self.lbl_texto.grid(row=3, column=5, columnspan=2)
        self.lbl_texto.config(font=("algerian", 55, "bold"))

        self.lbl_texto1 = ttk.Label(self.frame_central, text=' Bem-vindo à nossa biblioteca')
        self.lbl_texto1.grid(row=4, column=5, columnspan=2)
        self.lbl_texto1.config(font=("Courier New", 18))

        self.lbl_texto2 = ttk.Label(self.frame_central, text='Descubra mundos entre as páginas, aqui a busca pelo conhecimento ganha vida.')
        self.lbl_texto2.grid(row=5, column=5, columnspan=2)
        self.lbl_texto2.config(font=("Courier New", 18))

    def carregar_imagem(self):
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((500, 500)) 

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=2, column=5, columnspan=2) 

janela = tk.Tk()
app = JanelaPrincipal(janela)
janela.mainloop()
