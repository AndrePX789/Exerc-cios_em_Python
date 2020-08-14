def maça (quilos):
    if quilos < 6:
        valor = quilos * 1.80
    else:
        valor = quilos * 1.50
    return round(valor, 2)

def murango (quilos):
    if quilos < 6:
        valor = quilos * 2.50
    else:
        valor = quilos * 2.20
    return round(valor, 2)

def desconto (quilos, valores):
    if quilos > 8 or valores > 25:
        vtotal = valores * 0.90
        return round(vtotal, 2)
    return valores

maca = input ("Quantos quilos de Maçã você vai comprar? ")
morango = input ("Quantos quilos de Morango você vai comprar? ")

vmaca = maça(float(maca))
vmorango = murango(float(morango))
tkilos = float(maca + morango)
tvalor = vmaca + vmorango
vtotal = desconto(tkilos, tvalor)

print ("Você ira pagar ao todo " + str(vtotal) + " Reais !!")

