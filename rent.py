import sqlite3

class Rent:
    def __init__(self, start, end, requester, status='Pendente'):
        self._date_start = start
        self._date_end = end
        self._status = status
        self._requester = requester
    
        banco = sqlite3.connect('libraryDB.db')
        cursor = banco.cursor()
        hoje = self._date_start
        final = self._date_end
        stat = self._status
        req = self._requester
        cursor.execute("INSERT INTO rent (date_start, date_end, status_rent, requester_rent) VALUES(?,?,?,?)", (self._date_start, self._date_end, self._status, self._requester))
        banco.commit()
        banco.close()