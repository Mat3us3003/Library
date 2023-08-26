import sqlite3
from sqlite3 import Error

class Client:
    def __init__(self, name,  cpf):
        self._Fname = name
        self._cpf = cpf
    
    @property
    def Fname(self):
        return self._Fname
    
    @Fname.setter
    def Fname(self, name):
        self._Fname = name
        
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
    
    
    #Função para conectar no banco de dados
    def conecta():
        try:
            con = sqlite3.connect('libraryDB.db')
            #print('Conexão estabelecida com sucesso!')
            return con
        except Error as er:
            print('Erro durante a conexão.')


    'Passos: conexão, usar a conexão, executar a instrução, fechar a conexão'
    def inserir(self, sql):
        sql_inserir = f"INSERT INTO client VALUES ({self._Fname}, {self._cpf});"
        con = self.conecta()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    
    
         