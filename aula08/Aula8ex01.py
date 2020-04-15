'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
'''

from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num) #quando importa uma func somente de uma biblioteca, para utiliza-lá não precisa o nome da biblioteca
print('A raiz quadrada de {} é igual a {}'.format(num, ceil(raiz)))
