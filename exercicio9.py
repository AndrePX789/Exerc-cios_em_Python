pais_A = 80000
taxa_A = 1.03
pais_B = 200000
taxa_B = 1.015
anos = 0
while pais_A < pais_B:
    pais_A = int(pais_A * taxa_A)
    pais_B = int(pais_B * taxa_B)
    anos += 1
print(pais_A)
print(pais_B)
print(anos)