from gen.gen_histoire import *
from numeros1_50 import *

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


