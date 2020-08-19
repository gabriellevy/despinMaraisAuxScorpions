from abs.lancerDe import *
from abs.effet import *
from exec.situation import *
from caracLDOELH import *

class Combat(LancerDe):

    def __init__(self, nomMonstre, habileteMonstre, enduranceMonstre, goToVictoire, goToDefaite = "", degatsMonstre = 2, pvRestantsMonstreAvantGoToFinal=0):
        LancerDe.__init__(self, 2)
        self.m_NomMonstre = nomMonstre
        self.m_HabileteMonstre = habileteMonstre
        self.m_EnduranceMonstre = enduranceMonstre
        self.m_GoToVictoire = goToVictoire
        self.m_GoToDefaite = goToDefaite
        self.m_DegatsMonstre = degatsMonstre
        self.m_PvRestantsMonstreAvantGoToFinal = pvRestantsMonstreAvantGoToFinal

    def LancerDe(self, effetActuel):
        situation = Situation()

        resDeJoueur = self.CalculerResDe()
        resCombatJoueur = resDeJoueur + situation.m_Caracs[CaracLDOELH.HABILETE]
        print("Votre résultat d'attaque : Habileté {} + {} = {}".format(situation.m_Caracs[CaracLDOELH.HABILETE], resDeJoueur, resCombatJoueur))

        resDeMonstre = self.CalculerResDe()
        resCombatMonstre = resDeMonstre + self.m_HabileteMonstre
        print("Résltat du monstre : Habileté {} + {} = {}".format(self.m_HabileteMonstre, resDeMonstre, resCombatMonstre))

        if (resCombatJoueur > resCombatMonstre):
            print("Vous l'avez blessé il perd 2 points d'endurance")
            self.m_EnduranceMonstre = self.m_EnduranceMonstre - 2
            # si le monstre est mort (ou vaincu car trop blessé) le combat se termine :
            if ( self.m_EnduranceMonstre <= self.m_PvRestantsMonstreAvantGoToFinal):
                print("Le monstre est vaincu")
                if ( self.m_GoToVictoire != ""):
                    assert effetActuel != None
                    assert isinstance(effetActuel, Effet)
                    effetActuel.m_GoToEffetId = self.m_GoToVictoire
                return True
        elif (resCombatMonstre > resCombatJoueur):
            print("Le monstre vous a blessé, vous perdez {} points d'endurance".format(self.m_DegatsMonstre))
            situation.RetirerACarac(CaracLDOELH.ENDURANCE, self.m_DegatsMonstre)
            # si le joueur est mort (ou vaincu car trop blessé) le combat se termine :
            if ( situation.m_Caracs[CaracLDOELH.ENDURANCE] <= 0):
                print("Vous avez été vaincu")
                if ( self.m_GoToDefaite != ""):
                    assert effetActuel != None
                    assert isinstance(effetActuel, Effet)
                    effetActuel.m_GoToEffetId = self.m_GoToDefaite
                return True
        else:
            print("égalité")

        # affichage de l'état actuel
        print("{} HABILETÉ: {} ENDURANCE: {}".format(self.m_NomMonstre, self.m_HabileteMonstre, self.m_EnduranceMonstre))
        print("VOUS : HABILETÉ: {} ENDURANCE: {}".format(situation.m_Caracs[CaracLDOELH.HABILETE], situation.m_Caracs[CaracLDOELH.ENDURANCE]))

        return False

