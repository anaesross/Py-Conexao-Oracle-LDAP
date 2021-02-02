import ldap
# Criando conexão LDAP
# definindo variaveis de conexao

address = ""
user = ""
password = ""
base = "" 
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

provStore = []

count = -1
while (count < len(result)-1):
    count += 1
    resultado = result[count][1] 
    #print("Primeira String " , str(resultado)) # inicio: {'eTRoleName': [b'Acesso Basico Funcionario']}
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") # Acesso Basico Funcionario']}
    #print("Replace1: ", result01)
    result02 = str(result01).replace(removerdois, "") 
    
    provStore.append(result02)

print(provStore)
print(type (provStore))