import sys

import Calelib

try:
    n=sys.argv[1]
except:
    n=input("Inserisci l'anno di cui vuoi conoscere i dettagli: ")

n=int(n)
p=list()
pG=list()
if(n<=1582):
    pG=Calelib.PasquaG(n)
    print("Il giorno di Pasqua dell'anno scelto è il ",pG[0],"/",pG[1],"/",n,".", sep='')
else:
    p=Calelib.Pasqua(n)
    print("Il giorno di Pasqua dell'anno scelto è il ",p[0],"/",p[1],"/",n,".", sep='')

ndo=Calelib.Numerodoro(n)
print("Il numero d'oro dell'anno dato è ",ndo,".", sep='')

ep=Calelib.Epatta(n,ndo)
print("L'epatta dell'anno inserito è ",ep,".", sep='')

cs=Calelib.CicloSolare(n)
print("Il ciclo solare dell'anno è: ",cs,".", sep='')

ir=Calelib.IndizioneRomana(n)
print("L'indizione romana dell'anno che hai inserito è ",ir,".", sep='')

mr=Calelib.MartirologioRomano(ep)
print("La lettera del martirologio romano dell'anno è ",mr,".", sep='')

bis=Calelib.Bisestile(n)
if(bis==1):
    print("L'anno scelto è bisestile.")
else:
    print("L'anno scelto non è bisestile.")

Calelib.ProssimiUguali(n)
