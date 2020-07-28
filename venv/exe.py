from genMaraisAuxScorpions import GenMaraisAuxScorpions
from exec.execHistoire import *

# exécution de l'histoire
print("------ Création de 'Le Marais aux scorpions'")
generateur = GenMaraisAuxScorpions()
histoire = generateur.GenererHistoire()
generateur.GenererCaracs() #stocker les caracs dans situation ?
generateur.GenererPersos() #stocker les persos où ?
del generateur # generateur n'est plus utile désormais car tout a été créé
# print(histoire)
execHistoire = ExecHistoire()
execHistoire.LancerHistoire(histoire, "Numéros")
