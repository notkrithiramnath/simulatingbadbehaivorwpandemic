import Stats
import random

class Citizen:
    def __init__(self, name, friends,mygov,Stats,escape):
        self.name = name
        self.friends = friends


        self.friendslist = []
        self.friendsmeetingtoday = []
        self.dayssick = 0

        self.mygov = mygov
        self.fearofp = False
        self.fearofv = False
        self.dayssincesick = 0
        self.cangetbsick = True
        self.daycured = -5
        self.daydying = -5
        self.caninfect = True
        self.Stats = Stats
        self.escapeprob = escape
        self.rvalue = 0
        self.symptomslength = 0
        self.incubationlength = 0
        self.infectedme = -1
        self.immunitydays = 0
        self.symptomatic = False
        self.viruslist = []
    def calcdayssincesick(self,daynum):
        self.dayssincesick = daynum - self.daycured

    def detirminesicknesslength(self):

        self.symptomslength = random.randint(0,self.virus.maxsymptoms)
        self.incubationlength = random.randint(self.virus.minincubation,self.virus.maxincubation)

    def immunity(self):

        if self.daycured >0:
            if self.dayssincesick >= self.immunitydays:
                self.cangetsick = True
            else:
                 self.cangetsick = False

    def printme(self):
        realfriends = []
        for i in self.friendslist:
            realfriends.append(i.name)
        print(str(self.name)+" "+str(realfriends)+" sick? "+str(self.infected)+" can infect? "+str(self.caninfect)+" can get sick "+str(self.cangetsick)+" days sick: "+str(self.dayssick)+" daycured: "+str(self.daycured)+" day dying "+str(self.daydying)+" who infectedme: "+str(self.infectedme))

    def fvinfect(self):
        if self.infected == False:

    def friendmake(self, Persons,bubblelst):
        if self.name % self.friends == 0:
            #for i in range(self.friends-1):#of fiends -1
            #if person is evenly split
            for friendnum in range(self.name+1,self.name+self.friends):

                if friendnum < len(Persons):#make sure its less than the #of ppl
                    try:
                        self.friendslist.append(Persons[friendnum])#adding to the persons friends
                        Persons[friendnum].friendslist.append(self)
                    except:
                        print("EROROROROROROORORR")
            bubble1 = self.friendslist.copy()
            bubble1.append(self)
            bubblelst.append(bubble1)
        else:
            i = self.friendslist[0]#swapping friends so that anchor friendlist = everyone else
            for friend in i.friendslist:
                if friend.name != self.name:
                    self.friendslist.append(friend)
        #print("making friends")
        #self.printme()




    def incubation(self):
        if self.infected:
            if self.dayssick <= self.incubationlength:
                self.caninfect = True
                self.symptomatic = False
            if self.dayssick > self.incubationlength:
                self.caninfect = True
                self.symptomatic = True

    def escape(self,Sim):
        num = random.uniform(0.0,1.0)
        if num <= self.escapeprob:
            self.infect(Sim)


    def setinfect(self,friend,Sim):
        if fearofpvirus in friend.viruslist and fearofpvirus not in self.viruslist:
            willinfect = random.uniform(0.0, 1.0)
            if willinfect <= Sim.fearofpvirus.contagiousness:
                self.viruslist.append(fearofpvirus)
        if fearofvvirus in friend.viruslist and fearofvirus not in self.viruslist:
            willinfect = random.uniform(0.0, 1.0)
            if willinfect <= Sim.fearofvvirus.contagiousness:
                self.viruslist.append(fearofvvirus)
        if badvirus in friend.viruslist and (fearofpvirus not in self.viruslist and fearofvirus not in self.viruslist) and badvirus not in self.viruslist:
            willinfect = random.uniform(0.0, 1.0)
            if willinfect <= Sim.badvirus.contagiousness:
                self.viruslist.append(badvirus)

        # if a.infected and a.symptomatic:
        #     num = random.uniform(0.0,1.0)
        #     if num > self.escapeprob:
        #         return
        #         # if people are symptomatic and quarantine is true, then there is a chance people will not abide by the rules
        # if a.infected and not b.infected and b.cangetsick and a.caninfect and self.fearofp == False and self.fearofv == False:
        #     willinfect = random.uniform(0.0, 1.0)
        #     if willinfect <= Sim.virus.contagiousness:
        #         b.infected = True
        #         b.infectedme = a.name
        #         b.caninfect = True
        #         a.rvalue += 1
        #         b.detirminesicknesslength()
        #         die = random.uniform(0.0, 1.00)
        #         if die <= b.virus.mort:
        #             b.daydying = random.randint(b.incubationlength, b.symptomslength + b.incubationlength)

    def findfriendsmeetingtoday(self):
        self.friendsmeetingtoday = []
        for friend in self.friendslist:
            chance = random.uniform(0.0,1.0)
            if chance <= .5:
                self.friendsmeetingtoday.append(friend)
    # def detirminewillinfect(infecter,victim,Sim):
    #     if infecter.infected and not victim.infected and victim.cangetsick and infecter.caninfect:
    #         willinfect = random.uniform(0.0, 1.0)
    #         if willinfect <= Sim.virus.contagiousness:
    def infect(self,Sim):
        self.findfriendsmeetingtoday()
        for i in range(self.friends):
            chance = random.uniform(0.0, 1.0)

            if chance <= Sim.bubblescape  :
                person = self.name

                while person == self.name:

                    person = random.randint(1, len(Sim.Population)-1)

                victm = Sim.Population[person]
                self.setinfect(victm,self,Sim)

                self.setinfect(self,victm,Sim)

                self.Stats.meetings +=1
                self.mygov.GDP +=1
        for i in self.friendsmeetingtoday:

            self.setinfect(i, self, Sim)
            self.setinfect(self, i, Sim)
        self.Stats.meetings += len(self.friendsmeetingtoday)



    def daysick(self):
        if self.infected == True:
            self.dayssick+=1


    def cure(self,daynum):
        if self.infected and self.dayssick >= self.symptomslength+self.incubationlength:
            self.infected = False
            #self.caninfect = False
            #print("someone cured "+str(self.name))
            self.dayssick = 0
            self.daycured = daynum
            self.immunitydays = random.randint(0, self.virus.immundays)
            self.symptomatic = False


class American(Citizen):


    def whoami(self):
        print("I am an AMERICAN "+str(self.name)+" "+str(self.infected))
class djiboutian(Citizen):
    def whoami(self):
        print(" I AM DJIBOUTIAN")
# def meetfriends():
# def friendmake(i, pop):
#     return None
