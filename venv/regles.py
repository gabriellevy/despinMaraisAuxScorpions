from caracLDOELH import CaracLDOELH

def GenererRegles(genHist):
    genHist.AjouterEffet("""
            A certaines pages, vous aurez la possibilité de fuir un combat s'il
            vous semble devoir mal se terminer pour vous. Si vous prenez la
            Fuite, cependant, la créature vous aura automatiquement infligé
            une blessure tandis que vous vous échappez. (Vous ôterez alors
            deux points à votre ENDURANCE.) C'est le prix de la couardise.
            Pour cette blessure, vous pourrez toutefois vous servir de votre
            CHANCE selon les règles habituelles (voir page 16). La Fuite n'est
            possible que si elle est spécifiée à la page où vous vous trouverez.
            Si vous prenez la Fuite après avoir infligé une blessure à un
            ennemi, notez les modifications intervenues dans son total
            d'ENDURANCE et conservez ces indications car il est possible que
            vous reveniez plus tard dans cette clairière et que ce ou ces
            monstres s'y trouvent encore : dans ce cas, il vous faudrait peutêtre
            reprendre le combat là où vous l'aviez laissé.
            """, titre="Fuite")