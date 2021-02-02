import ldap
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

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
#efetuando uma busca
ldap_filter = '(objectClass=eTRole)'
result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
#print("---------------*******PROVSTORE********-------------")  
count = -1
while (count < len(result)-1):
    count += 1
    resultado = result[count][1] 
    #print(result[count][1] )
    #print(type(result[count][1] )) #tipo dict objeto: atributoObjto : [valor objeto]
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") 
    provrole = str(result01).replace(removerdois, "") 
    #print(provrole)
    #print(type(provrole)) - tipo string
#print("---------------******IDM*********-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor para executar query
#query idm:
cursor.execute("SELECT DISTINCT  FROM  WHERE  ORDER BY  ASC") # consulta sql
resultidm = cursor.fetchall()  # busca o resultado da consulta
#print(resultidm)
#print("---------------*******PORTAL********-------------")
#query portal
cursor.execute("SELECT DISTINCT  FROM  ORDER BY  ASC") # consulta sql
resultportal = cursor.fetchall()  # busca o resultado da consulta

#print("---------------*******FIM CONSULTA********-------------")

print("--------*********-------------")
idmVSportal = list(set(resultidm) - set(resultportal))
#print(idmVSportal)

print("-------***********-------------")
portalVSidm = list(set(resultportal) - set(resultidm))
#print(portalVSidm)

print("---------------*************-------------")
provRoleVSidm = list(set(provrole) - set(resultidm))
print(provRoleVSidm)

print("---------------*************-------------")
idmVSprovRole = list(set(resultidm) - set(provrole))
print(idmVSprovRole)
