from caracLDOELH import CaracLDOELH

def GenererNumeros191_200(genHist):
    genHist.AjouterEffet("""
        Vous êtes dans la Clairière n° 1. En vérité, il s'agit simplement
        d'un large rond-point d'où partent trois sentiers. Le sol est
        instable et humide et de gros insectes volettent au-dessus des
        mares qui parsèment l'endroit.
        """, "195")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez traverser cette clairière avec précaution pour rejoindre un autre chemin,", goToEffetId="58")
    genHist.AjouterChoixGoToEffet("Si vous préférez essayer de franchir d'un bond la partie marécageuse du sol,", goToEffetId="91")

