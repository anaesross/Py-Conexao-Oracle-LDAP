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
password = "Loc@1020"
db = "//192.168.37.128:1521/xe"
uid = "IDM"

#Criando conexão LDAP
address = "192.168.37.128:20389"
user = "eTGlobalUserName=etaadmin,eTGlobalUserContainerName=Global Users,eTNamespaceName=CommonObjects,dc=im,dc=eta"
base = "eTRoleContainerName=Roles,eTNamespaceName=CommonObjects,dc=im,dc=eta"
connection = ldap.initialize("ldap://%s"%address)
connection.protocol_version = ldap.VERSION3  #define versao 3 do protocolo ldap (recomendado)
connection.bind(user,password)
#efetuando uma busca no ldap
ldap_filter = '(objectClass=eTRole)'
result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
print("---------------*******PROVSTORE********-------------")  
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
print("---------------******IDM*********-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor
#query idm:
cursor.execute("SELECT DISTINCT IMR_NAME FROM idm.IMRROLE6 WHERE IMR_TYPE = 'Provisioning Role' ORDER BY IMR_NAME ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
count = 0
while result:   
    count +=1
    idm = result[0]
    #print (idm)
    planilha['B'+ str(count)] = idm
    result = cursor.fetchone()
print("---------------*******PORTAL********-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor
#query portal:
cursor.execute("SELECT DISTINCT NAME FROM IDENTITYPORTAL.PERMISSION ORDER BY NAME ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
count = 0
while result:   
    count +=1
    portal = result[0]
    #print (portal) #imprime todas as roles
    planilha['C'+ str(count)] = portal #escreve na planilha na coluna C os nomes das roles
    result = cursor.fetchone() # o que essa linha faz ?
cursor.close() #finaliza query
connection.close() #finaliza conexão com o banco

wb.save("C:\\Users\\Anaê\\Desktop\\roles.xlsx")

#imprime apenas o último valor, está sobreescrevendo? ou não consigo acessar pq eh uma tupla?
print("Portal: ", portal)
print("IDM: ", idm)
print("ProvRole: ", provrole)
print(type(portal))
"""
print(planilha['A1'].value)
print(planilha['B1'].value)
print(planilha['C1'].value)
"""
x = set(portal) and set(provrole) #verifica diferenças entre os dois
print("Diferenças: " , x)