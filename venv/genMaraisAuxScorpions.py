from gen.gen_histoire import *

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
        self.GenererNumeros1_10()

    def GenererNumeros1_10(self):
        self.AjouterEffet("""Le chemin est long pour arriver jusqu'au Marais qui s'étend à
l'extrême ouest du royaume, et votre voyage abonde en péripéties
qu'un novice aurait qualifiées d'aventures. Mais pour vous,
combattre des Orques et des Gobelins, affronter de malfaisants
sorciers ou tailler en pièces des loups géants n'est que routine
quotidienne. A mesure que vous progressez vers l'ouest, les
montagnes se changent en collines, les collines en plaines et les
plaines en basses terres au sol humide : le Marais aux Scorpions
n'est plus très loin. A votre entrée dans la petite bourgade de
Bourbenville, personne ne vous prête attention car les voyageurs
ne sont pas rares dans la région. Votre heaume d'acier et votre
épée à la longue lame effilée indiquent que vous êtes un
aventurier avec lequel il faut compter, mais il n'y a rien là
d'extraordinaire pour les habitants de l'endroit. Vous faites plus
grande impression cependant lorsque, installé au beau milieu
d'une taverne, vous annoncez à qui veut l'entendre votre projet
d'explorer le Marais aux Scorpions. Aussitôt, tous les autres
clients se rassemblent autour de vous en repoussant les tables
pour faire de la place. « Explorer le Marais ? s'écrie-t-on d'une
même voix. Vous n'y pensez pas ! D'autres s'y sont essayé avant
vous, et leurs os blanchissent dans ses profondeurs ! C'est une
région inextricable, infestée de vermine, de monstres et de
brigands affamés ; par surcroît, un clan de sorciers qui se sont
eux-mêmes baptisés les Maîtres a récemment revendiqué la
propriété de tout le territoire. L'un de ces mages, un colosse
brutal, accompagné de deux loups gris, est venu dans cette même
taverne la semaine précédente. Il n'a pas dit grand-chose, mais,
de toute évidence, il n'était pas du genre à accueillir à bras
ouverts ceux qui se risqueraient à pénétrer sur ses terres. » Tous
les villageois sont convaincus que vous allez vers une mort
certaine si vous persistez dans votre projet. « Il n'est pas
question qu'on vous laisse partir là-bas disent-ils. », et l'un d'eux
a même l'audace de poser sa main calleuse sur votre épaule pour
vous empêcher de quitter la taverne. Qu'allez-vous faire ?
""", "1")
        self.AjouterChoix("Tirer votre épée pour leur montrer qu'il ne fait pas bon se mettre en travers de votre chemin ?")
        self.AjouterChoix("Leur expliquer poliment que votre décision est irrévocable ?")
        self.AjouterEffet("Il se passe des choses dans cet effet d'histoire ! ", "2")
        self.AjouterEffet("Mais vraiment plein de trucs ", "3")
