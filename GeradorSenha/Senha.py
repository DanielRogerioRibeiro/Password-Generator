# Este é um Gerador de senha para criação de Senhas a partir do método de Substituição de Palavra dada pelo Usuário
# Por Segurança a senha deve possuir 8 a 12 caracteres não especiais
# A palavra base deverá conter letras Maiuscúlas e Minuscúlas
# Não utilize Data de Nascimento/Nome/Sobrenome

print ("Olá, Seja Bem Vindo ao Gerador de Senha.")
chave = input ("Por favor digite uma palavra Chave para a sua senha: ")

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
    elif letra in "": 
        senha = senha + "$"
    else: senha = senha + letra

print ("Sua Nova Senha é: ", senha)

