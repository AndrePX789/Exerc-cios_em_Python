int1 = int(input("Digite um Número Inteiro "))
int2 = int(input("Digite outro número Inteiro "))

lista = []
def intervalo (num1, num2):
    lista = []
    for numero in range(num1, num2 + 1):
        lista.append(numero)
    return lista

lista = intervalo(int1, int2)
print (lista)