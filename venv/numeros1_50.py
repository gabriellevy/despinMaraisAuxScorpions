from caracLDOELH import CaracLDOELH

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

    genHist.AjouterEffet("""
        Votre histoire le fascine, et, bientôt, il se lève d'un mouvement
        lent puis s'approche d'une table sur laquelle un globe est posé. Il
        le fait alors tourner sur son axe, révélant à l'intérieur de la sphère
        une cachette où sont empilées des Pièces d'Or. Il y en a tant que
        les yeux vous sortent de la tête. « Accepteriez-vous de me le
        vendre ? demande Pompatarte avec un sourire. Je vous en offre
        cent Pièces d'Or fin. »
        """, "2")
    genHist.AjouterChoixGoToEffet("Si vous acceptez son offre", goToEffetId="49")
    genHist.AjouterChoixGoToEffet("Si vous préférez refuser", goToEffetId="173")

    genHist.AjouterEffet("""
        Moins de deux kilomètres plus loin, vous trébuchez dans un trou,
        et vos deux pieds s'enfoncent aussitôt dans la vase. Vous essayez
        en vain de vous dégager en agrippant une plante, mais sa tige
        casse, et vous vous enlisez plus profondément encore. De petits
        cris retentissent alors derrière vous. Vous vous efforcez
        d'empoigner votre épée, mais des dents pointues se plantent
        dans votre main et, quelques instants plus tard, des dizaines de
        rats sont sur vous. Il vous est impossible de vous enfuir ou de les
        combattre et bientôt, ainsi que l'avaient prédit les gens du
        village, il ne reste plus de vous qu'un squelette sur lequel vient se
        refléter la lumière pâle qui filtre entre les arbres. Votre aventure
        est terminée. La prochaine fois vous saurez que, sans le secours
        de la magie, on ne sort pas vivant du Marais aux Scorpions.
        """, "3")

    genHist.AjouterEffet("""
        Le sorcier éclate d'un rire mauvais. « Je ne vais certainement pas
        gaspiller mon énergie à combattre un aussi piètre adversaire,
        lance-t-il avec mépris, mais exercez donc votre bravoure contre
        ceci... » Il fait alors un signe de la main en direction de la
        STATUE D'UN GOBELIN qui se dresse à l'abri d'une niche
        aménagée dans le mur. La statue s'avance aussitôt vers vous en
        brandissant son épée de pierre.
        """, "4")
    genHist.AjouterChoixGoToEffet("Si vous voulez la combattre", goToEffetId="284")
    genHist.AjouterChoixGoToEffet("Si vous préférez attaquer Stratagus luimême", goToEffetId="123")


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
    genHist.AjouterRetireurCarac(CaracLDOELH.CHANCE, 1)