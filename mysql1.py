import mysql.connector
conexao = mysql.connector.connect(user = 'root',password = 'uniceub',host = '127.0.0.1',database = 'db_empresa')
print(f'Conexão:{conexao}')
# print('\nConexão fechada.')
cursor = conexao.cursor()
# sql = 'CREATE DATABASE db_empresa if not exists'
# cursor.execute(sql)
sql1 = '''create table if not exists tb_funcionario(
    idt INT,
    nome VARCHAR(45)NOT NULL,
    salario DECIMAL(9,2)NULL,
    PRIMARY KEY (idt)
)'''
# cursor.execute(sql1)
# sql2 = '''insert into tb_funcionario
#     (idt,nome,salario)
#     values(5,'Pias',51000.00)          

# '''
# cursor.execute(sql2)
# conexao.commit()

# sql4 = '''delete from tb_funcionario 
#         where idt = 4'''
# cursor.execute(sql4)
# conexao.commit()
sql5 = '''update tb_funcionario
set salario = 100000
where nome = "Pedro"
'''
cursor.execute(sql5)

sql = '''select * from tb_funcionario
    '''
cursor.execute(sql)
registros = cursor.fetchall()
for i in registros:
    print(i)

# print('-Colunas,notação de vetor:')
# for row in registros:
#     print(f'Idt:{row[0]}')
#     print(f'Name:{row[1]}')
#     print(f'Salario:{row[2]}')

# for idt,nome,salario in registros:
#     print(f'Idt:{idt}')
#     print(f'Name:{nome}')
#     print(f'Salario:{salario}')

cursor.close()
conexao.close()
print('\nConexao fechada')