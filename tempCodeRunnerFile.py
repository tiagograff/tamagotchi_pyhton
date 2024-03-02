                # escolhas
                if choice == '1':
                    tamagotchi.food = checkLife(tamagotchi.food + 2)
                    tamagotchi.energy -= 2
                elif choice == '2':
                    tamagotchi.smart = checkLife(tamagotchi.smart + 2)
                    tamagotchi.food -= 1
                    tamagotchi.energy -= 1
                elif choice == '3':
                    tamagotchi.money = checkLife(tamagotchi.money + 3)
                    tamagotchi.food -= 1
                    tamagotchi.energy -= 2
                elif choice == '4':
                    tamagotchi.energy = checkLife(tamagotchi.energy + 3)
                    tamagotchi.food -= 1
                    tamagotchi.money -= 2
                else:
                    print('escolha inválida. tente novamente.')