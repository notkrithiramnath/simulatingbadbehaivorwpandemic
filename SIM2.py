import random
class SIM2:
    def __init__(self, pop, gov, bvirus,fpvirus,fvvirus, Stats, escapeprobability,bubbleescape,debug):
        self.Population = pop
        self.gov = gov
        self.badvirus = bvirus
        self.fearpvirus = fpvirus
        self.fearvvirus = fvvirus
        self.Stats = Stats
        self.escape = escapeprobability
        self.bubbles = []
        self.clnbubbles = []
        self.numsickpeople = 0
        self.bubblescape = bubbleescape
        self.peak = -5
        self.peakday = -5
        self.debug = debug
        self.lastday = 365

    def printeveryone(self):
        for i in self.Population:
            #print(str(i.name)+" "+str(i.infected))
            i.printme()

    def calcpeak(self,daynum):
        temp = self.Stats.infections
        if temp > self.peak:
            self.peak = temp
            self.peakday = daynum
    def startsim(self):
        for i in self.Population:
            i.friendmake(self.Population,self.bubbles)
            #i.printme()
        self.cleanbubbles()
        print(len(self.clnbubbles))
        self.makesick()

    def printday(self,day):
        if not self.debug:
            if day == 0:
                 print("day\tmeetings\tinfections\tGDP\tlockdown?\tDeaths\tPopulation\tcleanbubble")
            #
            print(str(day) + "\t "+ str(self.Stats.meetings) + "\t" + str(self.Stats.infections) +"\t" + str(self.gov.GDP)+"\t"+str(self.gov.lockdown)+"\t"+str(self.Stats.deaths)+"\t"+(str(len(self.Population)))+"\t"+str(len(self.clnbubbles)))


        else:
            print("running day " + str(day) + "\tmeetings" + str(self.Stats.meetings) + "\t infections: \t" + str(
        self.Stats.infections) +"\tGDP: " + str(self.gov.GDP)+"\t lockdown today: "+str(self.gov.lockdown)+"\t Deaths: "+str(self.Stats.deaths)+"\t pop"+(str(len(self.Population)))+"\t Cleanbubbles "+str(len(self.clnbubbles)))

    def kill(self,person):
        if person.dayssick ==person.daydying: #FIX MAKE SURE THAT WE SEE IF THEYLL DIE OR NOT THEN CHOOSE A RANDOM DAY
             person.infected = False
             person.caninfect = False
             person.cangetsick = False
             self.Population.remove(person)
             self.Stats.deaths +=1



    def cleanbubbles(self):

        self.clnbubbles = []
        for i in self.bubbles:
            clean = 0
            for person in i:
                if not person.infected:
                    clean+=1
            if clean == len(i):
                self.clnbubbles.append(i)






class randomsim1(basesim):
    def makesick(self):


        for i in self.Population:
            if random.uniform(0.0, 1.00) <= self.gov.initialinf:#if the number is less than the initial infection point
                i.infected = True
                i.dayssick = 1
                i.detirminesicknesslength()
                i.dayssick = random.randint(0,i.symptomslength+i.incubationlength)
                i.infectedme = -5
                die = random.uniform(0.0, 1.00)
                if die <= i.virus.mort:
                    i.daydying = random.randint(i.incubationlength, i.symptomslength + i.incubationlength)
        #self.printeveryone()

    def runaday(self, daynum):
        #self.printeveryone()
        #self.Population[7].printme()
        self.Stats.calcinfectedtoday(self.Population, self.gov)
        self.calcpeak(daynum)
        self.cleanbubbles()

        for i in self.Population:
            if not self.gov.lockdown:
                i.infect(self)
            else:
                i.escape(self)

        for i in self.Population:
            i.daysick()
            i.incubation()
            i.cure(daynum)
            i.calcdayssincesick(daynum)
            i.immunity()
            self.kill(i)

        self.printday(daynum)
        self.gov.lockdowntoday(self.Stats, self)
        if self.lastday == 365:
            if self.Stats.infections == 0:
                self.lastday = daynum-1


        #self.gov.calcGDP(self.Population)



class detsim(basesim):
    # def makesick(self):
    #     for i in range(self.gov.initialinf):
    #         self.Population[i].infected = True
    #     self.Population[7].infected = True
    #     self.printeveryone()

    def runaday(self, daynum, Stats):
        Stats.calcinfectedtoday(self.Population,self.gov)
        self.gov.lockdowntoday(Stats)
        for i in self.Population:
            i.cure()
            i.daysick()
        if not self.gov.lockdown:
            for i in self.Population:
                i.infect()
                Stats.meetings += len(i.friendsmeetingtoday)
        else:
            num = random.randint(1,self.escape)
            if num == 1:
                i.infect()
        print("running day " + str(daynum) + " with " + str(Stats.meetings) + " meetings " + " infections: "+str(Stats.infections)+" "+"GDP loss: "+str(self.gov.GDP)+" "+str(self.gov.lockdown))

    def prints(self):
        print(str(self.gov.GDP) + "\t\t" + str(self.Stats.deaths) + "\t" + str(self.Stats.realr) + "\t" + str(
            self.Stats.peakday) + "\t" + str(self.Stats.peak) + "\t" + str(self.Stats.lastday))

