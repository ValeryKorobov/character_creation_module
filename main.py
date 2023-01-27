from random import randint

DEFAULT_ATTACK = 5  # Constant - the standard number of attack points.
DEFAULT_DEFENCE = 10  # Constant - the standard number of defence points
DEFAULT_STAMINA = 80  # Constant - standard stamina points.


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)  # Range of attack points.
    RANGE_VALUE_DEFENCE = (1, 5)  # Range of defence points.
    SPECIAL_SKILL = 'Удача'  # Skill name constant.
    SPECIAL_BUFF = 15  # Constant value of damage points.

    def __init__(self, name):
        self.name = name

    def attack(self):
        """Apply character attack"""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}.')

    def defence(self):
        """Apply character protection"""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        """Apply special skill character"""
        return (f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    def __str__(self):
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.')


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Returns a string with the selected
        character class."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа,'
                               ' за которого хочешь играть: Воитель — warrior,'
                               ' Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)

        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character) -> str:
    """Takes a character's name and class as input.
    Returns messages about the results of a character's training cycle."""
    commands = {'attack': character.attack(),
                'defence': character.defence(),
                'special': character.special()}
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введите комманду: ')
        if cmd in commands:
            print(f'{commands[cmd]()}')


if __name__ == '__main__':
    def main() -> str:
        print('Приветствую тебя, искатель приключений!')
        print('Прежде чем начать игру...')
        char_name: str = input('...назови себя: ')
        print(f'Здравствуй, {char_name}!'
              ' Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
        print('Ты можешь выбрать один из трёх путей силы:')
        print('Воитель, Маг, Лекарь')
        char_class: str = choice_char_class()
        print(start_training(char_name, char_class))
