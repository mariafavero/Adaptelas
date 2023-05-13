segundos = int(input("Digite seu valor em segundos para a conversao: "))

horas = segundos//3600
segundos -= (horas * 3600)
minutos = segundos//60
segundos -= (minutos * 60)


print(f"{horas}:{minutos}:{segundos}")