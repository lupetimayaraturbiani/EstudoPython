# -*- coding: utf-8 -*-
payed_hours = float(input("Quantos reais você ganha por hora: "))

worked_hours = int(input("Quantas horas você trabalhou esse mês: "))

salary = payed_hours * worked_hours

print("O seu salário desse mês será de: " + "R$ " + str(salary))
