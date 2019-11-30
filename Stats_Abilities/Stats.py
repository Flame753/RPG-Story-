from Stats_Abilities.Vitality import Vitality
from Stats_Abilities.Magic import Magic
from Stats_Abilities.Defense import Defense
from Stats_Abilities.Agility import Agility
from Stats_Abilities.Strength import Strength


class Stats(Vitality, Strength, Defense, Magic, Agility):
    def __init__(self, vitality=0, strength=0, defense=0, magic=0, agility=0):
        Vitality.__init__(self)
        Strength.__init__(self)
        Defense.__init__(self)
        Magic.__init__(self)
        Agility.__init__(self)
        self.vitality = vitality
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.agility = agility

    def set_vitality(self, vitality):
        self.vitality = vitality

    def get_vitality(self):
        return self.vitality

    def set_strength(self, strength):
        self.strength = strength

    def get_strength(self):
        return self.strength

    def set_defense(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense

    def set_magic(self, magic):
        self.magic = magic

    def get_magic(self):
        return self.magic

    def set_agility(self, agility):
        self.agility = agility

    def get_agility(self):
        return self.agility

    @classmethod
    def get_all(cls):
        return[cls.vitality, cls.strength, cls.defense, cls.magic, cls.agility]

if __name__ == '__main__':
    # st1 = Stats()
    print(help(Stats()))
    # st1.set_dodge(4)
    # print("st1 dodge is: {}".format(st1.get_dodge()))
    # st1.set_health(2)
    # print(st1)