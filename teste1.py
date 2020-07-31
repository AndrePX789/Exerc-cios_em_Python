notas = [100, 50, 20, 10, 5, 2, 1]
def sacar_dinheiro (valor):
    notas_dinheiro = []
    i = 0
    for i in range(0, 7):
        conta = int(valor / notas[i])
        notas_dinheiro.append(conta)
        valor = valor - (conta * notas[i])
        
    
    palavras = ["Você vai receber ", "nota de ", " notas de ", ", ", " e ", " !!"]
    frase = [palavras[0]]

    for j in range(0,7):
        if notas_dinheiro[j] > 0:
            frase.append(notas_dinheiro[j])
            if notas_dinheiro[j] > 1:
                frase.append(palavras[2])
            else:
                frase.append(palavras[1])
            frase.append(notas[j])    
            frase.append(palavras[3])
    frase.append(palavras[5])
    print (frase)








dinheiro = input("Quanto você quer sacar? ")
if int(dinheiro) > 9 and int(dinheiro) < 1000:
    dinheiro = int(dinheiro)
    sacar_dinheiro(dinheiro)
else:
    print ("Você deve pedir um valor entre 10 a 600 reais!!") 