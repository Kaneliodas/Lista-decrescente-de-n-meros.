#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


# Comparação para encontrar o maior número
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3
#Descobrindo o menor número
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3
#Achar o número mediano
if num1 != maior and num1 != menor:
    meio = num1
elif num2 != maior and num2 != menor:
    meio = num2
else:
    meio = num3
# Exibição dos números
print("O maior número é:", maior)
print("O mediano número é:", meio)
print("O menor número é:", menor)
