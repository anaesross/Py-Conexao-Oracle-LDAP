import ldap
import cx_Oracle
from openpyxl import Workbook
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

wb = Workbook()
planilha = wb.worksheets[0] # criando index da planilha

#criando variáveis globais
idm = []
portal = []
provrole = []
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
#efetuando uma busca
ldap_filter = '(objectClass=eTRole)'
result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
#print("---------------*******PROVSTORE********-------------")  
count = -1
while (count < len(result)-1):
    count += 1
    resultado = result[count][1] 
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") 
    result02 = str(result01).replace(removerdois, "") 
    provrole.append(result02)
#print(provrole)

#print("---------------******IDM*********-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() 
#query idm:
cursor.execute("SELECT DISTINCT  FROM  WHERE  ORDER BY  ASC") # consulta sql
resultidm = cursor.fetchall()  
i = 0
for i in resultidm:
    if len(i) > 0:
        conversor = list(i)
        idm.append(conversor[0])

#print(idm)
#print("---------------*******PORTAL********-------------")
#query portal
cursor.execute("SELECT DISTINCT  FROM  ORDER BY  ASC") # consulta sql
resultportal = cursor.fetchall() 
i = 0
for i in resultportal:
    if len(i) > 0:
        conversor = list(i)
        portal.append(conversor[0])
#print(portal)
#print("---------------*******FIM CONSULTA********-------------")
planilha['A1'] = "Coluna 1"
planilha['B1'] = "Coluna 2"
planilha['C1'] = "Coluna 3"
planilha['D1'] = "Coluna 4"

#criando primeira linha d excel
print("---------------*******Coluna 1********-------------")
idmVSportal = list(set(idm) - set(portal)) 
count = -1
i= 1
while (count < len(idmVSportal)-1):
    count += 1
    i += 1 
    valor = idmVSportal[count]
    planilha['A'+ str(i)] = str(valor)
print(idmVSportal)
print("---------------*******Coluna 2********-------------")
portalVSidm = list(set(portal) - set(idm))
count = -1
i= 1
while (count < len(portalVSidm)-1):
    count += 1
    i += 1
    valorUm = portalVSidm[count]
    planilha['B'+ str(i)] = str(valorUm)
print(portalVSidm)
print("---------------*******Coluna 3********-------------")
provRoleVSidm = list(set(provrole) - set(idm))
count = -1
i= 1
while (count < len(provRoleVSidm)-1):
    count += 1
    i += 1
    valorDois = provRoleVSidm[count]
    planilha['C'+ str(i)] = str(valorDois)
print(provRoleVSidm)

print("---------------*******Coluna 4********-------------")
idmVSprovRole = list(set(idm) - set(provrole))
count = -1
i= 1
while (count < len(idmVSprovRole)-1):
    count += 1
    i += 1
    valorTres = idmVSprovRole[count]
    planilha['D'+ str(i)] = str(valorTres)
print(idmVSprovRole)

wb.save("diferencas.xlsx")
