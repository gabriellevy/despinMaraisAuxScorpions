def GenererNumeros1_10(genHist):
    genHist.AjouterEffet("""Le chemin est long pour arriver jusqu'au Marais qui s'étend à
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
    genHist.AjouterChoixGoToEffet( \
        "Tirer votre épée pour leur montrer qu'il ne fait pas bon se mettre en travers de votre chemin ?", goToEffetId="48")
    genHist.AjouterChoixGoToEffet( \
        "Leur expliquer poliment que votre décision est irrévocable ?", goToEffetId="95")

    genHist.AjouterEffet("Il se passe des choses dans cet effet d'histoire ! ", "2")
    genHist.AjouterEffet("Mais vraiment plein de trucs ", "3")

def GenererNumeros41_50(genHist):
    genHist.AjouterEffet("""Vous empoignez le pommeau de votre épée, prêt à dégainer, et
        vous leur lancez un défi d'une voix retentissante. Votre attitude,
        cependant, ne les impressionne pas le moins du monde : elle les
        fait même éclater de rire. « Nous ne sommes pas du genre
        bagarreur, vous disent-ils. Il n'y a ici que de simples villageois,
        mais un gaillard tel que vous, toujours prêt à brandir son épée,
        devrait bien en effet aller faire un tour dans le Marais. Pour les
        gens de votre espèce qui passent leur temps à chercher des
        ennuis, c'est l'endroit idéal. Et nous ne vous retiendrons pas plus
        longtemps. » Vous vous sentez alors quelque peu gêné et vous
        perdez 1 point de CHANCE pour vous être montré agressif envers
        ces paisibles villageois.
        """, "48")
    genHist.AjouterRetireurCarac("Chance", 1)