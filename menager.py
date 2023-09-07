import sqlite3

class Manager:
    def __init__(self, name, cpf, password, ident):
        self._name = name
        self._cpf = cpf
        self._password = password
        self._ident = ident
        
        
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO manager (name_manager, cpf_manager, password_manager, identificator_manager) VALUES('"+self._name+"', '"+self._cpf+"', '"+self._password+"', '"+self._ident+"')")
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
        
    @property
    def identificator(self):
        return self._ident
    @identificator.setter
    def senha(self, value):
        self._ident = value