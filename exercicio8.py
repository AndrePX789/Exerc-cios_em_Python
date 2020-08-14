validador = True
while validador:
    nome = input ("Digite seu nome: ")
    if len(nome) < 3:
        print ("Nome Inválido, digite novamente!!")
    else:
        validador = False

validador = True
while validador:
    idade = input ("Digite sua idade: ")
    if int(idade) < 0 or int(idade) > 150:
        print ("Idade Inválida, digite novamente!!")
    else:
        validador = False

validador = True
while validador:
    salario = input ("Digite o seu salario: ")
    if int(salario) < 0 :
        print ("Salario Inválido, digite novamente!!")
    else:
        validador = False

validador = True
while validador:
    sexo = input ("Digite seu sexo: ")
    if sexo != 'f' and sexo != 'm':
        print ("Sexo Inválido, digite novamente!!")
    else:
        validador = False

validador = True
while validador:
    estado_Civil = input ("Digite seu estado Civil: s, c, v, d ")
    if estado_Civil != 's' and estado_Civil != 'c' and estado_Civil != 'v' and estado_Civil != 'd':
        print ("Estado Civil Inválido, digite novamente!!")
    else:
        validador = False