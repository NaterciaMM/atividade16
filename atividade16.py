# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

altura = float(input("insira sua altura: "))
peso = float(input("insira seu peso: "))

indmassa = (altura*altura)/peso

if indmassa <18.5:
    print("abaixo do peso ")
elif 18.5 <= indmassa <25:
    print("peso ideal ")
if 25<= indmassa <30:
    print("sobrepeso")
elif indmassa >=30:
    print("obesidade")
