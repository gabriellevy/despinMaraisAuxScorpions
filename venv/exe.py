from gen.gen_histoire import *

# stupides tests
print("------ Création de 'Le Marais aux scorpions'")
truc = GenHist("Le Marais aux scorpions")
evt1 = truc.AjouterEvt("id1");
evt2 = truc.AjouterEvt("id2");
effet1 = truc.AjouterEffet("Il se passe des choses dans cet effet d'histoire ! ", evt = evt2)
effet2 = truc.AjouterEffet("Mais vraiment plein de trucs ", evt = evt2)
print(truc._m_Histoire)
print(truc._m_Histoire.__contains__(evt1))