num1 = int(input("Digite um numero inteiro: "))

def tabuada (num):
    print (f"Tabuada do {num}: ")
    for i in range(0,11):
        mult = num * i
        print(f"{num} X {i} = {mult}")

tabuada(num1)