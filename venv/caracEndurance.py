from abs.carac import Carac
from exec.situation import *

class Endurance(Carac):

    def ControlerValeur(self):
        """
        important dans les caracs surclassant cette carac de base : il peut y avoir un control ou une action à effectuer lors d'une modif de carac
        """
        Carac.ControlerValeur(self)

        if ( self.m_Valeur <= 0):
            situation = Situation()
            situation.m_PhaseHistoire = PhaseHistoire.DEFAITE

