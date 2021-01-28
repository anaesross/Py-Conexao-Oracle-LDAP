import ldap
# Criando conexão LDAP
# definindo variaveis de conexao

address = "192.168.37.128:20389"
user = "eTGlobalUserName=etaadmin,eTGlobalUserContainerName=Global Users,eTNamespaceName=CommonObjects,dc=im,dc=eta"
password = "Loc@1020"
base = "eTRoleContainerName=Roles,eTNamespaceName=CommonObjects,dc=im,dc=eta"
#"dc=im,dc=eta"
# efetuando conexao
connection = ldap.initialize("ldap://%s"%address)
connection.protocol_version = ldap.VERSION3  #define versao 3 do protocolo ldap (recomendado)
connection.bind(user,password)

#efetuando uma busca
ldap_filter = '(objectClass=eTRole)'

#att = 'eTRoleName'
#'(&(objectClass=eTRole (eTRoleName=*)))'

result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
#print(result[1][1])
"""
valor = result[0][1]
stri = str(valor)
print("String: " , stri) # {'eTRoleName': [b'Acesso Basico Funcionario']}
print (type(valor))
"""
"""
stri = result[0][1]
stri = str(stri)
print(stri)
remover = "{'eTRoleName': [b'"
removerdois = "']}"
stri_novo = stri.replace(remover, "") # Acesso Basico Funcionario']}
stri_novo = stri_novo.replace(removerdois, "") # Acesso Basico Funcionario
print(stri_novo) # Acesso Basico Funcionario
"""


count = -1
while (count < len(result)-1):
    count += 1
    #print("COntador: " , count) # inicio: 0 - /  1volta: 1
    #print("Primeiro Result: " , result)  # inicio : todas as roles em uma lista -/ 1volta: {'eTRoleName': [b'Acesso Basico Funcionario']}
    # {'eTRoleName': [b'Acesso Basico Funcionario']} - result vem assim no 2 loop
    #print("trava aqui no segundo loop")
    resultado = result[count][1] 
    #print("Primeira String " , str(resultado)) # inicio: {'eTRoleName': [b'Acesso Basico Funcionario']}
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") # Acesso Basico Funcionario']}
    #print("Replace1: ", result01)
    result02 = str(result01).replace(removerdois, "") 
    print("Replace2: ", result02) # Acesso Basico Funcionario
    
    #result = result[count][1]
    
    #print(str(result02)) #[1] qual atributo quero , estou buscando apenas o etrolename
