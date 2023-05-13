total = int(input("adicione um valor: " ))

#nNotas100 = total//100
#total -= (nNotas100 * 100)
#nNotas = total//50

#print(f"numeros de notas 100: {nNotas100} total {total}")

nota100 = total//100
total -= (nota100 * 100)
nota50 = total//50
total -= (nota50 * 50)
nota20 = total//20
total -= (nota20 * 20)
nota10 = total//10
total -= (nota10 * 10)
nota5 = total//5
total -= (nota5 * 5)
nota2 = total//2
total -= (nota2 * 2)
nota1 = total

print(f"{nota100} nota (s) de R$ 100,00\n{nota50} nota (s) de R$ 50,00\n{nota20} nota (s) de R$ 20,00\n{nota10} nota (s) de R$ 10,00\n{nota2} nota (s) de R$ 2,00\n{nota1} nota (s) de R$ 1,00")