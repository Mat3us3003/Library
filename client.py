import sqlite3

class Client:
    def __init__(self, name, cpf, senha):
        self._name = name
        self._cpf = cpf
        self._password = senha
        #self._Csenha = senha2
        
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO client (name_client, cpf_client, password_client) VALUES('"+self._name+"', '"+self._cpf+"', '"+self._password+"')")
        banco.commit()
        banco.close()
        
        
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value
         