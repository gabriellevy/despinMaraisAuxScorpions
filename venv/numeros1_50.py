from caracLDOELH import CaracLDOELH
from exec.situation import *
from abs.condition import *

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


def GenererNumeros21_30(genHist):
    genHist.AjouterEffet("""
        Vous vous reposez quelques minutes et vous récupérez 1 point
        d'ENDURANCE. Vous entendez alors un bruit à l'intérieur de
        l'arbre.
        """, "21")
    genHist.AjouterAjouteurCarac(CaracLDOELH.ENDURANCE, 1)
    genHist.AjouterChoixGoToEffet("Si vous souhaitez savoir ce qui se cache dans cet arbre", goToEffetId="55")
    genHist.AjouterChoixGoToEffet("Si vous préférez ne pas vous en préoccuper", goToEffetId="390")

    genHist.AjouterEffet("""
        Lorsque vous mettez les graines dans votre poche, de nouvelles
        pousses apparaissent déjà à la base des arbres. Il vous faut partir
        au plus vite. Quelle direction allez-vous prendre ?
        """, "22")
    genHist.AjouterChoixGoToEffet("Le nord ?", goToEffetId="320")
    genHist.AjouterChoixGoToEffet("Le sud ?", goToEffetId="90")
    genHist.AjouterChoixGoToEffet("L'ouest ?", goToEffetId="11")

    genHist.AjouterEffet("""
        L'Anneau de Cuivre reste froid, ce qui vous indique que la
        Maîtresse des Oiseaux est une sorcière bienfaisante. Vous lui
        expliquez alors l'objet de votre quête et vous lui demandez son
        aide. « Ce marchand est idiot, dit-elle en hochant la tête, car
        même s'il parvient à se procurer une carte du Marais, les sorciers
        malhonnêtes qui hantent les lieux s'efforceront de piller ses
        roulottes. Mais vous êtes un aventurier courageux et je vais vous
        aider à éviter les plus grands dangers de votre voyage. »
        """, "23", goToEffetId="248")

    def FinTexte24():
        print("""
        Vous vous tenez enfin sur un sol plus ferme
        et vous vous félicitez de posséder l'Anneau de Cuivre car, sans
        lui, vous seriez irrémédiablement perdu. Heureusement, vous
        savez grâce à sa magie quel chemin il convient ' de prendre pour
        trouver la clairière.
        """)
    def Malchanceux24():
        print(
            """
            Vous arrivez malgré tout à vous hisser hors du trou, 
            mais au prix de tels efforts que vous perdez 2 points d'ENDURANCE.
            """
            )
        situation = Situation()
        situation.RetirerACarac(CaracLDOELH.ENDURANCE, 2)
        FinTexte24()
        return True
    def Chanceux24():
        print("vous parvenez à vous extraire sans dommage de la vase.")
        FinTexte24()
        return True
    effet24 = genHist.AjouterEffetTenterLaChance(
        """
        Le Feu Follet danse devant vous et vous le suivez. Le sol devient
        bientôt de plus en plus humide, et vous tombez soudain dans un
        trou rempli de vase. Le Feu Follet disparaît alors : il n'était là que
        pour tromper les voyageurs imprudents dans votre genre et
        contribuer à leur perte. Tentez votre Chance.  
        """, "24", Chanceux24, Malchanceux24)
    effet24.m_GoToEffetId = "249"

    genHist.AjouterEffet("""
        L'Aigle lance un cri et vole en cercle autour de la clairière, puis il
        s'éloigne vers son nid. Vous pouvez vous estimer heureux de
        repartir sans dommage !
        """, "25", goToEffetId="202")

    genHist.AjouterEffetCombat("""
        Vous sentez que le MAÎTRE DES ARAIGNÉES est un
        personnage profondément malfaisant et vous l'attaquez avec
        votre épée. Il se défend en brandissant une baguette magique
        luisante, dont l'extrémité est très pointue et enduite d'une
        substance verdâtre et pestilentielle. Chaque fois que vous
        recevrez un coup de cette baguette magique, vous perdrez 1 point
        d'ENDURANCE supplémentaire (3 au lieu de 2).
        
        MAÎTRE DES ARAIGNÉES HABILETÉ : 9 ENDURANCE : 6
        """, "26", "MAÎTRE DES ARAIGNÉES", 9, 6, "354", degatsMonstre=3)

    genHist.AjouterEffet("""
        Grognard vous conseille d'aller chercher Pompatarte au marché
        du village. Mais dès que vous pénétrez dans le dédale de rues où
        s'alignent un nombre impressionnant de boutiques, vous êtes
        complètement perdu. Vous demandez votre chemin à plusieurs
        reprises et, finalement, un groupe d'enfants d'humeur joyeuse
        vous conduit devant une grande maison qui s'élève en bordure
        du marché. Vous frappez à la porte et c'est un Gobelin qui vous
        ouvre ! Ou plutôt une Gobeline qui fait office de servante et n'a
        rien à voir avec les guerriers Gobelins que vous avez eu l'occasion
        de combattre. Elle vous mène dans une bibliothèque où
        Pompatarte est assis. C'est l'un des hommes les plus étranges que
        vous ayez jamais vus... Il est très grand et obèse avec une longue
        barbe soigneusement nouée en tresses et une peau d'un rouge
        brillant ! Vous lui racontez aussitôt votre histoire en lui
        demandant s'il a besoin de quelqu'un tel que vous. « J'en ai
        besoin, en effet, marmonne-t-il, mais qu'est-ce qui vous fait
        croire que vous pourrez survivre dans le Marais aux Scorpions
        alors que tant d'autres n'en sont jamais revenus ? »
        """, "27")
    genHist.AjouterChoixGoToEffet("""
        Si vous souhaitez lui parler de la Vieille Femme 
        et de l'Anneau de Cuivre que vous portez au doigt
        """, goToEffetId="2")
    genHist.AjouterChoixGoToEffet("""
        Si vous préférez lui adresser un sourire en lui assurant que 
        vous êtes un guerrier hors pair
        """, goToEffetId="173")

    genHist.AjouterEffetCombat("""
        Il y a plusieurs ARBRES-ÉPÉES, mais vous les combattrez
        comme s'il s'agissait d'un seul et même adversaire. Vous avez un
        avantage sur eux : ils ne peuvent pas vous voir et ne vous
        repèrent que par les sons que vous émettez. Ces arbres sont
        nombreux cependant, et chacun d'eux est doté de plusieurs
        branches qui brandissent des lames acérées.
        
        ARBRES-ÉPÉES HABILETÉ: 9 ENDURANCE: 12
        """, "28", "ARBRES-ÉPÉES", 9, 12, "362")

    genHist.AjouterEffetTenterLaChanceGoTo("""
        Vous vous rendez compte qu'il serait tout à fait stupide de révéler
        à cet homme que vous vous êtes mis au service d'un sorcier
        malfaisant. Aussi lui répondez-vous par un mensonge. « Je sers
        les forces du Bien, assurez-vous. Mais pour l'instant, je voudrais
        simplement trouver le chemin qui me permettra de sortir du
        Marais. Je cherche l'un de ces sorciers que l'on appelle les
        Maîtres. » Tentez votre Chance.
        """, "29", "185", "378")

    genHist.AjouterEffetDefaite("""
        Vous commencez par jeter vos Bottes et votre Sac à Dos au bas
        de la falaise, puis vous plongez vous-même. Hélas ! vous vous
        rendez très vite compte, mais trop tard, que l'eau est peu
        profonde et le lit de la rivière, recouvert d'une épaisse couche de
        vase. Vous voilà enlisé. Vous parvenez cependant à vous dégager,
        mais lorsque vous atteignez enfin la surface de l'eau, vous vous
        trouvez nez à nez avec un Crocodile aux mâchoires grandes
        ouvertes. Vous empoignez votre épée, mais votre geste est vain :
        les mâchoires se referment sur vous et votre aventure se termine
        dans l'estomac du reptile.
        """, "30")

def GenererNumeros31_40(genHist):
    genHist.AjouterEffet("""
        En poursuivant votre marche, vous sentez que vous allez trop
        loin vers l'est depuis votre entrée dans le marécage. Vous vous
        demandez alors si vous avez pris le bon chemin et, soudain, vous
        entrez dans une clairière envahie d'herbes. C'est la Clairière n°
        21. Vous trouvez au milieu de la clairière un bassin rempli
        d'une eau qui semble pure comme le cristal. Une petite plage de
        sable fin borde l'un des côtés du bassin. Aucun autre chemin ne
        permet de sortir de la clairière en dehors de celui par lequel vous
        êtes arrivé. Qu'allez-vous faire ?
        """, "31")
    genHist.AjouterChoixGoToEffet("Si vous y êtes déjà venu", goToEffetId="364")
    genHist.AjouterChoixGoToEffet("Quitter les lieux en retournant vers l'ouest ?", goToEffetId="47")
    genHist.AjouterChoixGoToEffet("Attendre quelques minutes pour voir si aucun danger ne vous menace ?", goToEffetId="394")

    genHist.AjouterEffet("""
        Vous coupez les fleurs à grands coups d'épée, mais elles sont en
        trop grand nombre pour que vous puissiez toutes les abattre et
        vous vous épuisez vainement. Vos efforts vous coûtent 2 points
        d'ENDURANCE et 1 point d'HABILETÉ.
        """, "32")
    genHist.AjouterChoixGoToEffet("Si vous préférez abandonner la partie et vous enfuir", goToEffetId="269")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez faire usage de magie", goToEffetId="80")
    genHist.AjouterRetireurCarac(CaracLDOELH.ENDURANCE, 2)
    genHist.AjouterRetireurCarac(CaracLDOELH.HABILETE, 1)

    genHist.AjouterEffet("""
        Vous vous hâtez de traverser la clairière en espérant éviter une
        nouvelle attaque de l'Herbe à Pinces. Hélas ! elle se dresse encore
        plus vite devant vous et ses redoutables tenailles vertes s'ouvrent
        avidement en essayant de vous attraper.
        """, "33")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez combattre l'Herbe à Pinces à coups d'épée", goToEffetId="134")
    genHist.AjouterChoixGoToEffet("Si vous préférez recourir à la magie", goToEffetId="167")

    genHist.AjouterEffet("""
        Quelle Pierre de Magie allez-vous utiliser contre le Monstre du
        Bassin ?
        """, "34")
    genHist.AjouterChoixGoToEffet("Flétrissure ?", goToEffetId="237")
    genHist.AjouterChoixGoToEffet("Feu ?", goToEffetId="291")
    genHist.AjouterChoixGoToEffet("Terreur ?", goToEffetId="356")
    genHist.AjouterChoixGoToEffet("Aucune d'entre elles ?", goToEffetId="209")

    genHist.AjouterEffet("""
        Cette fois encore, les Orques visent mal et les deux flèches vous
        manquent, mais, soudain, elles décrivent une courbe et viennent
        se planter dans votre Sac à Dos ! Une seule d'entre elles parvient
        à vous égratigner l'épaule et vous perdez 1 point d'ENDURANCE.
        Vous vous rendez compte alors que l'Aimant d'Or est maudit et
        qu'il attire les flèches... Vous avez de la chance de l'avoir rangé
        dans votre Sac à Dos plutôt que de le porter directement sur vous
        ! Qu'allez-vous faire à présent ?
        """, "35")
    genHist.AjouterChoixGoToEffet("Attaquer avec votre épée ?", goToEffetId="281")
    genHist.AjouterChoixGoToEffet("Recourir à la magie ?", goToEffetId="399")
    genHist.AjouterChoixGoToEffet("Prendre la Fuite ?", goToEffetId="309")
    genHist.AjouterRetireurCarac(CaracLDOELH.ENDURANCE, 1)

    genHist.AjouterEffet("""
        Vous expliquez le but de votre quête au Maître des Jardins.
        """, "36")
    genHist.AjouterChoixGoToEffet("Si vous avez déjà découvert le buisson d'Anthérique", goToEffetId="283")
    genHist.AjouterChoixGoToEffet("sinon", goToEffetId="396")

    genHist.AjouterEffet("""
         
        """, "37")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez dire la vérité au sujet de votre quête", goToEffetId="292")
    genHist.AjouterChoixGoToEffet("Si vous préférez inventer une histoire et bavarder quelques moments", goToEffetId="220")

    genHist.AjouterEffet("""
        La Vase est morte et ses restes se putréfient à vue d'oeil. Il s'en
        dégage une odeur insupportable.
        """, "38", goToEffetId="153")

    genHist.AjouterEffet("""
        Vous jetez un sort d'Amitié à la Licorne qui vous regarde d'un air
        soupçonneux. De toute évidence, elle ne se fie pas aux humains.
        Votre magie fait cependant de l'effet car elle finit par se
        désintéresser de vous pour brouter l'herbe de la clairière.
        """, "39", goToEffetId="348")

    genHist.AjouterEffet("""
        Dominant votre peur, vous vous approchez de la sinistre tour.
        Des Chauves-Souris volent en tournoyant autour de son sommet.
        En vous approchant, vous remarquez une tête hideuse sculptée
        sur la porte de fer. La porte s'ouvre alors devant vous et
        Stratagus qui vous attend apparaît. Il est grand, d'une maigreur
        squelettique et porte une toge noire sur laquelle sont brodés des
        motifs écarlates qui semblent étinceler. Il vous accueille
        aimablement, mais l'Anneau continue de diffuser sa chaleur
        autour de votre doigt, vous avertissant ainsi que vous êtes en
        présence d'un être maléfique. « Je sais tout de vous, dit
        Stratagus, vous voulez explorer le Marais, et Grognard, ce
        fouineur imbécile, vous a envoyé ici. Mais qui vous fait croire que
        vous êtes digne de me servir ? J'ai besoin d'un héros qui n'ait
        peur de rien. » Qu'allez-vous faire ?
        """, "40")
    genHist.AjouterChoixGoToEffet("Lui lancer un défi ?", goToEffetId="4")
    genHist.AjouterChoixGoToEffet("""
        Lui affirmer que vous êtes un guerrier intrépide et que, grâce à
        votre Anneau Magique, vous ne perdrez jamais votre chemin ?
        """, goToEffetId="50")
    genHist.AjouterChoixGoToEffet("""
        Vous contenter de sourire en lui déclarant que vous n'avez peur
        de rien ?
        """, goToEffetId="97")


def GenererNumeros41_50(genHist):
    genHist.AjouterEffetGoToSiDejaVisite("382", "41") # si aps déjà visité passera auto au 41_b

    def Malchanceux41_b():
        # Si vous êtes Malchanceux, rendez-vous au .
        return True
    def Chanceux41_b():
        # et vous vous
        #         rendez au .
        print("Vous perdez 2 points d'ENDURANCE")
        situation = Situation()
        situation.RetirerACarac(CaracLDOELH.ENDURANCE, 2)

        return True
    effet41_b = genHist.AjouterEffetTenterLaChance("""
        Vous entrez dans une clairière entourée d'arbres dont les troncs
        sont recouverts de lierre. 
        Apparemment, il n'y a rien d'intéressant alentour et vous vous
        apprêtez donc à repartir lorsque vous vous trouvez soudain pris
        dans des sables mouvants ! Tentez-votre Chance.
        """,
        "41_b", Chanceux41_b, Malchanceux41_b, "270", "87")

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