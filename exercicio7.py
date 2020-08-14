validador = 0

while validador == 0:
    usuario = input ("Digite o seu Login: ")
    senha = input ("Digite uma Senha: ")
    if usuario == senha:
        print("A sua senha não pode ser igual ao seu login!!!, digite novamente! ")
    else:
        validador += 1
print ("Você foi cadastrado com sucesso!!!!")