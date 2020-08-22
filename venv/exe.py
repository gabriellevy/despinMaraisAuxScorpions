from genMaraisAuxScorpions import GenMaraisAuxScorpions
from exec.execHistoire import *
from exec.situation import *

# exécution de l'histoire
print("------ Création de 'Le Marais aux scorpions'")
situation = Situation()
generateur = GenMaraisAuxScorpions()
histoire = generateur.GenererHistoire()
perso = generateur.GenererCaracs() #stocker les caracs dans situation ?
#generateur.GenererPersos() #stocker les persos où ?
del generateur # generateur n'est plus utile désormais car tout a été créé
# print(histoire)
execHistoire = ExecHistoire()
execHistoire.LancerHistoire(histoire, "Numéros", "20")
