lista = [0,1,2,3,4,5,6,7,8,9,45,11,12,13,14,15,16,17,18,19,20]



def maior_numero(lista):
    temp = 0
    for numero in lista:        
        if numero > temp:
            temp = numero

    return temp

resposta = maior_numero(lista)
print(resposta)

def soma_and_media(lista):
    soma = sum(lista)
    media = round(soma / len(lista), 2)
    return soma, media

resposta2, resposta2_1 = soma_and_media(lista)
print (resposta2, resposta2_1) 


def adicionar_n_lista ():
    lista = []
    for numero in range(0,51):
        lista.append(numero)
    return lista

new_lista = adicionar_n_lista()


def print_impar (lista):
    for numero in lista:
        if numero % 2 != 0:
            print(numero)

print_impar(new_lista)


