import pdb
import sys

import Calelib


def Primogiorno(g0,gs,g):
    print("\n")
    print("Lu\tMa\tMe\tGi\tVe\tSa\tDo\n")
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
    while(q>0):
        x=x+mesi[q]
        q=q-1
    while(g[z]<mesi[n]):
        if(gs[g0]!=1):
            print(g[g0-x],"\t",sep='',end='')
        else:
            print(g[g0-x],"\n",sep='')
        g0=g0+1
        z=z+1
    print("\n\n")
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
nomi=["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]

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
#    print(g[g0],"\t",gs[g0])
#    g0=g0+1


g0=0

print("\n")
print("\t\t\tCalendario del",a)
print("\n")

n=0

while(n<12):
    print("\t\t\t",nomi[n],sep='')
    g0=Primogiorno(g0,gs,g)
    g0=AltriGiorni(g0,g,gs,mesi,n)
    n=n+1

print("\n")
