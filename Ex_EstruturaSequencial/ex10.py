# -*- coding: utf-8 -*-
peso = float(input("Digite o peso do peixe: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("João, você deverá pagar " + "R$" + str(multa) + "  de multa pelos " + str(excesso) + " quilos excedidos")
else: 
    print("Você pescou um peixe de peso regular de acordo com o regulamento: " + str(peso) + " quilos")