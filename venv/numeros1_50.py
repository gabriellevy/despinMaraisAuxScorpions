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
    genHist.AjouterChoixGoToEffet("Si vous préférez attaquer Stratagus lui-même", goToEffetId="123")

    genHist.AjouterEffetTenterLaChanceGoTo("Tentez votre Chance.", "5", "273", "297")

    genHist.AjouterEffet("""
        Vous revenez dans la maison de Gayolard. Un feu brûle dans la
        cheminée de la cuisine et une délicieuse odeur se répand
        alentour : quelque mets délectable est en train de mijoter dans la
        marmite. Le sorcier vous accueille avec cordialité et vous pose
        aussitôt cette question : « Avez-vous la baie ? »
        """, "6")
    genHist.AjouterChoixGoToEffet("Si vous avez réussi à lui rapporter le fruit violet de l'Anthérique", goToEffetId="175")
    genHist.AjouterChoixGoToEffet("Sinon,", goToEffetId="52")

    genHist.AjouterEffet("""
        Le visage du mauvais sorcier s'assombrit et les dessins de sa robe
        se mettent à danser devant vos yeux d'une manière menaçante. «
        C'est toujours mieux que rien, marmonne-t-il. Donnez-moi ce
        que vous avez et vous recevrez 250 Pièces d'Or en échange. »
        """, "7")
    genHist.AjouterChoixGoToEffet("Si vous acceptez son offre,", goToEffetId="266")
    genHist.AjouterChoixGoToEffet("Si vous préférez lui rappeler qu'il vous avait promis davantage,", goToEffetId="207")

    genHist.AjouterEffet("""
        « C'est dommage, soupire-t-il, il faudra que je trouve quelqu'un
        d'autre. S'il vous reste quelques-unes des Pierres de Magie que je
        vous ai données, je vous les échange contre une Potion de
        Guérison. » Qu'allez-vous faire ?
        """, "8")
    genHist.AjouterChoixGoToEffet("Échanger les Pierres qui vous restent contre la Potion ?", goToEffetId="141")
    genHist.AjouterChoixGoToEffet("Lui expliquer que vous les avez toutes utilisées ?", goToEffetId="316")
    genHist.AjouterChoixGoToEffet("Attaquer Pompatarte ?", goToEffetId="341")

    genHist.AjouterEffet("""
        Vous vous trouvez à la lisière sud du Marais aux Scorpions. Grâce
        à l'Anneau de Cuivre, vous saurez toujours où est le nord, mais il
        vous faut quand même tracer une carte sur laquelle devront
        figurer tous les sentiers que vous emprunterez et les clairières
        que vous explorerez (voir page 21 les indications concernant la
        manière d'établir cette carte). Vous découvrez très vite un sentier
        orienté au nord qui s'enfonce à l'intérieur du Marais. Quelques
        mots peints grossièrement sur un roc vous donnent cet
        avertissement : ATTENTION ! MARAIS AUX SCORPIONS ! FAITES DEMITOUR
        ! Deux tibias croisés surmontés d'un crâne complètent cette
        recommandation dont, bien entendu, vous ne tenez aucun
        compte. D'une démarche assurée, vous franchissez la lisière du
        marécage et vous comprenez aussitôt qu'il serait tout à fait
        imprudent de vous aventurer dans la vase qui borde le sentier.Il
        vous faut suivre celui-ci jusqu'au bout sans vous en écarter le
        moins du monde.
        """, "9", goToEffetId="195")

    genHist.AjouterEffet("""
        Les arbres noueux s'écartent bientôt devant vous, et vous entrez
        dans une autre clairière. C'est la Clairière n° 5. Vous constatez aussitôt qu'on s'est
        battu ici. Le sol a été piétiné, l'herbe humide est tachée de sang et
        deux flèches sont plantées dans un arbre un peu plus loin.
        """, "10")
    genHist.AjouterChoixGoToEffet("Si vous y êtes déjà venu,", goToEffetId="142")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez examiner cette clairière pour voir ce qu'elle recèle", goToEffetId="59")
    genHist.AjouterChoixGoToEffet("Si vous préférez la quitter le plus vite possible", goToEffetId="227")

def GenererNumeros11_20(genHist):
    genHist.AjouterEffet("""
        En progressant vers l'ouest, le Marais devient plus sinistre
        encore et vous êtes en train de vous demander si vous pourrez en
        supporter davantage lorsqu’enfin le sentier s'élargit pour aboutir
        à une étroite et longue échappée. C'est la Clairière n° 6. Vous jetez un coup d'oeil autour de vous : il n'y a aucun
        autre sentier. Il semble que vous soyez arrivé dans un cul-de-sac.
        Vous vous approchez alors d'un grand rocher gris sur lequel vous
        comptez vous allonger pour prendre quelque repos. Mais,
        soudain, le rocher bouge ! Cette couleur grise n'était pas celle de
        la pierre mais d'un pelage rêche. Deux yeux rouges vous fixent
        d'un regard furieux et une BÊTE IMMONDE dotée de six pattes
        griffues, s'avance aussitôt vers vous. Qu'allez-vous faire ?
        """, "11")
    genHist.AjouterChoixGoToEffet("Si vous y êtes déjà venu,", goToEffetId="210")
    genHist.AjouterChoixGoToEffet("La combattre ?", goToEffetId="176")
    genHist.AjouterChoixGoToEffet("Prendre la Fuite ?", goToEffetId="102")
    genHist.AjouterChoixGoToEffet("Essayer de lui jeter un sort ?", goToEffetId="374")

    genHist.AjouterEffetCombat("""
        Le GÉANT se bat en poussant des cris de fureur. Il est doué d'une
        force extraordinaire mais, par chance pour vous, ses gestes sont
        plutôt maladroits et sa massue ne vous frappe que rarement.
        Lorsqu'elle atteint son but, cependant, vous perdez 4 points
        d'ENDURANCE au lieu de 2 en raison de la puissance du coup.
        Aussi, faites attention !
        
        GÉANT HABILETÉ: 9 ENDURANCE: 12
        """, "12", "GÉANT", 9, 12, "61", degatsMonstre = 4, pvRestantsMonstreAvantGoToFinal=6, goToEffetIdFuite="161")

    genHist.AjouterEffet("""
        « Je suis un guerrier en mission », répliquez-vous. Votre Anneau
        ne vous avertit d'aucun danger et vous parlez donc au Maître des
        Grenouilles sans éprouver la moindre inquiétude. Quel sorcier
        avez-vous choisi de servir ?
        """, "13")
    genHist.AjouterChoixGoToEffet("Gayolard ?", goToEffetId="212")
    genHist.AjouterChoixGoToEffet("Stratagus ?", goToEffetId="287")
    genHist.AjouterChoixGoToEffet("Pompatarte ?", goToEffetId="376")

    genHist.AjouterEffet("""
        Le sentier vous mène à une petite clairière où, quelques années
        plus tôt, un arbre immense s'est abattu en entraînant dans sa
        chute plusieurs autres arbres. C'est la Clairière n° 32. Sinon, lisez ce qui suit. En
        vous approchant, vous entendez des bruits de lutte. Derrière un
        large tronc, vous apercevez alors un SCORPION GÉANT en train
        de se battre avec un Nain vêtu d'une cuirasse. Le Nain est en
        difficulté : au moment où vous apparaissez, le Scorpion l'a pris
        par le cou dans l'une de ses pinces et le précipite sur le sol ou il
        reste étendu sans vie. Il vous semble peu probable que vos
        Pierres de Magie puissent avoir quelque effet sur un tel
        adversaire.
        """, "14")
    genHist.AjouterChoixGoToEffet("Si vous y êtes déjà venu,", goToEffetId="338")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez quitter la clairière tandis que le monstre dévore sa victime", goToEffetId="88")
    genHist.AjouterChoixGoToEffet("Si vous choisissez en revanche d'attaquer le Scorpion", goToEffetId="312")

    genHist.AjouterEffet("""
        Qu'allez-vous lui proposer ?
        """, "15")
    genHist.AjouterChoixGoToEffet("Un Aimant d'Or ?", goToEffetId="63")
    genHist.AjouterChoixGoToEffet("Une Amulette appartenant à l'un des autres Maîtres ?", goToEffetId="198")
    genHist.AjouterChoixGoToEffet("Un énorme joyau violet ?", goToEffetId="276")
    genHist.AjouterChoixGoToEffet("Rien de tout cela ?", goToEffetId="212")

    genHist.AjouterEffet("""
        Quelque chose dans votre voix vous trahit. Il fait des gestes de la
        main en vous fixant d'un regard inquisiteur. 
        """, "16")
    genHist.AjouterChoixGoToEffet("Est-il en train de lire dans vos pensées ?", goToEffetId="198")

    genHist.AjouterEffet("""
        Si cet homme est malfaisant, vous ne voulez rien avoir à faire
        avec lui et vous traversez la clairière sans lui prêter attention.
        Cependant, au moment où vous allez rejoindre le sentier, une
        cordelette s'enroule autour de votre cou. Vous vous débattez,
        mais le voleur vous étrangle et vous vous écroulez sur le sol, sans
        connaissance. Vous perdez aussitôt 3 points d'ENDURANCE.
        Lorsque vous reprenez conscience, vous vous sentez mal et vous
        avez le tournis. De plus, toutes vos Pierres et vos autres objets
        magiques ont disparu, et il n'y a plus trace du voleur.
        """, "17", goToEffetId="179")
    genHist.AjouterRetireurCarac(CaracLDOELH.ENDURANCE, 3)
    # TODO MATHIEU : perte des pierres et des objets magiques (lesquels ?? je n'en connais aucun...)

    genHist.AjouterEffet("""
        Lorsqu'ils vous voient les charger en brandissant votre épée, les
        Brigands prennent peur, et tous les cinq s'enfuient parmi les
        arbres qui bordent la clairière. Vous ne vous arrêtez pas pour
        autant et vous traversez la clairière en courant et en hurlant. Les
        Brigands désemparés ne songent même pas à vous poursuivre.
        """, "18", goToEffetId="19")

    genHist.AjouterEffet("""
        Deux sentiers permettent de quitter la clairière. L'un, orienté au
        nord, est beaucoup plus large et mieux tracé, comme si de
        nombreux voyageurs l'avaient emprunté. Dans quelle direction
        allez-vous poursuivre votre chemin ?
        """, "19")
    genHist.AjouterChoixGoToEffet("Vers le nord ?", goToEffetId="280")
    genHist.AjouterChoixGoToEffet("Vers l'est ?", goToEffetId="137")

    genHist.AjouterEffet("""
        Le fruit a un goût délicieux et vous sentez une impression de
        bien-être se répandre dans tout votre corps. Vous récupérez 2
        points d'ENDURANCE et 1 de CHANCE. Vous ne découvrez rien
        d'intéressant par ailleurs
        """, "20")
    genHist.AjouterAjouteurCarac(CaracLDOELH.ENDURANCE, 2)
    genHist.AjouterAjouteurCarac(CaracLDOELH.CHANCE, 1)
    # TODO MATHIEU : à faire : gérer la limite max des valeurs de caracs


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