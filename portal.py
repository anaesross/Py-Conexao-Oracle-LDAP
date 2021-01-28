from openpyxl import Workbook
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

wb = Workbook()

planilha = wb.worksheets[0]

dados = ''

uid = "IDM"    # usuário
pwd = "Loc@1020"   # senha
db = "//192.168.37.128:1521/xe" # string de conexão do Oracle

connection = cx_Oracle.connect(uid+"/"+pwd+"@"+db) # cria a conexão
cursor = connection.cursor() # cria um cursor

cursor.execute("SELECT DISTINCT NAME FROM IDENTITYPORTAL.PERMISSION ORDER BY NAME ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta , tipo tuple (???)
result = list(result)
print("Primeiro Print: " , result[0])
count = 0
while result:
    count += 1
    dados = result[0]
    print (dados)
    planilha['A'+ str(count)] = dados
    result = cursor.fetchone()
print(dados)
wb.save("C:\\Users\\Anaê\\Desktop\\roles.xlsx")
#print("teste: " + dados) #só vem o último, está sobreescrevendo?


