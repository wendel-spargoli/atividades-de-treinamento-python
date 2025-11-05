#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peixes_peso = int(input("Quantos quilos de peixe você trouxe hoje? "))
limite_peso = 50

if peixes_peso > limite_peso:
    excesso = peixes_peso - limite_peso
    print(f"Você trouxe {excesso}Kg de peixe a mais que o limite permitido.\nVocê terá que pagar o valor de {excesso * 4} reais por multa compensatória.")
else:
    print("Sem pendências. Você não tem excesso de peixe!")