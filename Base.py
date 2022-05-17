import random as rd 



   
def avalanche(Niter,taille,h,p):
    S=[[0 for j in range(taille)] for i in range(taille)]
    ava=[]
    duree=[]
    perte=[]
    for grain in range(Niter):
        ip=rd.randint(taille//2-taille//5,taille//2+taille//5)
        jp=rd.randint(taille//2-taille//5,taille//2+taille//5)
        S[ip][jp]+=1
        a=1
        atot=0
        d=0
        perdu=0
        

        while a>0:
            for i in range(1,taille-1):
                for j in range(1,taille-1):
                    pc=rd.random()

                    if ((S[i][j]-S[i][j+1]>h) or (S[i][j]-S[i][j-1]>h) or (S[i][j]-S[i+1][j]>h) or (S[i][j]-S[i-1][j]>h) )and (pc>=p) :
                        S[i][j]-=h
                        S[i][j+1]+=h/8
                        S[i][j-1]+=h/8
                        S[i+1][j]+=h/8
                        S[i-1][j]+=h/8
                        S[i+1][j+1]+=h/8
                        S[i+1][j-1]+=h/8
                        S[i-1][j-1]+=h/8
                        S[i-1][j+1]+=h/8
                        
                            
                        a+=1
                        d+=1

                    else:
                        a=0
                    atot+=a
            for i in range(taille):
                perdu+=S[i][0]
                S[i][0]=0
                perdu+=S[i][-1]
                S[i][-1]=0
            for j in range(taille):
                perdu+=S[0][j]
                S[0][j]=0
                perdu+=S[-1][j]
                S[-1][j]=0
        ava.append(atot)
        duree.append(d)
        perte.append(perdu)

    return (S,ava,duree,perte)
def sommecumul(L):
    sc=[]
    s=0
    for val in L:
        s+=val
        sc.append(s)
    return(sc)

def loiproba(variable):
    Max=max(variable)
    N=len(variable)
    loi=[]
    varalea= range(4,Max+1,4)
    for i in varalea:
        compt=0
        for var in variable:
            if var==i:
                compt+=1
        loi.append(compt/float(N))
    return(varalea,loi)



                        
