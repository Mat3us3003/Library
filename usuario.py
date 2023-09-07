import tkinter as tk
from tkinter import ttk, Menu
from ttkbootstrap.style import Style
from PIL import Image, ImageTk


class Janelausuario:
    def __init__(self, janela):
        self.janela = janela
        self.frame_central = tk.Frame(self.janela)
        self.frame_central.pack()
        self.style = Style(theme="solar")
        self.janela.geometry('800x800')
        self.usuario()

    def limpar_grid(self):
        for widget in self.frame_central.winfo_children():
            widget.grid_forget()

    def usuario(self):
        self.limpar_grid()
        # Criar um frame para imagens e botões com espaçamento pady e padx
        frame_conteudo = tk.Frame(self.frame_central, pady=150, padx=20)
        frame_conteudo.grid(row=0, column=0)

        # Load and display the images
        self.logos = ["img/agendaa.png", "img/devolucao.png", "img/R.png"]
        self.carregar_imagens()
        self.exibir_imagens(frame_conteudo)

        # Criar botões dentro do mesmo frame
        self.btn_agendar = tk.Button(frame_conteudo, text='Agendar', font=("algerian", 30))
        self.btn_agendar.grid(row=1, column=0, padx=10)

        self.btn_devolver = tk.Button(frame_conteudo, text='Devolver', font=("algerian", 30))
        self.btn_devolver.grid(row=1, column=1, padx=10)

        self.btn_prorrogar = tk.Button(frame_conteudo, text='Prorrogar', font=("algerian", 30))
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


    def mudar_tema(self):
        # Obter o tema selecionado e aplicá-lo
        tema = self.tema_var.get()
        self.style.theme_use(tema)

    def sobre(self):
        self.limpar_grid()
        self.janela = janela
        self.frame_central.pack()
        self.style = Style(theme="solar") 
        self.janela.geometry('800x800')

        self.lbl_nome = tk.Label(self.frame_central, text='Bem-vindo à nossa Biblioteca Virtual!\n\n Aqui, acreditamos que a leitura é uma jornada que transcende as páginas de um livro e \n se transforma em uma experiência única e inspiradora. Nossa missão é criar um espaço\n onde a literatura se conecta com a vida real, permitindo que você agende e mergulhe\n nas histórias que tanto ama.\n\n Imagine a sensação de folhear as páginas de um livro físico, sentir o cheiro das páginas\n e ser transportado para mundos desconhecidos. Através da nossa biblioteca virtual, você \n pode não apenas explorar uma vasta coleção de livros, mas também agendar um momento especial\n para pegar um exemplar físico em nossa biblioteca.\n\nAo agendar um livro conosco, você está comprometendo-se não apenas a ler, mas a viver \naventuras, conhecer personagens inspiradores e explorar novas ideias. Cada livro que você \n escolhe representa uma jornada que enriquecerá sua mente e alimentará sua alma.\n\nEntão, reserve um momento, escolha seu livro e agende sua visita à nossa biblioteca. \nDeixe-se inspirar por cada página, e saiba que, com cada agendamento, você está \nescrevendo mais um capítulo da sua própria história literária. Estamos aqui para \ncelebrar essa jornada com você e continuar a inspirar a paixão pela leitura \nem todas as suas formas.')
        
        self.lbl_nome.grid(row=1, column=1, pady=35)
        self.lbl_nome.config(font=("Courier New", 20)) 

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


janela = tk.Tk()
app = Janelausuario(janela)
janela.mainloop()