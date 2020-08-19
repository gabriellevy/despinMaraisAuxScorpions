from abs.lancerDe import *
from abs.effet import *
from exec.situation import *
from caracLDOELH import *

class TenterChance(LancerDe):

    def __init__(self, idGoToChanceux, idGoToMalchanceux):
        LancerDe.__init__(self, 2)
        self.m_IdGoToMalchanceux = idGoToMalchanceux
        self.m_IdGoToChanceux = idGoToChanceux

    def LancerDe(self, effetActuel):
        """
        Lancement d'un dé au cours d'un effet
        :param effetActuel:
        :return: True si l'exécution est terminée, False si il faut lancer les dés une nouvelle fois en restant dans son effet actuel
        """
        res = self.CalculerResDe()
        situation = Situation()
        print("résultat du lancer : {}".format(res))
        valChance = situation.m_Caracs[CaracLDOELH.CHANCE]
        print("valeur de chance : {}".format(valChance))
        chanceux = res <= valChance
        # retire un de chance
        situation.RetirerACarac(CaracLDOELH.CHANCE, 1)
        if (chanceux):
            print("Vous êtes chanceux")
        else:
            print("Vous êtes malchanceux")
        if ( chanceux and self.m_IdGoToChanceux != None):
            # modifier go to effet courant
            assert effetActuel != None
            assert isinstance(effetActuel, Effet)
            effetActuel.m_GoToEffetId = self.m_IdGoToChanceux
        elif self.m_IdGoToMalchanceux != None:
            # modifier go to effet courant
            assert effetActuel != None
            assert isinstance(effetActuel, Effet)
            effetActuel.m_GoToEffetId = self.m_IdGoToMalchanceux

        return False
