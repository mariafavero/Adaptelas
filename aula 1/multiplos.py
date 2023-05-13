A = int(input("Adicione um numero: "))
B = int(input("Adicione um numero: "))

if(A>B):
    max = A
    min = B
else:
    max = B
    min = A

divSimpl = max/min
divInt = max//min
if(divSimpl == divInt):
    print(f"Multiplos")
else:
    print(f"Nao multiplos")

