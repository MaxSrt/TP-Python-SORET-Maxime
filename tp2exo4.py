base = 4
fromage = 800
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrer le nombre de personne(s) conviées à la fondue : "))
nvfromage = (800*nbConvives)/base
nveau = (2*nbConvives)/base
nvail = (2*nbConvives)/base
nvpain = (400*nbConvives)/base
print("Pour faire une fondue fribourgeoise pour", nbConvives)
print("-", nvfromage, "gr de fromage")
print("-", nveau, "dl d'eau")
print("-", nvail, "gousee(s) d'ail")
print("-", nvpain, "gr de pain")