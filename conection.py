import sqlite3
from sqlite3 import Error
#Função para conectar no banco de dados
def conecta():
    try:
        con = sqlite3.connect('libraryDB.db')
        #print('Conexão estabelecida com sucesso!')
        return con
    except Error as er:
        print('Erro durante a conexão.')

sql_mostra_cliente = 'SELECT * FROM cliente;'
'Estabelecer a conexão com o banco de dados'
def listar(sql):
    con = conecta()
    cursor = con.cursor() #Objeto que permite executar SQL
    cursor.execute(sql)
    resultado = cursor.fetchall() #carrega todos os dados em resultado
    #for i in resultado:
    #    print(i)
    con.close()
    return resultado

sql_inserir_cliente = "INSERT INTO cliente VALUES (NULL, 'Teste', '123', 'teste@teste');"
'Passos: conexão, usar a conexão, executar a instrução, fechar a conexão'
def inserir(sql):
    con = conecta()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()

# sql_atualizar = 'UPDATE cliente SET nome="Teste Alterado", email="teste@alterado" WHERE id=5;'
# def atualizar(sql):
#     con = conecta()
#     cursor = con.cursor()
#     cursor.execute(sql)
#     con.commit()
#     con.close()

# sql_remover = f'DELETE FROM cliente WHERE id=4;'
# def remover(sql):
#     con = conecta()
#     cursor = con.cursor()
#     cursor.execute(sql)
#     con.commit()
#     con.close()

#criar_tabela(sql_criar_tabela)
#inserir(sql_inserir_cliente)
#atualizar(sql_atualizar)
#remover(sql_remover)
#mostrar_tabela(sql_mostra_cliente)
#listar(sql_mostra_cliente)