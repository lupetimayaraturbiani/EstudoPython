nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

doenca = input("Possui uma doença infecto-contagiosa? ").upper()

if idade >= 65:
    print("O paciente " + nome + " possui atendimento prioritário")
elif doenca == "SIM":
    print("O paciente " + nome + " deve ser isolado")
else: 
    print("O paciente " + nome + " não possui atendimento prioritário e pode ficar na sala de espera conjunta")