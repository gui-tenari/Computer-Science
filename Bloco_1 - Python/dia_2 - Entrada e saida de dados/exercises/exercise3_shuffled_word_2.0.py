import random

with open('words.txt', 'r') as words_list:
    words = [word.split('\n')[0] for word in words_list.readlines()]
    word = random.choice(words)
    print(word)
    shuffled_word = "".join(random.sample(word, len(word)))
    attempts_left = 3

    print(f"PALAVRA EMBARALHADA: {shuffled_word}")

    while attempts_left > 0:
        inputted_answer = input("Digite seu palpite: ")
        if(inputted_answer == word):
            print(f"Parabéns, você acertou a palavra! A resposta era {word}")
            break
        else:
            attempts_left -= 1
            print(f"Tente denovo, você tem {attempts_left} tentativas restantes")
            if attempts_left == 0:
                print(f"Não foi dessa vez! A palavra era {word}")