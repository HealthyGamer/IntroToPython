class Player:
    def __init__(self, id, xp=0, attack=0, hp=0):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.hp = hp

    def isNewPlayer(self):
        return True

    def isAlive(self):
        return True

    def attack(self):
        return 1

    def takeDamage(self):
        return self.isAlive()

    def updateHealth(self):
        return self.isAlive()

    def loadPlayer(self):
        return True


class Mob:
    def __init__(self):
        self.hp = 10
        self.attack = 1

    def isAlive(self):
        return True
