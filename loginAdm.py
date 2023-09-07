from menager import Manager
import sqlite3
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
import time
from book import Book
from client import Client

class JanelaLogin:
    def __init__(self, janela):
        self.janela = janela
        # self.janela.geometry('800x800')
        self.style = Style(theme="vapor") 
        
                
        self.frame_central = tk.Frame(self.janela)
        self.frame_central.pack(expand=True)

        # self.logo_path = "img/biblio.png"
        # self.carregar_imagem()
        # self.exibir_imagem()
        
        
        self.login_manager()
    
    def limpar_grid(self):
        for widget in self.frame_central.winfo_children():
            widget.grid_forget()

    #time.sleep(2)

    def login_manager(self):
        self.limpar_grid()
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

        self.btn_logar = tk.Button(self.frame_central, text='Entrar', command=self.cadastro_manager)
        self.btn_logar.grid(row=8, column=0, columnspan=2,pady=20)
        self.btn_logar.config(font=("algerian", 25))
        
        
    def carregar_imagem(self):
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((200, 200)) 

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=1, column=1, columnspan=2) 
       
        
    def cadastro_manager(self):
        
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
        
        self.lbl_ident = tk.Label(self.frame_central, text='Identificador:')
        self.lbl_ident.grid(row=9, column=1, sticky="w",pady=20)
        self.lbl_ident.config(font=("Courier New", 28))  

        self.ent_ident = tk.Entry(self.frame_central, width=50 )
        self.ent_ident.grid(row=10, column=1)
        self.ent_ident.config(font=("Courier New", 28))
        
        self.frm_botoes = tk.Frame(self.frame_central)
        self.frm_botoes.grid(row=11, column=0, columnspan=2)

        self.btn_cadastrar = tk.Button(self.frm_botoes, text='Entrar',command=self.cadastrar_manager)
        self.btn_cadastrar.grid(row=0, column=1, pady=20, padx=10)
        self.btn_cadastrar.config(font=("algerian", 28))

        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar', command=self.login_manager)
        self.btn_voltar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_voltar.config(font=("algerian", 28))
        
    
    def cadastro_book(self):
        
        self.limpar_grid() 
        
        self.lbl_titulo = tk.Label(self.frame_central, text='Título:')
        self.lbl_titulo.grid(row=3, column=1, sticky="w",pady=20)
        self.lbl_titulo.config(font=("Courier New", 28))
        
        self.ent_titulo = tk.Entry(self.frame_central, width=50 )
        self.ent_titulo.grid(row=4, column=1)
        self.ent_titulo.config(font=("Courier New", 28))

        self.lbl_author = tk.Label(self.frame_central, text='Autor:')
        self.lbl_author.grid(row=5, column=1, sticky="w",pady=20)
        self.lbl_author.config(font=("Courier New", 28))  

        self.ent_author = tk.Entry(self.frame_central, width=50 )
        self.ent_author.grid(row=6, column=1)
        self.ent_author.config(font=("Courier New", 28))
       
        self.lbl_gender = tk.Label(self.frame_central, text='Gênero:',pady=20)
        self.lbl_gender.grid(row=7, column=1, sticky="w")
        self.lbl_gender.config(font=("Courier New", 28))

        lista = ['Romance', 'Aventura', 'Terror', 'Comédia', 'Infantil']
        self.cbx_gender = ttk.Combobox(self.frame_central, values=lista, state='readonly')
        self.cbx_gender.config(font=("Courier New", 28)) 
        self.cbx_gender.grid(row=8, column=1, sticky="w")
        
        self.frm_botoes = tk.Frame(self.frame_central)
        self.frm_botoes.grid(row=11, column=0, columnspan=2)

        self.btn_cadastrar_book = tk.Button(self.frm_botoes, text='Cadastrar Livro', command=self.confirmar_book)
        self.btn_cadastrar_book.grid(row=0, column=1, pady=20, padx=10)
        self.btn_cadastrar_book.config(font=("algerian", 28))

        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar', command=self.login_manager)
        self.btn_voltar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_voltar.config(font=("algerian", 28))

        
    def cadastrar_manager(self):
        print(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get(), self.ent_ident.get())
        c = Manager(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get(), self.ent_ident.get())
        self.login_manager()
        
    def confirmar_book(self):
        b = Book(self.ent_titulo.get(), self.ent_author.get(), self.cbx_gender.get())
        self.cadastro_book()
        
        
    def carregar_imagem(self):
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((200, 200)) 

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=1, column=1, columnspan=2) 
        
    def rent(self):
        self.limpar_grid()
        colunas = ('id', 'date_start', 'date_end', 'status_rent', 'requester_rent')
        self.tvw = ttk.Treeview(self.frame_central, columns=colunas, height=5, show='headings')
        self.tvw.grid(row=0,column=0)
        #Cabeçalho
        self.tvw.heading('id', text='ID')
        self.tvw.heading('date_start', text='Início')
        self.tvw.heading('date_end', text='Final')
        self.tvw.heading('status_rent', text='Status')
        self.tvw.heading('requester_rent', text='Solicitante')
        #Colunas
        self.tvw.column('id', minwidth=30, width=30)
        self.tvw.column('date_start', minwidth=100, width=200)
        self.tvw.column('date_end', minwidth=100, width=200)
        self.tvw.column('status_rent', minwidth=200, width=200)
        self.tvw.column('requester_rent', minwidth=200, width=200)
        #Linhas
        self.atualizar_treeview()
        # #Barra de rolagem
        # scb = ttk.Scrollbar(self.janela, orient=tk.VERTICAL,command=self.tvw.yview)
        # scb.grid(row=0, column=1, sticky='ns')
        # self.tvw.config(yscrollcommand=scb.set)
        
        self.frm_botoes = tk.Frame(self.frame_central)
        self.frm_botoes.grid(row=1, column=0)
        
        self.btn_aceitar = tk.Button(self.frm_botoes, text='Aceitar', command=self.aceitar)
        self.btn_aceitar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_aceitar.config(font=("algerian", 20))
        
        self.btn_negar = tk.Button(self.frm_botoes, text='Negar', command=self.negar)
        self.btn_negar.grid(row=1, column=0, pady=20, padx=10)
        self.btn_negar.config(font=("algerian", 20))
        
        self.btn_devolvido = tk.Button(self.frm_botoes, text='Devolvido', command=self.devolvido)
        self.btn_devolvido.grid(row=2, column=0, pady=20, padx=10)
        self.btn_devolvido.config(font=("algerian", 20))
        
        
    def atualizar_treeview(self):
        items = self.tvw.get_children() #limpa o componente treeview antes de preencher com o conteúdo do BD
        for i in items:
            self.tvw.delete(i)
        sql_listar_contas = 'SELECT r.id_rent, r.date_start, r.date_end, r.status_rent, c.id_client FROM rent r, client c WHERE r.requester_rent=c.id_client;'
        dados = self.listar(sql_listar_contas)
        for linha in dados:
            self.tvw.insert('', tk.END, values=linha)
            
    def listar(self, sql):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall() 
        banco.close()
        return resultado
    
    def aceitar(self):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE rent SET status_rent='Aprovado' WHERE id_rent=1")
        banco.commit()
        banco.close()
        self.atualizar_treeview()
    
    def negar(self):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE rent SET status_rent='Negado' WHERE id_rent=1")
        banco.commit()
        banco.close()
        self.atualizar_treeview()
        
    def devolvido(self):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE rent SET status_rent='Devolvido' WHERE id_rent=1")
        banco.commit()
        banco.close()
        self.atualizar_treeview()
       
        
        
janela = tk.Tk()
app = JanelaLogin(janela)
janela.mainloop()
