from client import Client
from book import Book
from menager import Manager
from rent import Rent
from datetime import datetime, timedelta
import datetime
from validate_docbr import CPF
#c1 = Client('Jocely Franco', '123456789', '123')
#b1 = Book('O Alienista', 'Machado de Assis', 'True', 'Literatura')
#m1 = Manager('Mateus', '987654321', '321', '555')
#r1 = Rent(datetime.date.today(), datetime.date.today() + timedelta(days=7), 1, 'pendente')

c2 = Client('Mateus', '012.345.678-90', '123')
print(CPF().validate('012.345.678-90'))
print(c2.cpf)
if c2.cpf:
    print('valido')
else:
    print('invalido')

# print(datetime.date.today())