class virus:
    def __init__(self, name, rval, incubation, mort,immundays,symptoms,contagiousness,minincubation):
        self.name = name
        self.rval = rval
        self.maxincubation = incubation
        self.mort = mort
        self.immundays = immundays
        self.maxsymptoms = symptoms
        self.contagiousness = contagiousness
        self.minincubation = minincubation
    # infect


# class covid(virus):
#     def __init__(self):
#         #name = covid, rval = 5, incubation = 7, mortality prob =  -1, immune days after getting better = 30
#         super().__init__("covid",5,7,-1,30)

