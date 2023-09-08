import sqlite3

class Book:
    def __init__(self, name, author, gender, status=True):
        self._name = name
        self._author = author
        self._status = status
        self._gender = gender
        
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO book (name_book, author_book, status_book, gender_book) VALUES(?,?,?,?)", (self._name, self._author, self._status, self._gender))
        banco.commit()
        banco.close()
        
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        self._author = value
        
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
    
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, value):
        self._gender = value