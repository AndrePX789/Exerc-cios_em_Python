perguntas = ["Telefonou para a vitíma?", "Esteve no local do crime?", "Mora perto da vitíma?", "Devia para a vitíma?", "Já trabalhou com a vitíma?"]

respostas = []
def detetive (lista):
    aux = 0
    for i in range (0, 5):
        if lista[i] == "S":
            aux += 1
    
    if aux == 2:
        print ("Suspeita!!")
    elif aux == 3 or aux == 4:
        print ("Cúmplice")
    elif aux == 5:
        print ("Assassino")
    else:
        print ("Inocente")

print ("Responda S ou N !!!")

for j in range (0, 5):
    resposta = input (perguntas[j])
    respostas.append(resposta)

detetive(respostas)


