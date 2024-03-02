import tamagotchi as game
# pausa para continuar


def pause():
    input('\naperte qualquer tecla "enter" para continuar\n')


# rodando o jogo
if __name__ == "__main__":
    print('bem vind@ ao tamagotchi game em python')
    tamagotchi = game.Tamagotchi()
    tamagotchi.get_name()
    if tamagotchi.name is not None and tamagotchi.name != '':
        print('vamos começar o jogo!')
        while tamagotchi.life == True:
            choice = input('qual destas opções você deseja escolher?\n' +
                           '1. tomar banho\n' +
                           '2. dormir\n' +
                           '3. comer\n' +
                           '4. brincar\n' +
                           '5. trabalhar\n' +
                           '6. estudar\n')

            if choice == '1':
                tamagotchi.shower()
            elif choice == '2':
                tamagotchi.sleep()
            elif choice == '3':
                tamagotchi.eat()
            elif choice == '4':
                tamagotchi.play()
            elif choice == '5':
                tamagotchi.work()
            elif choice == '6':
                tamagotchi.study()
            else:
                print('\nvalor inválido, tente novamente\n')

            tamagotchi.ageTime()
            tamagotchi.top()
            tamagotchi.status()
            tamagotchi.checkLife()
            pause()
    print('\n\nsua pontuação foi de: {} pontos\n\n'.format(tamagotchi.age * 10))
