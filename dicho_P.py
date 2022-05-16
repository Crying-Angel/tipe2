from Base import avalanche
def tan(p):
    Niter=10000
    S,ava,duree,perte=avalanche(Niter,30,2,p)
    stan=0
    for i in range(1,len(S)-2):
        d=min(i,abs(len(S)-i))
        stan+=(S[i][i])/(np.sqrt(2)*d)
    stan=stan/((len(S))-3)
    return(stan-0.64)
def dicho(f,a,b,eps):
    g,d=a,b
    while d-g>eps:
        m=(g+d)/2
        if f(m)*f(g)>=0:
            g=m
        else:
            d=m
    return((d+g)/2)
res=open("resultat_p.txt",'w')
r=dicho(tan, 0, 1, 0.001)