numeroFunc = int(input("Digite seu numero de funcionario: "))
numeroHoras = int(input("Digite a quantidade de horas trabalhadas: "))
numeroSalario = float(input("Digite o valor do salario por hora: "))

multiplicação = (numeroHoras * numeroSalario)

print(f"NUMERO: {numeroFunc}")
print(f"SALARIO: U$ {multiplicação:.2F}")
