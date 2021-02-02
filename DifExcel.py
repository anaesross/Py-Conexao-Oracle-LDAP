from openpyxl import Workbook
import ldap
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

#declarando variáveis globais
valor = ''
provrole = ''
idm = ''
portal = ''

#criando objeto workbook para criar o excel
wb = Workbook()

planilha = wb.worksheets[0] # criando index da planilha

#criando variáveis globais
provrole = ''
portal = ''
idm = ''
#variáveis para conexão com banco oracle
password = ""
db = ""
uid = ""

#Criando conexão LDAP
address = ""
user = ""
base = ""
connection = ldap.initialize("ldap://%s"%address)
connection.protocol_version = ldap.VERSION3  #define versao 3 do protocolo ldap (recomendado)
connection.bind(user,password)
#efetuando uma busca no ldap
ldap_filter = '(objectClass=eTRole)'
result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
print("------*********-------------")  
count = -1
i = 0
while (count < len(result)-1):
    count += 1
    i += 1
    resultado = result[count][1] 
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") 
    provrole = str(result01).replace(removerdois, "") 
    planilha['A'+ str(i)] = provrole
    #print(provrole)
print("---------------***************-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor
#query idm:
cursor.execute("SELECT DISTINCT  FROM  WHERE  ORDER BY  ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
count = 0
while result:   
    count +=1
    idm = result[0]
    planilha['B'+ str(count)] = idm
    result = cursor.fetchone()
print("---------------***************-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor
#query portal:
cursor.execute("SELECT DISTINCT  FROM  ORDER BY  ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
count = 0
while result:   
    count +=1
    portal = result[0]
    planilha['C'+ str(count)] = portal #escreve na planilha na coluna C os nomes das roles
    result = cursor.fetchone() 
cursor.close() #finaliza query
connection.close() #finaliza conexão com o banco


wb.save("roles.xlsx")
