

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

