from gen.gen_histoire import *
from numeros1_50 import *
from numeros51_100 import *
from numeros151_200 import *
from numeros251_300 import *
from random import randrange
from caracLDOELH import CaracLDOELH
from chance import *

class GenMaraisAuxScorpions(GenHist):
    """
    contient ce qui est spécifique à la création de l'histoire du marais au corpions
    pourra éventuellement être divisée entre la génération d'un LDOELH standard et la spécialisation de celui là on verra
    """

    def __init__(self):
        GenHist.__init__(self, "Le marais aux scorpions")

    def GenererHistoire(self):
        self.GenererPreparationAventure()
        self.GenererNumeros()
        return self._m_Histoire

    def GenererPreparationAventure(self):
        self.AjouterEvt("Préparation aventure")
        self.AjouterEffet("Rien à faire ici pour l'instant")

    def GenererNumeros(self):
        self.AjouterEvt("Numéros")
        GenererNumeros1_10(self)
        GenererNumeros41_50(self)

        GenererNumeros91_100(self)

        GenererNumeros271_280(self)
        GenererNumeros291_300(self)


    def GenererCaracs(self):
        """
        génère toutes les caracs qui peuvent être visualisées par le joueur
        (d'autres caracs peuvent être générées et invisibles n'importe quand dans l'aventure)
        """
        perso = GenHist.GenererCaracs(self)
        # note : ce serait mieux de pouvoir tirer au dé pour déterminer ces valeurs
        habilete = 6 + randrange(1,7)
        perso.AjouterCarac(CaracLDOELH.HABILETE, habilete)
        chance = 6 + randrange(1,7)
        perso.AjouterCarac(CaracLDOELH.CHANCE, chance)
        endurance = 12 + randrange(1,7) + randrange(1,7)
        perso.AjouterCarac(CaracLDOELH.ENDURANCE, endurance)

        return perso

    def AjouterEffetTenterLaChanceGoTo(self, texte, id, idGoToChanceux, idGoToMalchanceux, evt = ""):
        effet = self.AjouterEffet(texte, id, evt)
        effet.m_LancerDe = TenterChance( idGoToChanceux, idGoToMalchanceux)
        #hum problème pour avoir une fonction comme membre d'un classe là (plus exécution pas faite...)'

    """
    int endurance = 12 + Aleatoire::GetAl()->D6() + Aleatoire::GetAl()->D6();
    GestCarac::GetGestionnaireCarac()->AjouterCaracNombre(LDOELH::ENDURANCE, endurance, 0, endurance);

    int chance = 6 + Aleatoire::GetAl()->D6();
    GestCarac::GetGestionnaireCarac()->AjouterCaracNombre(LDOELH::CHANCE, chance, 0, chance);

    GestCarac::GetGestionnaireCarac()->AjouterCaracNombre(LDOELH::REPAS, 10, 0, 10);

    Equipement::GetEquipementDepart();
    """
