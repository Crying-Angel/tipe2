import numpy as np
from Base import avalanche
h=1.1
def tan(p):
    sm=0
    n=3
    for i in range(n):
        Niter=10000
        S,ava,duree,perte=avalanche(Niter,20,h,p)
        stan=0
        for i in range(1,len(S)-2):
            d=min(i,abs(len(S)-i))
            stan+=(S[i][i])/(np.sqrt(2)*d)
        stan=stan/((len(S))-3)
        sm+=stan
    sm=sm/n
    return(sm)
def dicho(f,a,b,eps):
    assert f(a)*f(b)<0 and eps>0
    g,d=a,b
    while d-g>eps:
        m=(g+d)/2
        if f(m)*f(g)>=0:
            g=m
        else:
            d=m
    return((d+g)/2)
for j in range(1,20):
    t=int(tan(0.5)*1000)/1000
    print(h,' tan=',t)
    res=open("hp_value.txt","a")
    res.write(str(h))
    res.write("_")
    res.write(str(t))
    res.write("\n")
    res.close()
    h+=1
    h=int(h*100)/100
