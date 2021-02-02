import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

dados = ''

uid = ""    # usuário
pwd = ""   # senha
db = "" # string de conexão do Oracle

connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db) # cria a conexão
cursor = connection.cursor() # cria um cursor

cursor.execute("SELECT DISTINCT  FROM  ORDER BY  ASC") # consulta sql
result = cursor.fetchall()  # busca o resultado da consulta , tipo tuple (???)
#for i in result:
print(result)

result = list(result)

print(type (result))
portal = []
i = 0
for i in result:
    if len(i) > 0:
        conversor = list(i)
        portal.append(conversor[0])

print(portal)
print(type (portal))