import math


class Player:
    def __init__(self, name, level, exp, add_exp):
        self.name = name
        self.level = level
        self.exp = exp
        self.add_exp = add_exp

    def exp(self):
        self.exp += self.add_exp

    def show_stars(self):
        print('Имя игрока ', self.name)
        print('Уровень игрока ', self.level)
        print('Изначальный опыт игрока ', self.exp)
        print('Новый опыт игрока ', self.add_exp)
        
        self.exp += self.add_exp
        print('Текущий опыт ', self.exp)

        while self.level < len(levels) and self.exp >= levels[self.level]:
            self.level += 1
        print('Уровень повышен - Текущий уровень ' ,self.level)
    

class Warrior(Player):
    def __init__(self, name, level, experience, add_exp, weapon, armor):
        super().__init__(name, level, experience, add_exp)
        self.weapon = weapon
        self.armor = armor

    def attack(self):
        while self.level < len(levels) and self.exp >= levels[self.level]:
            self.level += 1
        print('Уровень повышен - Текущий уровень ' ,self.level)
        att = (self.level/2) * self.weapon 
        print('Атака игрока равна ', att)
        print(self.level)

    def defend(self):
        df = math.log(self.exp)*armor
        print('защита')
        print(df)


levels = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]
input_data = input('Имя игрока, его уровень, количество имеющегося опыта, новый опыт, урон от оружия и защита: ')
data = input_data.split()
name = str(data[0])
level = int(data[1])
experience = int(data[2])
add_exp = int(data[3])
weapon = int(data[4])
armor = int(data[5])


def main():
        
    player = Player(name, level, experience, add_exp)
    player.show_stars()
    player = Warrior(name,level,experience,add_exp,weapon,armor)
    player.attack()
    player.defend()

if __name__ == '__main__':
    main()       