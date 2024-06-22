print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3

print('~' * 25)
print('{} -> {}'.format(t1, t2), end = ' -> ')

while cont <= n:
    fibonacci = t1 + t2
    print('{}'.format(fibonacci), end = ' -> ')
    t1 = t2
    t2 = fibonacci
    cont += 1
print('FIM')
print('~' * 25)
