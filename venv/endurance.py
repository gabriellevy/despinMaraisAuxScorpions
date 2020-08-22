from abs.carac import Carac

class Endurance(Carac):

    def ControlerValeur(self):
        """
        important dans les caracs surclassant cette carac de base : il peut y avoir un control ou une action à effectuer lors d'une modif de carac
        """
        if ( self.m_Valeur <= 0):
            print("Vous êtes mort, votre aventure s'arrête ici...")
            exit() # TODO MATHIEU : intégrer fin de partie dans execHistoire (que l'effet actuel soit quand même affiché mais ensuite plus rien)

