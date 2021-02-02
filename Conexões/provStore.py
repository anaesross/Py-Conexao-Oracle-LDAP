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

result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter,['eTRoleName'])
                            # base em que é efetuada a busca, o segundo é o escopo da busca e por último o filtro
print(result)
count = -1
while (count < len(result)-1):
    count += 1
    resultado = result[count][1] 
    resultado = str(resultado)
    remover = "{'eTRoleName': [b'"
    removerdois = "']}"
    result01 = str(resultado).replace(remover, "") 
    #print("Replace1: ", result01)
    result02 = str(result01).replace(removerdois, "") 
    print(result02) 
    print(type (result02))
