import datetime
from tkinter import Menu, messagebox
from menager import Manager
import sqlite3
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
from tkinter import ttk
from ttkbootstrap.window import Window
from book import Book
from client import Client
from rent import Rent

class LoginAdm:
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
        
        self.cpf_user = self.ent_usuario.get()

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
            self.inicio()
            #self.janela.destroy()
            # self.limpar_grid()
            # telaAdmin = LoginAdm()
            # telaAdmin.iniciarAdmin(self.janela)
        else:
            self.usuario()
            

       
        
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

        self.btn_cadastrar = tk.Button(self.frm_botoes, text='Entrar',command=self.confirmar_client)
        self.btn_cadastrar.grid(row=0, column=1, pady=20, padx=10)
        self.btn_cadastrar.config(font=("algerian", 28))

        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar', command=self.login)
        self.btn_voltar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_voltar.config(font=("algerian", 28))


        
    def confirmar_client(self):
        if self.ent_nome.get() == '' or self.ent_cpf.get() == '' or self.ent_senha.get() == '':
            messagebox.askokcancel("Erro", "Preencha todos os campos!")
            self.cadastrar_client()
        else:
            c = Client(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get())
            aviso = messagebox.askokcancel("Aviso", "Cadastro feito com sucesso!")
            self.login()
            
        
       
        
    
        
        
        
        #######################################################################################################
        #self.janela = ttkbootstrap.Window()
        # self.janela = janela
        
        # self.logo_path = "img/biblio.png"
        # self.carregar_imagem()
        # self.exibir_imagem()
        #self.inicio()
        
    # def iniciarAdmin(self, janela):
    #     self.janela = janela
    #     self.frame_central = tk.Frame(self.janela)
    #     self.frame_central.pack(expand=True)
    #     self.inicio()
        
            
    def limpar_grid(self):
        for widget in self.frame_central.winfo_children():
            widget.grid_forget()
            
    def mudar_tema(self):
        # Obter o tema selecionado e aplicá-lo
        tema = self.tema_var.get()
        self.style.theme_use(tema)
        
        
    def carregar_imagem(self):
        self.logo = Image.open(self.logo_path)
        self.logo = self.logo.resize((200, 200)) 

    def exibir_imagem(self):
        self.logo_tk = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_central, image=self.logo_tk)
        self.label_logo.grid(row=1, column=1, columnspan=2)
        
    
    def carregar_imagens(self):
        self.images_tk = []
        for logos in self.logos:
            image = Image.open(logos)
            image = image.resize((350, 350))
            self.images_tk.append(ImageTk.PhotoImage(image))

    def exibir_imagens(self, frame):
        for i, image_tk in enumerate(self.images_tk):
            label = tk.Label(frame, image=image_tk)
            label.grid(row=0, column=i, padx=15) 

    
    def inicio(self):
        
        # self.janela.geometry('800x800')
        self.style = Style(theme="vapor") 
        
        #self.janela = ttk.Window()
        
        self.limpar_grid()
        # Criar um frame para imagens e botões com espaçamento pady e padx
        frame_conteudo = tk.Frame(self.frame_central, pady=150, padx=20)
        frame_conteudo.grid(row=0, column=0)

        # Load and display the images
        self.logos = ["img/agendaa.png", "img/devolucao.png", "img/R.png"]
        self.carregar_imagens()
        self.exibir_imagens(frame_conteudo)

        # Criar botões dentro do mesmo frame
        self.btn_agendar = tk.Button(frame_conteudo, text='Cadastrar livro', font=("algerian", 30), command=self.cadastro_book)
        self.btn_agendar.grid(row=1, column=0, padx=10)

        self.btn_devolver = tk.Button(frame_conteudo, text='Requisições', font=("algerian", 30), command=self.rent)
        self.btn_devolver.grid(row=1, column=1, padx=10)

        self.btn_prorrogar = tk.Button(frame_conteudo, text='Prorrogar', font=("algerian", 30))
        self.btn_prorrogar.grid(row=1, column=2, pady=10)

        # Criar o menu principal
        menu_principal = Menu(self.janela)
        self.janela.config(menu=menu_principal)

        # Criar um submenu "Temas"
        submenu_temas = Menu(menu_principal, tearoff=0)
        
         # Adicionar um item de menu "Inicio"
        menu_principal.add_command(label="Inicio", command=self.inicio)

        menu_principal.add_cascade(label="Temas", menu=submenu_temas)
        self.tema_var = tk.StringVar()
        self.tema_var.set("solar")  

        submenu_temas.add_radiobutton(label="Solar", variable=self.tema_var, value="solar", command=self.mudar_tema)

        submenu_temas.add_radiobutton(label="Darkly", variable=self.tema_var, value="darkly", command=self.mudar_tema)

        submenu_temas.add_radiobutton(label="Superhero", variable=self.tema_var, value="superhero", command=self.mudar_tema)


       
        
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

        self.btn_cadastrar = tk.Button(self.frm_botoes, text='Entrar',command=self.confirmar_manager)
        self.btn_cadastrar.grid(row=0, column=1, pady=20, padx=10)
        self.btn_cadastrar.config(font=("algerian", 28))

        
    
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
        self.cbx_gender = ttk.Combobox(self.frame_central, values=lista)
        self.cbx_gender.config(font=("Courier New", 28)) 
        self.cbx_gender.grid(row=8, column=1, sticky="w")
        
        self.frm_botoes = tk.Frame(self.frame_central)
        self.frm_botoes.grid(row=11, column=0, columnspan=2)

        self.btn_cadastrar_book = tk.Button(self.frm_botoes, text='Cadastrar Livro', command=self.confirmar_book)
        self.btn_cadastrar_book.grid(row=0, column=1, pady=20, padx=10)
        self.btn_cadastrar_book.config(font=("algerian", 28))

        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar')
        self.btn_voltar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_voltar.config(font=("algerian", 28))

        
    def confirmar_manager(self):
        if self.ent_nome.get() == '' or self.ent_cpf.get() == '' or self.ent_senha.get() == '' or self.ent_ident.get() == '':
            messagebox.askokcancel("Erro", "Preencha todos os campos!")
            self.cadastro_manager
        else:
            print(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get(), self.ent_ident.get())
            c = Manager(self.ent_nome.get(), self.ent_cpf.get(), self.ent_senha.get(), self.ent_ident.get())
            
            
    def confirmar_book(self):
        if self.ent_titulo.get() == '' or self.ent_author.get() == '' or self.cbx_gender.get() == '':
            messagebox.askokcancel("Erro", "Preencha todos os campos!")
            self.cadastro_book
        else:
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
        self.atualizar_rent()
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
        
        
    def atualizar_rent(self):
        items = self.tvw.get_children() #limpa o componente treeview antes de preencher com o conteúdo do BD
        for i in items:
            self.tvw.delete(i)
        sql_listar_contas = 'SELECT r.id_rent, r.date_start, r.date_end, r.status_rent, c.name_client FROM rent r, client c WHERE r.requester_rent=c.id_client;'
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
        self.atualizar_rent()
    
    def negar(self):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE rent SET status_rent='Negado' WHERE id_rent=1")
        banco.commit()
        banco.close()
        self.atualizar_rent()
        
    def devolvido(self):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("UPDATE rent SET status_rent='Devolvido' WHERE id_rent=1")
        banco.commit()
        banco.close()
        self.atualizar_rent()
        
        
        
        
        
###################################################################################################################
       

    def limpar_grid(self):
        for widget in self.frame_central.winfo_children():
            widget.grid_forget()

    def usuario(self):
        self.style = Style(theme="solar")
        self.limpar_grid()
        # Criar um frame para imagens e botões com espaçamento pady e padx
        frame_conteudo = tk.Frame(self.frame_central, pady=150, padx=20)
        frame_conteudo.grid(row=0, column=0)

        # Load and display the images
        self.logos = ["img/agendaa.png", "img/devolucao.png", "img/R.png"]
        self.carregar_imagens()
        self.exibir_imagens(frame_conteudo)

        # Criar botões dentro do mesmo frame
        self.btn_agendar = tk.Button(frame_conteudo, text='Agendar', font=("algerian", 30), command=self.agendamento)
        self.btn_agendar.grid(row=1, column=0, padx=10)

        self.btn_devolver = tk.Button(frame_conteudo, text='Devolver', font=("algerian", 30))
        self.btn_devolver.grid(row=1, column=1, padx=10)

        self.btn_prorrogar = tk.Button(frame_conteudo, text='Prorrogar', font=("algerian", 30), command=self.prorrogar)
        self.btn_prorrogar.grid(row=1, column=2, pady=10)

        # Criar o menu principal
        menu_principal = Menu(self.janela)
        self.janela.config(menu=menu_principal)

        # Criar um submenu "Temas"
        submenu_temas = Menu(menu_principal, tearoff=0)
        
         # Adicionar um item de menu "Inicio"
        menu_principal.add_command(label="Inicio", command=self.usuario)

        menu_principal.add_cascade(label="Temas", menu=submenu_temas)
        self.tema_var = tk.StringVar()
        self.tema_var.set("solar")  

        submenu_temas.add_radiobutton(label="Solar", variable=self.tema_var, value="solar", command=self.mudar_tema)

        submenu_temas.add_radiobutton(label="Darkly", variable=self.tema_var, value="darkly", command=self.mudar_tema)

        submenu_temas.add_radiobutton(label="Superhero", variable=self.tema_var, value="superhero", command=self.mudar_tema)

        # Adicionar um item de menu "Sobre"
        menu_principal.add_command(label="Sobre", command=self.sobre)


    def sobre(self):
        self.limpar_grid()
        self.frame_central.pack()
        self.style = Style(theme="solar") 
        self.janela.geometry('800x800')

        self.lbl_nome = tk.Label(self.frame_central, text='Bem-vindo à nossa Biblioteca Virtual!\n\n Aqui, acreditamos que a leitura é uma jornada que transcende as páginas de um livro e \n se transforma em uma experiência única e inspiradora. Nossa missão é criar um espaço\n onde a literatura se conecta com a vida real, permitindo que você agende e mergulhe\n nas histórias que tanto ama.\n\n Imagine a sensação de folhear as páginas de um livro físico, sentir o cheiro das páginas\n e ser transportado para mundos desconhecidos. Através da nossa biblioteca virtual, você \n pode não apenas explorar uma vasta coleção de livros, mas também agendar um momento especial\n para pegar um exemplar físico em nossa biblioteca.\n\nAo agendar um livro conosco, você está comprometendo-se não apenas a ler, mas a viver \naventuras, conhecer personagens inspiradores e explorar novas ideias. Cada livro que você \n escolhe representa uma jornada que enriquecerá sua mente e alimentará sua alma.\n\nEntão, reserve um momento, escolha seu livro e agende sua visita à nossa biblioteca. \nDeixe-se inspirar por cada página, e saiba que, com cada agendamento, você está \nescrevendo mais um capítulo da sua própria história literária. Estamos aqui para \ncelebrar essa jornada com você e continuar a inspirar a paixão pela leitura \nem todas as suas formas.')
        
        self.lbl_nome.grid(row=1, column=1, pady=35)
        self.lbl_nome.config(font=("Courier New", 20)) 
        
    def prorrogacao(self):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        self.new_date = datetime.today() + datetime.timedelta(days=7)
        cursor.execute("UPDATE rent SET date_end={self.new_date} WHERE requester_rent = {cpf_user}")
        banco.commit()
        banco.close()
        self.atualizar_rent()



    def agendamento(self):
        self.limpar_grid()
        self.janela.title('Agendar')
        #self.janela.geometry('800x800')
        self.frame_central.pack()
        self.logo_path = "img/biblio.png"
        self.carregar_imagem()
        self.exibir_imagem()
    

        self.lbl_agen = tk.Label(self.frame_central, text='Agendamento')
        self.lbl_agen.config(font=("algerian", 35))
        self.lbl_agen.grid(row=1, column=0, columnspan=2, pady=15)  
        
        # Criando o Scrollbar
        scb_tabela = tk.Scrollbar(self.frame_central)
        scb_tabela.grid(row=2, column=1, sticky=tk.NS)

        # Cria as colunas com lista
        colunas = ['titulo', 'autor', 'genero']
        self.tvw = ttk.Treeview(self.frame_central, show='headings', columns=colunas,bootstyle='success')
        self.tvw.grid(row=2, column=0, sticky=tk.NSEW)



        self.tvw.heading('titulo', text='Titulo')
        self.tvw.heading('autor', text='Autor')
        self.tvw.heading('genero', text='Gênero')
        self.tvw.config(height=30)
        
        #Colunas
        self.tvw.column('titulo', minwidth=30, width=30)
        self.tvw.column('autor', minwidth=100, width=200)
        self.tvw.column('genero', minwidth=100, width=200)
        
        #Linhas
        self.atualizar_agendamento()

        # Crie um frame para os botões
        frame_botoes = tk.Frame(self.frame_central)
        frame_botoes.grid(row=3, column=0, pady=10)

        btn_selecionar = tk.Button(frame_botoes, text='Selecionar',font=("algerian", 30), command=self.selecionar)
        btn_selecionar.grid(row=0, column=0, padx=150)

        btn_confirmar = tk.Button(frame_botoes, text='Confirmar', font=("algerian", 30), command=self.confirmar)
        btn_confirmar.grid(row=0, column=1, padx=150)
        
    
    def listar(self, sql):
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall() 
        banco.close()
        return resultado
        
        
    def atualizar_agendamento(self):
        items = self.tvw.get_children() #limpa o componente treeview antes de preencher com o conteúdo do BD
        for i in items:
            self.tvw.delete(i)
        sql_listar_contas = 'SELECT name_book, author_book, gender_book FROM book;'
        dados = self.listar(sql_listar_contas)
        for linha in dados:
            self.tvw.insert('', tk.END, values=linha)
            
    lista = []    
    def selecionar(self):
        if len(self.lista)<3:
            self.selecao = self.tvw.selection()
            self.seleciona = self.tvw.item(self.selecao, "values")
            self.lista.append(self.seleciona)
            if self.lista == ['']:
                messagebox.askokcancel("Erro", "Selecione um livro!")
            else:
                messagebox.askokcancel("Sucesso", "Livro adicionado!")
        else:
            messagebox.askokcancel("Erro", "Limite de livros atingido!")
        print(self.lista)
    
    def confirmar(self):
        self.limpar_grid()
        self.janela.title('Confirmar empréstimo')
        #self.janela.geometry('800x800')
        self.frame_central.pack()
        self.logo_path = "img/biblio.png"
        self.carregar_imagem()
        self.exibir_imagem()
    

        self.lbl_agen = tk.Label(self.frame_central, text='Agendamento')
        self.lbl_agen.config(font=("algerian", 35))
        self.lbl_agen.grid(row=1, column=0, columnspan=2, pady=15)  
        
        # Criando o Scrollbar
        scb_tabela = tk.Scrollbar(self.frame_central)
        scb_tabela.grid(row=2, column=1, sticky=tk.NS)

        # Cria as colunas com lista
        colunas = ['titulo', 'autor', 'genero']
        self.tvw = ttk.Treeview(self.frame_central, show='headings', columns=colunas,bootstyle='success')
        self.tvw.grid(row=2, column=0, sticky=tk.NSEW)



        self.tvw.heading('titulo', text='Titulo')
        self.tvw.heading('autor', text='Autor')
        self.tvw.heading('genero', text='Gênero')
        self.tvw.config(height=30)
        
        #Colunas
        self.tvw.column('titulo', minwidth=30, width=30)
        self.tvw.column('autor', minwidth=100, width=200)
        self.tvw.column('genero', minwidth=100, width=200)
        
        #Linhas
        for i in self.lista:
            self.tvw.insert('', tk.END, values=(i))

        # Crie um frame para os botões
        frame_botoes = tk.Frame(self.frame_central)
        frame_botoes.grid(row=3, column=0, pady=10)

        btn_confirmar = tk.Button(frame_botoes, text='Pedir', font=("algerian", 30), command=self.pedir)
        btn_confirmar.grid(row=0, column=1, padx=150)
        
        
    def prorrogar(self):
        self.limpar_grid()
        colunas = ('id', 'date_start', 'date_end', 'status_rent', 'requester_rent', 'name_book')
        self.tvw = ttk.Treeview(self.frame_central, columns=colunas, height=5, show='headings')
        self.tvw.grid(row=0,column=0)
        #Cabeçalho
        self.tvw.heading('id', text='ID')
        self.tvw.heading('date_start', text='Início')
        self.tvw.heading('date_end', text='Final')
        self.tvw.heading('status_rent', text='Status')
        self.tvw.heading('requester_rent', text='Solicitante')
        self.tvw.heading('name_book', text='Livros')
        #Colunas
        self.tvw.column('id', minwidth=30, width=30)
        self.tvw.column('date_start', minwidth=100, width=200)
        self.tvw.column('date_end', minwidth=100, width=200)
        self.tvw.column('status_rent', minwidth=200, width=200)
        self.tvw.column('requester_rent', minwidth=200, width=200)
        self.tvw.column('name_book', minwidth=200, width=200)
        #Linhas
        self.atualizar_prorrogar()
        # #Barra de rolagem
        # scb = ttk.Scrollbar(self.janela, orient=tk.VERTICAL,command=self.tvw.yview)
        # scb.grid(row=0, column=1, sticky='ns')
        # self.tvw.config(yscrollcommand=scb.set)
        
        self.frm_botoes = tk.Frame(self.frame_central)
        self.frm_botoes.grid(row=1, column=0)
        
        self.btn_aceitar = tk.Button(self.frm_botoes, text='Prorrogar', command=self.prorrogacao)
        self.btn_aceitar.grid(row=0, column=0, pady=20, padx=10)
        self.btn_aceitar.config(font=("algerian", 20))
        
        
        
    def atualizar_prorrogar(self):
        items = self.tvw.get_children() #limpa o componente treeview antes de preencher com o conteúdo do BD
        for i in items:
            self.tvw.delete(i)
        sql_listar_contas = 'SELECT r.id_rent, r.date_start, r.date_end, r.status_rent, c.name_client, b.name_book FROM rent r, client c, book b WHERE r.requester_rent=c.id_client AND b.status_book=="Aprovado";'
        dados = self.listar(sql_listar_contas)
        for linha in dados:
            self.tvw.insert('', tk.END, values=linha)
        
    
    def pedir(self):
        r = Rent(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7), 'pendente')
        
# janela = tk.Tk()
# app = LoginAdm(janela)
# janela.mainloop()
janela = tk.Tk()
app = LoginAdm(janela)
janela.mainloop()
