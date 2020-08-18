from caracLDOELH import CaracLDOELH

def GenererNumeros271_280(genHist):
    genHist.AjouterEffet("""
        ???
        """, "271")

    genHist.AjouterEffet("""
        ???
        """, "272")

    genHist.AjouterEffet("""
        Tandis que vous vous hâtez le long du chemin qui mène au
        village, votre Anneau de Cuivre se met à vous picoter le doigt.
        Vous jetez alors un coup d'oeil par-dessus votre épaule et vous
        apercevez une forme noire qui s'envole de la tour. Vous vous
        cachez aussitôt dans des buissons et vous observez la créature
        qui s'est ainsi lancée à votre poursuite, mais vous ne saurez
        jamais de qui ou de quoi il s'agissait exactement. Au bout d'un
        moment, en effet, la mystérieuse silhouette noire retourne au
        sommet de la tour et vous vous mettez à courir à toutes jambes
        jusqu'à ce que vous ayez atteint le village où vous arrivez hors
        d'haleine et passablement débraillé. Vous feriez mieux de vous
        choisir un autre patron !
        """, "273")
    genHist.AjouterChoixGoToEffet("Si vous souhaitez vous entretenir avec le bon sorcier Gayolard", goToEffetId="335")
    genHist.AjouterChoixGoToEffet( "Si vous préférez prendre contact avec Pompatarte, l'homme à l'aura de mystère,", goToEffetId="27")

def GenererNumeros291_300(genHist):
    genHist.AjouterEffet("""
        Tandis que vous courez à toutes jambes, vous entendez un
        sifflement derrière vous. Vous jetez un regard par-dessus votre
        épaule : Stratagus vous poursuit sur un tapis volant. Vous faites
        aussitôt volte-face en brandissant votre épée, mais trop tard ! Il
        est sous l'effet d'un sortilège de Force dont lui seul a le secret et il
        vous saisit par la peau du cou puis vous emporte dans les airs.
        Vous avez beau hurler, le tapis volant s'élève de plus en plus
        haut, et, bientôt, le sorcier vous lâche. Vous tombez, vous
        tombez... et tout devient noir... Votre aventure est terminée.
        """, "297")

