from abs.lancerDe import *
from abs.effet import *
from exec.situation import *
from caracLDOELH import *

class TenterChance(LancerDe):

    def __init__(self, idGoToChanceux = None, idGoToMalchanceux = None,
                 callbackChanceux = None, callbackMalchanceux = None):
        LancerDe.__init__(self, 2)
        self.m_IdGoToMalchanceux = idGoToMalchanceux
        self.m_IdGoToChanceux = idGoToChanceux
        self.m_CallbackChanceux = callbackChanceux
        self.m_CallbackMalchanceux = callbackMalchanceux

    def LancerDe(self, effetActuel, input):
        """
        Lancement d'un dé au cours d'un effet
        :param input: seulement utile dans ces cas très particulier de lancer dé, à priori pas pour tenter la chance
        :param effetActuel: effey durant lequel ce lancer de dé arrive
        :return: True si l'exécution est terminée, False si il faut lancer les dés une nouvelle fois en restant dans son effet actuel
        """
        res = self.CalculerResDe()
        situation = Situation()
        valChance = situation.m_Caracs[CaracLDOELH.CHANCE]
        comp = "="
        if ( res > valChance):
            comp = ">"
        elif ( res < valChance):
            comp = "<"
        print("résultat du lancer : {} {} valeur de chance : {}".format(res,  comp, valChance))
        print("".format())
        chanceux = res <= valChance
        # retire un de chance
        situation.RetirerACarac(CaracLDOELH.CHANCE, 1)
        if (chanceux):
            print("Vous êtes chanceux")
        else:
            print("Vous êtes malchanceux")
        if ( chanceux):
            if self.m_CallbackChanceux != None:
                self.m_CallbackChanceux()
            if ( self.m_IdGoToChanceux != None ):
                # modifier go to effet courant
                assert effetActuel != None
                assert isinstance(effetActuel, Effet)
                effetActuel.m_GoToEffetId = self.m_IdGoToChanceux
        else:
            if self.m_CallbackMalchanceux != None:
                self.m_CallbackMalchanceux()
            if ( self.m_IdGoToMalchanceux != None ):
                # modifier go to effet courant
                assert effetActuel != None
                assert isinstance(effetActuel, Effet)
                effetActuel.m_GoToEffetId = self.m_IdGoToMalchanceux

        return True
