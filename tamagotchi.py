# objeto tamagotchi
class Tamagotchi:
    # atributos
    def __init__(self):
        self.age = 0
        self.clean = 20
        self.energy = 20
        self.food = 20
        self.fun = 20
        self.life = True
        self.money = 20
        self.name = ''
        self.smart = 20

    # métodos
    # definir nome do tamagotchi
    def get_name(self):
        name = input('escolha um nome para seu tamagotchi:\n')
        if name == '':
            print('nome inválido')
            self.name = None
        else:
            self.name = name

    # passagem de tempo

    def ageTime(self):
        self.age += 1
        self.clean -= 1
        self.energy -= 1
        self.food -= 1
        self.fun -= 1
        self.money -= 1
        self.smart -= 1
    # definir nome do tamagotchi

    def shower(self):
        self.clean += 2
        self.fun -= 2
    # definir sono do tamagotchi

    def sleep(self):
        self.energy += 3
        self.food -= 1
        self.fun += 1
    # definir fome do tamagotchi

    def eat(self):
        self.food += 2
        self.clean -= 2
        self.energy += 1
        self.fun += 1
        self.money -= 2

    # definir diversão do tamagotchi

    def play(self):
        self.fun += 2
        self.clean -= 2
        self.money -= 3
        self.energy -= 2

    # definir dinheiro do tamagotchi

    def work(self):
        self.money += 3
        self.clean -= 1
        self.fun -= 2
        self.food -= 1
        self.energy -= 2

    # definir inteligência do tamagotchi

    def study(self):
        self.energy -= 2
        self.fun -= 1
        self.smart += 3
        self.food -= 1

    # verificar vida do tamagotchi

    def checkLife(self):
        # se ao menos um valor dos atributos é menos ou igual a zero
        if any(value <= 0 for value in [self.energy, self.clean, self.fun, self.food, self.smart, self.money]):
            self.life = False
            print('o {} morreu :('.format(self.name))

    # definir status do tamagotchi

    def status(self):
        print('status do {}\n'.format(self.name) +
              'idade: {}\n'.format(self.age) +
              'limpeza: {}\n'.format(self.clean) +
              'fome: {}\n'.format(self.food) +
              'diversão: {}\n'.format(self.fun) +
              'dinheiro: {}\n'.format(self.money) +
              'inteligência: {}\n'.format(self.smart))

    # verificar se ultrapassou de 20 caso sim, volta para 20

    def top(self):
        # retorna um dicionário contendo atributos do objeto
        for attribute in self.__dict__:
            # obetendo o valor do atributo dinamicamente
            value = getattr(self, attribute)
            if isinstance(value, int) and value > 20:
                # ajustando caso for maior que 20
                setattr(self, attribute, 20)
