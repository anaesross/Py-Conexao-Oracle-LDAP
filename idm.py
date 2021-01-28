import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

uid = "IDM"    # usuário
pwd = "Loc@1020"   # senha
db = "//192.168.37.128:1521/xe" # string de conexão do Oracle
 
connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor

cursor.execute("SELECT DISTINCT IMR_NAME FROM idm.IMRROLE6 WHERE IMR_TYPE = 'Provisioning Role' ORDER BY IMR_NAME ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
while result:   
    idm = result[0]
    print (idm)
    result = cursor.fetchone()
