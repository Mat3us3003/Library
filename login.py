import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
from client import Client
from loginAdm import LoginAdm
from usuario import Janelausuario

class JanelaLogin:
    def __init__(self, janela):
        self.janela = janela
        # self.janela.geometry('800x800')
        self.style = Style(theme="solar") 
        
                
        self.frame_central = tk.Frame(self.janela)
        self.frame_central.pack(expand=True)

        # self.logo_path = "img/biblio.png"
        # self.carregar_imagem()
        # self.exibir_imagem()
        
        
        self.login()
    
    def limpar_grid(self):
        for widget in self.frame_central.winfo_children():
            widget.grid_forget()

    def login(self):
        self.limpar_grid
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

        self.btn_logar = tk.Button(self.frame_central, text='Entrar', command=self.logar)
        self.btn_logar.grid(row=8, column=0, columnspan=2,pady=20)
        self.btn_logar.config(font=("algerian", 25))
        
        self.btn_cadastrar = tk.Button(self.frame_central, text='Cadastrar', command=self.cadastro)
        self.btn_cadastrar.grid(row=9, column=0, columnspan=2,pady=20)
        self.btn_cadastrar.config(font=("algerian", 25))

        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((200, 200))
        
        
    def logar(self):
        if self.ent_usuario.get() == '987654321':
            print(1)
            #self.janela.destroy()
            self.limpar_grid()
            telaAdmin = LoginAdm()
            telaAdmin.iniciarAdmin(self.janela)
        else:
            Janelausuario(self.janela)
            
        print(2)

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=1, column=1, columnspan=2) 
       
        
    def cadastro(self):
        
        self.limpar_grid()
        
        self.lbl_login = ttk.Label(self.frame_central, text='Cadastro')
        self.lbl_login.grid(row=2, column=0, columnspan=2)
        self.lbl_login.config(font=("algerian", 50, "bold"))  
        
        self.lbl_nome = tk.Label(self.frame_central, text='Nome:')
        self.lbl_nome.grid(row=3, column=1, sticky="w",pady=20)
        self.lbl_nome.config(font=("Courier New", 28))
        
        self.ent_nome = tk.Entry(self.frame_central, width=50 )
        self.ent_nome.grid(row=4, column=1)
        self.ent_nome.config(font=("Courier New", 28))

        self.lbl_cpf = tk.Label(self.frame_central, text='CPF:')
        self.lbl_cpf.grid(row=5, column=1, sticky="w",pady=20)
        self.lbl_cpf.config(font=("Courier New", 28))  

        self.ent_cpf = tk.Entry(self.frame_central, width=50 )
        self.ent_cpf.grid(row=6, column=1)
        self.ent_cpf.config(font=("Courier New", 28))
       
        self.lbl_senha = tk.Label(self.frame_central, text='Senha:',pady=20)
        self.lbl_senha.grid(row=7, column=1, sticky="w")
        self.lbl_senha.config(font=("Courier New", 28))

        self.ent_senha = tk.Entry(self.frame_central, width=50, show='*')
        self.ent_senha.grid(row=8, column=1)
        self.ent_senha.config(font=("Courier New", 28)) 
        
        self.frm_botoes = tk.Frame(self.frame_central)
        self.frm_botoes.grid(row=9, column=0, columnspan=2)

        self.btn_cadastrar = tk.Button(self.frm_botoes, text='Entrar',command=self.cadastrar_client)
        self.btn_cadastrar.grid(row=0, column=1, pady=20, padx=10)
        self.btn_cadastrar.config(font=("algerian", 28))

        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar', command=self.login)
        self.btn_voltar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_voltar.config(font=("algerian", 28))

        
    def cadastrar_client(self):
        c = Client(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get())
        self.login()
        
    def confirmar_manager(self):
        if self.ent_nome.get() == '' or self.ent_cpf.get() == '' or self.ent_senha.get() == '':
            messagebox.askokcancel("Erro", "Preencha todos os campos!")
            self.cadastrar_client()
        else:
            c = Client(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get())
            aviso = messagebox.askokcancel("Aviso", "Cadastro feito com sucesso!")
            self.login()
            
        
        
    def carregar_imagem(self):
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((200, 200)) 

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=1, column=1, columnspan=2) 
       
        
        
janela = ttk.Window()
app = JanelaLogin(janela)
janela.mainloop()
