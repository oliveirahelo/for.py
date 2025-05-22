numero = int(input(" Digite seu numero: "))
comeco = int(input("Digite o numero que devera começar: "))
fim = int(input(" Digite ate qual numero deverar ser multiplicado: "))

for i in range(comeco, fim):
    print(f" {i} x {numero} = {i * numero}")