#tabuada usando for
num=int(input('digite o número para calcular a tabuada: '))

for i in range(1, 11):
    print(f'{num} x {i:2} = {num*i:2}')