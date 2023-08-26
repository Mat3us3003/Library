import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk

class JanelaLogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.geometry('800x800')
        self.style = Style(theme="solar") 
        
                
        self.frame_central = tk.Frame(self.janela)
        self.frame_central.pack(expand=True)


        self.centralizar_elementos()


    def centralizar_elementos(self):
        self.logo_path = "img/usuario.png"
        self.carregar_imagem()
        self.exibir_imagem()
        self.lbl_login = ttk.Label(self.frame_central, text='Login')
        self.lbl_login.grid(row=2, column=0, columnspan=2)
        self.lbl_login.config(font=("algerian", 55, "bold"))  

        self.lbl_usuario = tk.Label(self.frame_central, text='Usuário:')
        self.lbl_usuario.grid(row=3, column=1, sticky="w",pady=20)
        self.lbl_usuario.config(font=("Courier New", 28))  

        self.ent_usuario = tk.Entry(self.frame_central, width=50 )
        self.ent_usuario.grid(row=4, column=1)
        self.ent_usuario.config(font=("Courier New", 28))
       
        self.lbl_senha = tk.Label(self.frame_central, text='Senha:',pady=20)
        self.lbl_senha.grid(row=5, column=1, sticky="w")
        self.lbl_senha.config(font=("Courier New", 28))

        self.ent_senha = tk.Entry(self.frame_central, width=50, show='*')
        self.ent_senha.grid(row=6, column=1)
        self.ent_senha.config(font=("Courier New", 28)) 

        self.btn_logar = tk.Button(self.frame_central, text='Entrar',)
        self.btn_logar.grid(row=8, column=0, columnspan=2,pady=20)
        self.btn_logar.config(font=("algerian", 25))



        self.lbl_adm = tk.Label(self.frame_central, text='Entrar com Admin')
        self.lbl_adm.grid(row=9, column=0, columnspan=2, pady=25)
        self.lbl_adm.config(font=("Monaco", 20))
    def carregar_imagem(self):
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((200, 200)) 

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=1, column=1, columnspan=2) 
        
janela = tk.Tk()
app = JanelaLogin(janela)
janela.mainloop()
