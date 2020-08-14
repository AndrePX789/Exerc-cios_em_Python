validador = True
while validador:
    pais_A = input ("Digite a população do Pais A: ")
    if int(pais_A) <= 0:
        print ("População Inválida, Digite novamente")
    else:
        validador = False

validador = True
while validador:
    taxa_A = input ("Digite a taxa de crescimento do  Pais A: ")
    if int(taxa_A) <= 0:
        print ("Taxa Inválida, Digite novamente")
    else:
        validador = False
taxa_A = int(taxa_A) / 100

validador = True
while validador:
    pais_B = input ("Digite a população do Pais B: ")
    if int(pais_B) <= 0:
        print ("População Inválida, Digite novamente")
    else:
        validador = False

validador = True
while validador:
    taxa_B = input ("Digite a taxa de crescimento do  Pais B: ")
    if int(taxa_B) <= 0:
        print ("Taxa Inválida, Digite novamente")
    else:
        validador = False
taxa_B = int(taxa_B) / 100

anos = 0
while pais_A < pais_B:
    pais_A = int(pais_A * taxa_A)
    pais_B = int(pais_B * taxa_B)
    anos += 1
print(pais_A)
print(pais_B)
print(anos)