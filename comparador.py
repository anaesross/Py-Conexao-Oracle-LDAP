import ldap
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"D:\\instantclient_19_9")

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
#efetuando uma busca
ldap_filter = '(objectClass=eTRole)'
result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
print("---------------*******PROVSTORE********-------------")  
count = -1
while (count < len(result)-1):
    count += 1
    resultado = result[count][1] 
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") 
    provrole = str(result01).replace(removerdois, "") 
    #print(provrole)
print("---------------******IDM*********-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor
#query idm:
cursor.execute("SELECT DISTINCT IMR_NAME FROM idm.IMRROLE6 WHERE IMR_TYPE = 'Provisioning Role' ORDER BY IMR_NAME ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
while result:   
    idm = result[0]
    #print (idm)
    result = cursor.fetchone()
print("---------------*******PORTAL********-------------")
connection = cx_Oracle.connect(uid+"/"+password+"@"+db) #cria a conexão
cursor = connection.cursor() # cria um cursor
#query portal:
cursor.execute("SELECT DISTINCT NAME FROM IDENTITYPORTAL.PERMISSION ORDER BY NAME ASC") # consulta sql
result = cursor.fetchone()  # busca o resultado da consulta
while result:   
    portal = result[0]
    #print (portal)
    result = cursor.fetchone()
cursor.close() #finaliza query
connection.close() #finaliza conexão com o banco

#só printa o último valor, está sobreescrevendo? 
print ("Teste Portal: " , portal) #Teste SalesForce Roles
print ("Teste idm: " , idm) #Teste SalesForce Roles
print ("Teste provrole: " , provrole) # SalesForce Roles

x = set(portal) and set(provrole) #verifica diferenças entre os dois
print("Diferenças: " , x)

if ( portal and provrole != idm):
    print("Diferentes")
else:
    print("Não tem diferenças")