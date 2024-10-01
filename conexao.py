import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco"
)

if conexao.is_connected():
    print("Conectado")
    cursor=conexao.cursor()

conexao.close()
cursor.close()