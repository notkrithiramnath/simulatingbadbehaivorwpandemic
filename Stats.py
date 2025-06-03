class Stats:
    def __init__(self,meetings,infections,rvalue):
        #self.totalmeet =
        self.infections = infections
        self.meetings = meetings
        self.rvalue = rvalue
        self.peoplesick = 0
        self.deaths = 0
        self.totalr = 0
        self.realr = 0


    def calcinfectedtoday(self,population,gov):
        self.infections = 0
        for i in population:
            if i.infected == True:
                self.infections += 1

    def calcrvalue(self,bubblelist):

        for bubble in bubblelist:
            for person in bubble:
                self.totalr +=person.rvalue
        self.realr = self.totalr/(len(bubblelist)*len(bubblelist[1]))

