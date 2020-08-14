valor = 11
while int(valor) < 0 or int(valor) > 10:
    valor = input ("Digite uma nota: ")
    if int(valor) < 0 or int(valor) > 10:
        print ("Nota Inválida, Digite Novamente")
print ("Nota Válida!!")
