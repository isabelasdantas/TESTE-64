n = int(input('Digite um número: sendo [999 para parar]: '))
soma = soma2 = 0
while n != 999:
    soma2 += n
    n = int(input('Digite um número: sendo [999 para parar] '))
    soma += 1
print('Você digitou {} números e a soma entre eles é: {}.'.format(soma, soma2))
