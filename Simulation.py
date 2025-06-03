import Stats
import people


class simulation:
    def __init__(self, pop, gov, virus, Stats):
        self.Population = pop
        self.gov = gov
        self.virus = virus
        self.Stats = Stats

    def printeveryone(self):
        for i in self.Population:
            print(str(i.name)+" "+str(i.infected))
    # def makepeople(self,Population,gov):
    #     for person in range(gov.population):
    #         Population.append(person)
    #     return Population
    def makesick(self):
        for i in range(self.gov.initialinf):
            self.Population[i].infected = True
        self.Population[7].infected = True
        self.printeveryone()
    def startsim(self):
        for i in self.Population:
            i.friendmake(self.Population)
            #i.printme()
        self.makesick()

    def runaday(self, daynum, Stats):

        for i in self.Population:
            if self.gov.lockdown() != True:
                i.cure()
                i.meet()

                i.infect()
                if i.infected ==True:
                    i.dayssick +=1

            Stats.meetings += len(i.friendsmeetingtoday)
        for citizen  in self.Population:
            if citizen.infected == True:
                Stats.infections +=1


        print("running day " + str(daynum) + " with "+str(Stats.meetings) + " meetings " + str(Stats.infections))
