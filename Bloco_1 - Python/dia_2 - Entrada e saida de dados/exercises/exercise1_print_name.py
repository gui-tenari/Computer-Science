name = input("digite seu nome: ")

splited_name = list(name)

print(splited_name)

while len(splited_name):
    for letter in splited_name:
        print(letter, end="")

    print("")
    if not len(splited_name):
        break
    splited_name.pop()
    

