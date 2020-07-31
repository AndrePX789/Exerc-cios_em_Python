def F_duplo (peso):
    if peso <= 5:
        valor = peso * 4.90
    else:
        valor = peso * 5.80
    return valor

def alcatra (peso):
    if peso <= 5:
        valor = peso * 5.90
    else:
        valor = peso * 6.80
    return valor

def picanha (peso):
    if peso <= 5:
        valor = peso * 6.90
    else:
        valor = peso * 7.80
    return valor

print("Digite o código da carne: Filé duplo = 1, Alcatra = 2 e Picanha = 3")
cod = input ("Código: ")
quilos = input ("Quantos quilos você vai comprar? ")
pagamento = input ("Você vai pagar com o cartão Tabajara? ")
print ("\n")
cod = int(cod)
quilos = int(quilos)
if cod == 1:
    valor = F_duplo(quilos)
    produto = "Filé Duplo"
elif cod == 2:
    valor = alcatra(quilos)
    produto = "Alcatra"
elif cod == 3:
    valor = picanha(quilos)
    produto = "Picanha"
else:
    print ("Código selecionado inválido")
desc = 0
if pagamento == "S":
    valdesc = valor * 0.95
    desc = valor * 0.05
    round(desc, 2)
    round(valdesc, 2)
else:
    valdesc = valor - desc
    round(valdesc, 2)

print ("Cupom Fiscal: ")
print ("Produto: " + produto)
print ("Quilos: " + str(quilos))
print ("Preço Total: " + str(valor))
print ("Pagamento com cartão tabajara: " + pagamento)
print ("Valor do desconto: " + str(round(desc,2)))
print ("Valor á Pagar: " + str(round(valdesc,2)))

