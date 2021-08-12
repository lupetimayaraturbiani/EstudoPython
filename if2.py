name = input("Digite o seu nome: ")
idade = int(input("Informe sua idade: "))

doenca = input("Suspeita de doença infecto-contagiosa? S/N  ").upper()


if idade >= 65 and doenca == "S":
    print("O paciente " + name + " deve ir para a sala amarela! - com prioridade")
elif idade < 65 and doenca == "S":
    print("O paciente " + name + " deve ir para a sala amarela! - sem prioridade")
elif idade >= 65 and doenca == "N":
    print("O paciente " + name + " deve ir para a sala branca! - com prioridade")
elif idade < 65 and doenca == "N":
    print("O paciente " + name + " deve ir para a sala branca! - sem prioridade")
else: 
    print("Não foi informada a presença ou não de doença")