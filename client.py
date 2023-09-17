import sqlite3
import re

class Client:
    def __init__(self, name, cpf, senha):
        self._name = name
        self._cpf = cpf
        self._password = senha
        #self._Csenha = senha2
        
        # banco = sqlite3.connect('libraryDB.db')
        # cursor = banco.cursor()
        # cursor.execute("INSERT INTO client (name_client, cpf_client, password_client) VALUES(?,?,?)", (self._name, self._cpf, self._password))
        # banco.commit()
        # banco.close()
        
        
    
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
         
    
    def valida(self):
        if not self.cpf:
            return False
        novo_cpf = self.calcula(self.cpf[:9])
        novo_cpf = self.calcula(novo_cpf)
        if novo_cpf == self.cpf:
            return True
        return False
        
    @staticmethod
    def calcula(fatia):
        if not fatia:
            return False
        
        sequencia = fatia[0] * len(fatia)
        
        if sequencia == fatia:
            return False
        soma = 0
        for c,m in enumerate(range(len(fatia)+1, 1, -1)):
            soma += int(fatia[c]*m)
            
        resto = 11-(soma%11)
        resto = resto if resto <= 9 else 0
        return fatia + str(resto)
    
    @staticmethod
    def numeros(cpf):
        return re.sub('[^0-9]','', cpf)