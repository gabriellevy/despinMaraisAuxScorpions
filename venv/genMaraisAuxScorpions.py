from gen.gen_histoire import *
from numeros1_50 import *
from numeros51_100 import *
from numeros151_200 import *
from numeros251_300 import *
from regles import *
from random import randrange
from caracLDOELH import CaracLDOELH
from caracEndurance import Endurance
from chance import *
from combat import *

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

        self._m_Histoire.m_MessageVictoire = "Vous avez gagné"
        self._m_Histoire.m_MessageDefaite = "Vous êtes mort, votre aventure s'arrête ici..."
        return self._m_Histoire

    def GenererPreparationAventure(self):
        self.AjouterEvt("Préparation aventure")
        GenererRegles(self)

    def GenererNumeros(self):
        self.AjouterEvt("Numéros")
        GenererNumeros1_10(self)
        GenererNumeros11_20(self)
        GenererNumeros21_30(self)
        GenererNumeros31_40(self)
        GenererNumeros41_50(self)

        GenererNumeros91_100(self)

        GenererNumeros191_200(self)

        GenererNumeros271_280(self)
        GenererNumeros291_300(self)


    def GenererCaracs(self):
        """
        génère toutes les caracs qui peuvent être visualisées par le joueur
        (d'autres caracs peuvent être générées et invisibles n'importe quand dans l'aventure)
        """
        perso = GenHist.GenererCaracs(self)
        # note : ce serait mieux de pouvoir tirer au dé pour déterminer ces valeurs
        habileteVal = 6 + randrange(1,7)
        perso.CreerCaracVisible(CaracLDOELH.HABILETE, habileteVal, 0, habileteVal)
        chanceVal = 6 + randrange(1,7)
        perso.CreerCaracVisible(CaracLDOELH.CHANCE, chanceVal, 0, chanceVal)
        enduranceVal = 12 + randrange(1,7) + randrange(1,7)
        enduranceCarac = Endurance(CaracLDOELH.ENDURANCE, enduranceVal, 0, enduranceVal)
        perso.AjouterCaracVisible(enduranceCarac)

        return perso

    def AjouterEffetTenterLaChanceGoTo(self, texte, id, idGoToChanceux, idGoToMalchanceux, evt = ""):
        effet = self.AjouterEffet(texte, id, evt)
        effet.m_LancerDe = TenterChance( idGoToChanceux = idGoToChanceux, idGoToMalchanceux = idGoToMalchanceux)
        return effet

    def AjouterEffetTenterLaChance(self, texte, id, callbackChanceux, callbackMalchanceux, evt = ""):
        effet = self.AjouterEffet(texte, id, evt)
        effet.m_LancerDe = TenterChance(callbackChanceux = callbackChanceux, callbackMalchanceux = callbackMalchanceux)
        return effet

    def AjouterEffetCombat(self, texte, id, nomMonstre, habileteMonstre, enduranceMonstre, goToVictoire, goToDefaite = "",
                           degatsMonstre = 2, pvRestantsMonstreAvantGoToFinal=0, goToEffetIdFuite="", evt = ""):
        """
        gère les combats tant qu'ils ne sont pas trop étranges au point de nécessiter une fonction spécifique
        :param texte:
        :param id:
        :param nomMonstre:
        :param habileteMonstre:
        :param goToVictoire:
        :param goToDefaite:
        :param degatsMonstre:
        :param pvRestantsMonstreAvantGoToFinal:
        :param evt:
        :return:
        """
        effet = self.AjouterEffet(texte, id, evt)
        effet.m_LancerDe = Combat( nomMonstre, habileteMonstre, enduranceMonstre, goToVictoire, goToDefaite, degatsMonstre, pvRestantsMonstreAvantGoToFinal, goToEffetIdFuite)

