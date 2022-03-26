# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa
#  que lê todas essas informações e filtre mantendo somente as pessoas que estão reprovadas, e
#  escreva seus nomes em outro arquivo. A nota miníma para aprovação é 6.

with open("grades.txt", mode="r") as grades:
    reproved = open("reproved.txt", mode="w")
    for line in grades:
        student = line.split(" ")
        if int(student[1]) < 6:
            print(student[0], file=reproved)

  