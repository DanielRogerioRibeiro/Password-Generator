# Este é um Gerador de senha para criação de Senhas a partir do método de Substituição de Palavra dada pelo Usuário.
# Para maiores detalhes acesse README.md 

print ("Olá, Seja Bem Vindo ao Gerador de Senha.")
chave = input ("Por favor digite uma palavra Chave para a sua senha: ")

print ("Sua Palavra Chave é: ", chave,"?")

#Validação da Senha

val = input ("Digite '1' para Sim ou '2' para não: ")
validacao = int (val)  
if validacao == 1:
    print ("Ok")
else:
    chave1 = input ("Por favor digite sua Nova Chave: ")
    
# Catálogo de Substituição de Letras da Segunda Chave
    senha1 = ""
    for letra in chave1:
        if letra in "a":
            senha1 = senha1 + "@"
        elif letra in "Ee": 
            senha1 = senha1 + "3"
        elif letra in "l": 
            senha1 = senha1 + "&"
        elif letra in "Ii": 
            senha1 = senha1 + "!"
        elif letra in "Oo": 
            senha1 = senha1 + "0"
        elif letra in "Uu": 
            senha1 = senha1 + "*"
        elif letra in "Ss": 
            senha1 = senha1 + "$"
        elif letra in "Tt": 
            senha1 = senha1 + "?"
        elif letra in "Cc": 
            senha1 = senha1 + "¢"
        elif letra in "Gg": 
            senha1 = senha1 + "¨"
        elif letra in "Bb": 
            senha1 = senha1 + "5"
        elif letra in "m": 
            senha1 = senha1 + "+"
        elif letra in "n": 
            senha1 = senha1 + "^"
        elif letra in "r": 
            senha1 = senha1 + "~"
        elif letra in "Ll": 
            senha1 = senha1 + "11"    
        else: senha1 = senha1 + letra

  
# Catálogo de Substituição de Letras da Primeira Chave

senha = ""
for letra in chave:
    if letra in "a":
        senha = senha + "@"
    elif letra in "E": 
        senha = senha + "3"
    elif letra in "e": 
        senha = senha + "&"
    elif letra in "Ii": 
        senha = senha + "!"
    elif letra in "Oo": 
        senha = senha + "0"
    elif letra in "Uu": 
        senha = senha + "*"
    elif letra in "Ss": 
        senha = senha + "$"
    elif letra in "Tt": 
        senha = senha + "?"
    elif letra in "Cc": 
        senha = senha + "¢"
    elif letra in "Gg": 
        senha = senha + "¨"
    elif letra in "Bb": 
        senha = senha + "5"
    elif letra in "m": 
        senha = senha + "+"
    elif letra in "n": 
        senha = senha + "^"
    elif letra in "r": 
        senha = senha + "~"
    elif letra in "Ll": 
        senha = senha + "11"
    else: senha = senha + letra


# Impressão da Nova senha
print ("Nova senha criada com Sucesso!!!!!")

if validacao == 1:
    print ("Sua Nova Senha é: ",senha)
else:
    print ("Sua Nova Senha é: ",senha1)

# Finalização do Programa
while True:

    sair = str( input( 'PRESSIONE "ENTER" PARA SAIR ' ) )

    if not sair:

        exit()




