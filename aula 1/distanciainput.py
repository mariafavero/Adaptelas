x1 = int(input("Digite x1: "))
y1 = int(input("Digite y1: "))
x2 = int(input("Digite x2: "))
y2 = int(input("Digite y2: "))

difx = (x2 - x1) ** 2 # "**" exponencial#
dify = (y2 - y1) ** 2 

somadif = difx + dify

result = somadif ** (1/2) #"(1/2)" é para gerar uma raiz quadrada#

print (f"A distancia entre dois pontos e:{result}")