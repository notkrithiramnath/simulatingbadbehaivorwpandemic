import random
class randomizer:
    def __init__(self,government,virus ):
        self.government = government
        self.virus = virus
    def randomizevirusincubation(self):
        self.virus.incubation = random.randint(6,14)