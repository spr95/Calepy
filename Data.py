import sys

import Calelib

try:
    d=sys.argv[1]
    g,m,a=d.split("/")
except:
    d=input("Inserisci la data di cui vuoi conoscere le informazioni nel formato GG/MM/AAAA: ")
    g,m,a=d.split("/")

print(g,m,a)
g=int(g)
m=int(m)
a=int(a)
ndo=Calelib.Numerodoro(a)
ep=Calelib.Epatta(a,ndo)
el=Calelib.EtaLuna(g,m,a,ep)
print("L'età della luna alla data scelta è di ",el," giorni.", sep='')
t=Calelib.GiornoAnno(g,m,a)
bis=Calelib.Bisestile(a)
print("Il giorno scelto è il ",t," giorno dell'anno.",sep='')
if(bis==0):
    print("Mancano ",365-t," giorni alla fine dell'anno.",sep='')
else:
    print("Mancano ",366-t," giorni alla fine dell'anno.",sep='')

f=Calelib.Formula(a,t,g,m)
if(f==0):
    print("Il giorno scelto è Sabato.")
if(f==1):
    print("Il giorno scelto è Domenica.")
if(f==2):
    print("Il giorno scelto è Lunedì.")
if(f==3):
    print("Il giorno scelto è Martedì.")
if(f==4):
    print("Il giorno scelto è Mercoledì.")
if(f==5):
    print("Il giorno scelto è Giovedì.")
if(f==6):
    print("Il giorno scelto è Venerdì.")

if(a>=1900 and a<2100):    
    dG=Calelib.DataG(g,m,a)
    print("Il giorno scelto è il ",dG[0],"/",dG[1],"/",dG[2]," secondo il calendario giuliano.",sep='')

aPG=a+4713
print("L'anno scelto si trova nell'anno ",aPG," del periodo giuliano.",sep='')

gG=Calelib.GiornoGiuliano(g,m,a)
print("Il giorno scelto è il ",gG," giorno giuliano.",sep='')

Calelib.GiornoSettimana(g,m,a)
