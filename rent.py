import sqlite3

class Rent:
    def __init__(self, start, end, status, requester):
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
        cursor.execute("INSERT INTO rent (date_start, date_end, status_rent, requester_rent) VALUES(?,?,?,?)", (hoje, final, stat, req))
        banco.commit()
        banco.close()