def alcool (litros):
    if litros < 21:
        valor = litros * (1.90 - (1.90 * 0.03))
    else:
        valor = litros * (1.90 - (1.90 * 0.05))
    return round(valor, 2)

def gasolina (litros):
    if litros < 21:
        valor = litros * (2.50 - (2.50 * 0.04))
    else:
        valor = litros * (2.50 - (2.50 * 0.06))
    return round(valor, 2)

combustivel = input ("Se for gasolina digite G, se for Alcool digite A: ")
litros = input ("Quantos litros você vai abastecer? ")
litros = float(litros)

if combustivel == "G":
    valor = gasolina(litros)
elif combustivel == "A":
    valor = alcool(litros)
else:
    print("Tipo de combustível Inválido!!")

print ("Você ira pagar " + str(valor) + " Reais em combustível!!")