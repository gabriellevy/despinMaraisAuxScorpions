def GenererNumeros51_60(genHist):
    genHist.AjouterEffet("""
        Une trappe s'ouvre devant vous, révélant une fosse. D'un bond,
        cependant, vous parvenez à sauter par-dessus et vous traversez le
        hall d'entrée en courant à toutes jambes. Une Statue essaye de
        vous arrêter, mais vous la repoussez et vous ouvrez la porte d'un
        coup de pied. La tête hideuse sculptée sur le panneau de fer tente
        de vous mordre sans succès et vous filez loin de la tour.
        """, "51")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez prendre la direction du Marais", goToEffetId="296")
    genHist.AjouterChoixGoToEffet("Si vous préférez courir vers le village", goToEffetId="5")

    genHist.AjouterEffetDefaite("""
        Vous n'avez malheureusement pas de baie à lui donner et tandis
        que vous racontez ce qui vous est arrivé dans le Marais, le visage
        de Gayolard s'assombrit. « Je suis sûr que vous avez fait de votre
        mieux », dit-il d'un air triste. En le voyant si déçu, vous lui
        proposez d'essayer à nouveau, mais il ne veut pas en entendre
        parler. « Ce serait courir de trop grands risques », objecte-t-il.
        Vous avez fait ce que vous pouviez. Hélas ! ce n'était pas
        suffisant, et votre aventure se termine ici.
        """, "52")

    genHist.AjouterEffetGoToSiDejaVisite("329", "53") # si pas déjà visité passera auto au 53_b

    genHist.AjouterEffet("""
        Tandis que vous suivez le sentier en direction du sud, vous
        entendez coasser des milliers de grenouilles... Elles sont de
        toutes tailles, depuis les plus minuscules jusqu'aux plus énormes.
        Le sentier aboutit à une clairière parsemée de petites mares.
        C'est la Clairière n° 8. Vous voyez tout d'abord
        d'immenses champignons puis vous apercevez un homme assis
        sur l'un d'eux. Cet homme est tout petit mais corpulent, il a des
        yeux noirs et ses paupières sont agitées de battements brefs. Sa
        bouche est exceptionnellement large. Il porte au cou une
        amulette d'argent en forme de grenouille et deux énormes Grenouilles vertes sont
        assises de part et d'autre du champignon. « Je suis le
        MAÎTREDES GRENOUILLES, dit-il aimablement. Qu'est-ce qui
        vous amène ici ? »
        """, "53_b")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez lui répondre avec la même amabilité", goToEffetId="13")
    genHist.AjouterChoixGoToEffet("Si vous préférez l'attaquer", goToEffetId="62")

    genHist.AjouterEffetTenterLaChanceGoTo("""
        Ses traits se convulsent sous l'effet de la fureur et il se met à
        hurler : « Comment osez-vous revenir les mains vides ? »"
        """, "54", "109", "285")

    genHist.AjouterEffet("""
        Vous vous approchez de l'arbre avec prudence. Une forte odeur
        s'en dégage : quelque animal sauvage a sans doute établi là sa
        tanière. Et soudain, en effet, apparaît dans l'ouverture du tronc
        creux la tête hirsute d'un OURS de taille gigantesque.
        """, "55")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez vous enfuir", goToEffetId="390")
    genHist.AjouterChoixGoToEffet("Si vous préférez combattre l'Ours", goToEffetId="200")

    genHist.AjouterEffet("""
        Après avoir cheminé à travers champs et le long des rues
        sinueuses qui mènent à la place du marché, vous arrivez enfin
        devant la maison de Pompatarte. Vous frappez à la porte et la
        Gobe-line vous fait entrer. Quelques instants plus tard, vous vous
        retrouvez dans la bibliothèque où Pompatarte est assis, vêtu
        d'une toge de soie. « Alors, comment vont nos affaires ?
        s'exclame-t-il d'emblée. M'avez-vous rapporté une carte qui
        permette d'atteindre Courbensaule ? »
        """, "56")
    genHist.AjouterChoixGoToEffet("Si vous êtes effectivement allé jusqu'à Courbensaule", goToEffetId="158")
    genHist.AjouterChoixGoToEffet("Dans le cas contraire", goToEffetId="8")

    genHist.AjouterEffetGoToEffet("""
        Aucune des Pierres de Magie que vous possédez ne semble
        pouvoir vous aider dans la situation présente. Il ne vous reste
        donc plus qu'à tirer votre épée et à attaquer le malfaisant sorcier.
        """, "57", goToEffetId="124")

def GenererNumeros91_100(genHist):
    genHist.AjouterEffet("""PAS FAIT
        """, "91")
    genHist.AjouterEffet("""PAS FAIT
        """, "92")
    genHist.AjouterEffet("""PAS FAIT
        """, "93")
    genHist.AjouterEffet("""PAS FAIT
        """, "94")
    genHist.AjouterEffet("""Les villageois hochent la tête d'un air navré tandis que vous vous
        dirigez vers la porte, mais ils ne font aucune autre tentative pour
        vous retenir. Avant que vous ayez atteint la porte, cependant, un
        homme vous barre soudain le passage. Il est petit, d'âge moyen,
        et porte une barbe noire taillée à angle droit. Tout d'abord vous
        pensez qu'il s'agit d'un fermier, mais un fermier ne vous prêterait
        certainement pas autant d'attention. L'homme vous prend par le
        bras et vous mène à une table, dans un coin de la taverne. Les
        autres clients ont repris leurs conversations habituelles, et vous
        avez envie de savoir ce que cet homme silencieux peut bien avoir
        à vous dire. Il se présente alors sous le nom de Grognard et vous
        tient ce langage : « Si vous voulez vraiment affronter les périls du
        Marais, au moins devriez-vous avoir un autre but que le simple
        fait de dresser une carte et d'abattre des bêtes sauvages.
        """, "95")

    genHist.AjouterChoixGoToEffet( "Si vous approuvez ce qu'il dit", goToEffetId="240")
    genHist.AjouterChoixGoToEffet( "Sinon, rendez-vous au", goToEffetId="122")

