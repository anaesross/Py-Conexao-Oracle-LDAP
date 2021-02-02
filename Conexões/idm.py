import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

uid = ""    # usuário
pwd = ""   # senha
db = "" # string de conexão do Oracle
 
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor

cursor.execute("SELECT DISTINCT  FROM  WHERE  ORDER BY  ASC") # consulta sql
result = cursor.fetchall()  # busca o resultado da consulta , mudar para fetchall vem todos de uma vez
print("Primeiro Print: " , result[0])
count = 0
while result:
    count += 1
    idm = result[0]
    print (idm)
    #print(type(dados))
    result = cursor.fetchall()

