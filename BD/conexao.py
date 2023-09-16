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

        #falta adicionar os livros

        conn.commit()
        conn.close()

    conn = sqlite3.connect('libraryDB.db')
    return conn