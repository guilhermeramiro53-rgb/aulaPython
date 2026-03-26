import pymysql as pySQL
print(pySQL.version_info)
# cria a conexão com o banco de dado
conexao = pySQL.connect(
    host="localhost",   # endereço do serividor (local = "localhost")
    user="root", # usuário do mysql
    password="",  # senha do mysql
    database="bd_livrariaonline", # banco que voce ja criou
    port=3306   # porta padrão do mysql
)

# Criar o cursor - versão dicionário (retorna {"coluna": valor})
cursor = conexao.cursor(pySQL.cursors.DictCursor)

# Buscar todos os registros
cursor.execute("SELECT * FROM clientes")
todos = cursor.fetchall()

for cliente in todos:
    print(cliente["nome"],"-", cliente["email"],"-", cliente["telefone"])
