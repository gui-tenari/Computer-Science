# Exercício 2: Escreva um programa que receba vários números naturais e calcule a soma desses
#  valores. Caso algum valor da entrada seja inválido, por exemplo uma letra, uma mensagem deve
# ser exibida, na saída de erros, no seguinte formato: "Erro ao somar valores, {valor} é um
# valor inválido". Ao final, você deve imprimir a soma dos valores válidos.

from curses.ascii import isdigit


numbers = input("digite seus numeros separados por espaço:")

splited_numbers = numbers.split(" ")

total = 0

for number in splited_numbers:
    if isdigit(number):
        total += int(number)
    else:
        print (f"Erro ao somar valores, {number} é um valor inválido")
    
    
print(f"A soma dos valores é: {total}")


try:
    arquivo = open("arquivo.txt", "w")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")
