#calculando IMC
#informações do usuario
peso=int(input('digite o seu peso em quilogramas (kg): '))
altura=float(input('digite a sua altura em metros (m): '))

#calculo do IMC
imcCalculado = peso/(altura**2)
print(f'seu IMC (kg/m²) é de: {imcCalculado:.2f}')

#classificação na tabela
if imcCalculado < 18.5:
    print('classificação: abaixo do peso')
elif 18.6 <= imcCalculado < 24.9:
    print('classificação: peso normal')
elif 25 <= imcCalculado < 29.9:
    print('classificação: sobrepeso')
elif 30 <= imcCalculado < 34.9:
    print('classificação: obesidade grau 1')
elif 35 <= imcCalculado < 39.9:
    print('classificação: obesidade grau 2')
else:
    print('classificação: obesidade grau 3')