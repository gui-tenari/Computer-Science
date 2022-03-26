# 1. Crie uma função que receba dois números e retorne o maior deles.

from unicodedata import name


def major_one (num1, num2):
    if num1 > num2:
        return (num1)
    else:
        return (num2)


print("Maior numero:", major_one(11,9))

#2. Calcule a média aritmética dos valores contidos em uma lista.

def avarage(list):
    length = len(list)
    total = 0
    for item in list:
        total += item
    return total / length


number_list = [2, 2, 2, 3, 2]

print("Média aritméritca:",avarage(number_list))

# 3. Faça um programa que, dado um valor n qualquer, tal que n > 1 , 
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.

def print_square(number):
    stars = number * '*'
    print('Quadrado de estrelas:')
    for number in range(1, number):
        print(stars)
    return stars


print(print_square(4))

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior 
# quantidade de caracteres.

def major_length_name(list):
    major_name = ''
    for name in list:
        if len(name) > len(major_name):
            major_name = name
        
    return major_name


name_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana", "Guilherme"]

print("O maior nome da lista é: ",major_length_name(name_list))

# 5. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
# é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores
# em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a
# partir do tamanho de uma parede(em m²).

import math

def how_much_paint(meters):
    paint_liters = math.ceil(meters / 3)
    paint_number = math.ceil(paint_liters / 18)

    return ( paint_number, paint_number * 80 )

print(how_much_paint(350))