

import random as random
import Simulation
import gov
import people
import virus
import Stats
import SIM2
from gov import USAgov

Population = []

#INDEPENDENT VARIABLES
#SIMULATION VARIABLES0
POPULATIONNUM = 10000
INITIALINFECTIONS = .5 #probability someone will be initially infected
NUMBEROFDAYS =365 #number of days the simulation is run
ESCAPEPROBABILITY = 0.01 #1 out of chance someoen will escape lockdown 0.1 default
BUBBLESCAPE = 0.01#chance somoene will escape bubble 0.01 default
#GOV VARIABLES
LOCKDOWNTHRESHOLD =.1 #percentage of population infected before lockdown initiatted
QUARANTINE = False
#QUARANTINE = False
#POPULATION VARIABLEA
NUMBEROFFRIENDS = 10 #AVERAGE number of friends per person

#VIRUS VARIABLEs
CONTAGIOUSNESS = 0.5#pROBABILITY you will get infected if you meet a sick person
MORTALITYRATE = 0.034 #probability  of PEOPLE WHO WILL DIE IF THEY GET SICK
MININCUBATION = 2
INCUBATIONPERIOD = 7#AVERAGE NUMBER OF DAYS before disease becomes symptoms
SYMPTOMSPRESENT = 14#when they have to stay home
IMMUNEDAYS = 90 #Average of of days you are immune once you get sick

DEBUG = False

#Independent variables
# Name = USA, Population = 100, Initial infected 20, GDP = 0

US = gov.USAgov("USA",POPULATIONNUM,INITIALINFECTIONS, 0,LOCKDOWNTHRESHOLD,QUARANTINE)
covid = virus.virus("covid", CONTAGIOUSNESS, INCUBATIONPERIOD, MORTALITYRATE, IMMUNEDAYS,SYMPTOMSPRESENT,CONTAGIOUSNESS,MININCUBATION)
stats2 = Stats.Stats(0,0,0)
for i in range(POPULATIONNUM):
    american = people.American(i, NUMBEROFFRIENDS, False, False, [], [],US,covid,stats2,ESCAPEPROBABILITY)
    Population.append(american)

realsim = SIM2.randomsim1(Population,US,covid,stats2, 0,BUBBLESCAPE,DEBUG )

seedlist = [20,200,500,22]

#print(realsim.bubbles)
random.seed(22)#making all results always the same
realsim.startsim()
for i in range(NUMBEROFDAYS):
    realsim.runaday(i)
stats2.calcrvalue(realsim.bubbles)
print(str(realsim.gov.GDP) +"\t\t" + str(realsim.Stats.deaths)+"\t"+str(stats2.realr)+"\t"+str(realsim.peakday)+"\t"+str(realsim.peak)+"\t"+str(realsim.lastday))
