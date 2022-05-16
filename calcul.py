from Base import avalanche
Niter=100000
S,ava,duree,perte=avalanche(Niter, 30,1.25,0.2)
import os 
try:
    os.remove('fichier')
except:
    print(u'le fichier est déjà supprimé')
import pickle
fich=open('fichier','wb')
pickle.dump(S,fich)
pickle.dump(ava,fich)
pickle.dump(duree,fich)
pickle.dump(perte,fich)
fich.close()
fich=open('nb.txt','w')
fich.write(str(Niter))
fich.close()
