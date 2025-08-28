#tabuada com while
num=int(input('digite o número para o calculo da tabuada: '))
contador=1
while contador <=10:
    print(f'{num} x {contador:2} = {num*contador:2}')
    contador +=1