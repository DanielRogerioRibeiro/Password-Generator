# Este é um Gerador de senha para criação de Senhas a partir do método de Substituição de Palavra dada pelo Usuário
# Por Segurança a senha deve possuir 8 a 12 caracteres não especiais
# A palavra base deverá conter letras Maiúsculas e Minúsculas
# Não utilize Data de Nascimento/Nome/Sobrenome

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
    
    senha1 = ""
    for letra in chave1:
        if letra in "a":
            senha1 = senha1 + "@"
        elif letra in "E": 
            senha1 = senha1 + "3"
        elif letra in "e": 
            senha1 = senha1 + "&"
        elif letra in "Ii": 
            senha1 = senha1 + "!"
        elif letra in "Oo": 
            senha1 = senha1 + "0"
        else: senha1 = senha1 + letra
  
# Catálogo de Substituição de Letras

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
    elif letra in "S": 
        senha = senha + "$"
    elif letra in "s": 
        senha = senha + "§"
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


print ("Nova senha criada com Sucesso!!!!!")

if validacao == 1:
    print ("Sua Nova Senha é: ",senha)
else:
    print ("Sua Nova Senha é: ",senha1)


