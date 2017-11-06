import pdb
import sys

import Calelib


def Primogiorno(g0,gs):
    if(gs[g0]==0):
        print("\t \t \t \t \t",g[0],"\t",sep='',end='')
    elif(gs[g0]==1):
        print("\t \t \t \t \t \t",g[0],"\n",sep='')
    elif(gs[g0]==2):
        print(g[0],"\t",sep='',end='')
    elif(gs[g0]==3):
        print("\t",g[0],"\t",sep='',end='')
    elif(gs[g0]==4):
        print("\t \t",g[0],"\t",sep='',end='')
    elif(gs[g0]==5):
        print("\t \t \t",g[0],"\t",sep='',end='')
    elif(gs[g0]==6):
        print("\t \t \t \t",g[0],"\t",sep='',end='')
    g0=g0+1
    return g0
    
def AltriGiorni(g0,g,gs,mesi,n):

    x=z=0
    q=n
    while(q>=0):
        x=x+mesi[q]
        q=q-1
    if(n==0):
        while(g[z]<mesi[n]):
            if(gs[g0]!=1):
                print(g[g0],"\t",sep='',end='')
            else:
                print(g[g0],"\n",sep='')
            g0=g0+1
            z=z+1
    else:
        x=x-mesi[n]
        while(g[z]<mesi[n]):
            if(gs[g0]!=1):
                print(g[g0-x],"\t",sep='',end='')
            else:
                print(g[g0-x],"\n",sep='')
            g0=g0+1
            z=z+1
    
    return g0
    
try:
    a=sys.argv[1]
except:
    a=input("Inserisci l'anno di cui vuoi generare il calendario: ")

a=int(a)
g=list()
ga=0
bis=Calelib.Bisestile(a)
if(bis==1):
    ga=366
else:
    ga=365

g0=0

mesi=[31,28,31,30,31,30,31,31,30,31,30,31]

if(bis==1):
    mesi[1]=29

while(g0<=ga):
    g.append(g0+1)
    g0=g0+1

gs=list()
g0=0

while(g0<ga):
    gs.append(Calelib.Formula(a,g[g0]))
    g0=g0+1

#g0=0
#while(g0<ga):
#   print(g[g0],"\t",gs[g0])
#    g0=g0+1

g0=0

print("\t\t\tCalendario del",a)
print("\n\n")
print("\t\t\tGennaio")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")
n=0

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tFebbraio")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tMarzo")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tAprile")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tMaggio")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tGiugno")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tLuglio")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tAgosto")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tSettembre")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tOttobre")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tNovembre")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

n=n+1
print("\n\n")
print("\t\t\tDicembre")
print("\n")
print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")

g0=Primogiorno(g0,gs)

g0=AltriGiorni(g0,g,gs,mesi,n)

print("\n\n")
