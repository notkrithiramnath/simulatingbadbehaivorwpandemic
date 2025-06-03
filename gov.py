class gov:
    def __init__(self, name, population,initialinf,GDP,lockdownthreshold,quarantine):
        self.name = name
        self.lockdown = False
        self.lockdownpolicy = True
        self.mask = False
        self.populationnum = population
        self.initialinf = initialinf
        self.GDP = GDP
        self.lockdownthreshold = lockdownthreshold
        self.quarantine = quarantine
        #self.populationlist = []
    def lockdowntoday(self,Stats,Sim):
        if self.lockdownpolicy:
            number = (len(Sim.Population)*self.lockdownthreshold)/100#number of people sick to detirmine lockdown
            if Stats.infections >= number:
                self.lockdown =  True
            else:
                self.lockdown = False

    def calcGDP(self,population):
        if not self.lockdown:
            for i in population:
                if i.caninfect:
                    self.GDP+=1



class USAgov(gov):
    def __init__(self,name,population,initialinf,GDP,lockdownthreshold,quarantine):
        super(USAgov, self).__init__(name, population, initialinf,GDP,lockdownthreshold,quarantine)
#
#     def whoami(self):
#         print("I AM AMERICA")
#
# class wakanda(gov):
#     def __init__(self,name,lockdown,mask,population,initialinf,GDP):
#         super(USAgov, self).__init__(name, population, initialinf,GDP)

