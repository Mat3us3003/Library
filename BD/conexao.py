import sqlite3
import os

def criar_conexao():
    if not os.path.exists('libraryDB.db'):
        conn = sqlite3.connect('libraryDB.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE "book" (
                        "id_book"	INTEGER NOT NULL,
                        "name_book"	TEXT NOT NULL,
                        "author_book"	TEXT NOT NULL,
                        "status_book"	BLOB NOT NULL,
                        "gender_book"	TEXT NOT NULL,
                        PRIMARY KEY("id_book" AUTOINCREMENT));''')
        
        cursor.execute('''CREATE TABLE "client" (
                        "id_client"	INTEGER NOT NULL UNIQUE,
                        "name_client"	TEXT NOT NULL,
                        "cpf_client"	TEXT NOT NULL,
                        "password_client"	TEXT NOT NULL,
                        PRIMARY KEY("id_client" AUTOINCREMENT));''')
        
        cursor.execute('''CREATE TABLE "manager" (
                        "id_manager"	INTEGER NOT NULL,
                        "name_manager"	TEXT NOT NULL,
                        "cpf_manager"	INTEGER NOT NULL,
                        "password_manager"	INTEGER NOT NULL,
                        "identificator_manager"	INTEGER NOT NULL,
                        PRIMARY KEY("id_manager" AUTOINCREMENT));''')
        
        cursor.execute('''CREATE TABLE "rent" (
                        "id_rent"	INTEGER NOT NULL UNIQUE,
                        "date_start"	BLOB NOT NULL,
                        "date_end"	BLOB NOT NULL,
                        "status_rent"	TEXT NOT NULL,
                        "requester_rent"	INTEGER NOT NULL,
                        PRIMARY KEY("id_rent" AUTOINCREMENT));''')

        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('O Alienista', 'Machado de Assis', True, 'Literatura'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('Senhor do Aneis: Retorno do Rei', 'J.R.R. Tolkien', True, 'Aventura'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('O Caminho da Luz', 'Paulo Coelho', True, 'Autoajuda'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('A Divina Comédia', 'Dante Alighieri', True, 'Literatura'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('A Origem das Espécies', 'Charles Darwin', True, 'Ciências'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', True, 'Literatura'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('A Metamorfose', 'Franz Kafka', True, 'Literatura'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('1984', 'George Orwell', True, 'Ficção Científica'))

        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('O Guia do Mochileiro das Galáxias', 'Douglas Adams', True, 'Ficção Científica'))
        
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", ('O Código Da Vinci', 'Dan Brown', True, 'Ficção'))
        
        cursor.execute("INSERT INTO manager (name_manager, cpf_manager, password_manager, identificator_manager) VALUES(?,?,?,?)", ('Mateus', '16581239216', '123456', '555'))
        
        cursor.execute("INSERT INTO manager (name_manager, cpf_manager, password_manager, identificator_manager) VALUES(?,?,?,?)", ('Joceli', '27162748279', '654321', '555'))
        conn.commit()
        conn.close()

    conn = sqlite3.connect('libraryDB.db')
    return conn