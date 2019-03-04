class Enemy:
    def __init__(self, x):
        self.energy = x

    def printEnergy(self):
        print(self.energy)

enemyPawn = Enemy(10)
enemyBoss = Enemy(100)

enemyPawn.printEnergy()
enemyBoss.printEnergy()