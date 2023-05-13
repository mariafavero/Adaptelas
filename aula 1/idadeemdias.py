dias = int(input("Digite a quantidade de dias: "))

anos = dias//365 #"// são para respostas com numeros inteiros"
dias -= (anos * 365) #"-= significa dias = dias - (anos*365)"
meses = dias//30
dias -= (meses * 30)

print(f"{anos} ano (s)\n{meses} mes (es)\n{dias} dias (s)")