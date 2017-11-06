def PasquaG(N):
    G=N%19
    I=((19*G+15)%30)
    J=((N+N//4+I)%7)
    L=I-J
    MP=3+(L+40)//44
    GP=L+28-31*(MP//4)
    return GP,MP

def Pasqua(N):
    G=N%19
    C=N//100
    H=((C-C//4-(8*C+13)//25+19*G+15)%30)
    I=H-(H//28)*(1-(29//(H+1))*((21-G)//11))
    J=((N+N//4+I+2-C+C//4)%7)
    L=I-J
    MP=3+(L+40)//44
    GP=L+28-31*(MP//4)
    return GP,MP

def Numerodoro(N):
    s=N%19
    ndo=s+1
    return ndo

def Epatta(N,ndo):
    a=((ndo*11)-10)%30
    b=N//100-15
    c=(b-(b//25))//3
    d=(b*3)//4
    e=(d-c)%30
    if(a>e):
        ep=a-e
    else:
        ep=30-(e-a)
    return ep

def CicloSolare(N):
    cs=(N+9)%28
    if(cs==0):
        cs=28
    return cs

def IndizioneRomana(N):
    ir=(N-312)%15
    if(ir==0):
        ir=15
    return ir

def Bisestile(N):
    bis=0
    if(N<=1582):
        if(N%4==0):
            bis=1
        else:
            bis=0
    else:
        if(N%4==0):
            if(N%100==0 and N%400==0):
                bis=1
            elif(N%100==0 and N%400!=0):
                bis=0
            elif(N%100!=0):
                bis=1
    return bis
            
def EtaLuna(g,m,a,ep):
    el=0
    rl=0
    if(m==1 or m==3):
        rl=0
    elif(m==2 or m==4):
        rl=1
    elif(m==5):
        rl=2
    elif(m==6):
        rl=3
    elif(m==7):
        rl=4
    elif(m==8):
        rl=5
    elif(m==9 or m==10):
        rl=7
    elif(m==11 or m==12):
        rl=9
    
    el=ep+rl+g
    bis=Bisestile(a)
    if(el>30):
        el=el-30
    if(bis==1 and m>=3):
        el=el+1
    return el

def ProssimiUguali(N):
    
    if((N%4)==0):
        print("I prossimi anni uguali a quello inserito sono il ",N+28," e il ",N+(28*2),".",sep='');
    if(((N-1)%4)==0):
        print("I prossimi anni uguali a quello inserito sono il ",N+6,", il ",N+17," e il ",N+28,".",sep='');
    if(((N-2)%4)==0):
        print("I prossimi anni uguali a quello inserito sono il ",N+11,", il ",N+17," e il ",N+28,".",sep='');
    if(((N-3)%4)==0):
        print("I prossimi anni uguali a quello inserito sono il ",N+11,", il ",N+22," e il ",N+28,".",sep='');
    
def GiornoAnno(g,m,a):
    t=0
    if(m==1):
        t=g
    elif(m==2):
        t=31+g
    elif(m==3):
        t=31+28+g
    elif(m==4):
        t=31+28+31+g
    elif(m==5):
        t=31+28+31+30+g
    elif(m==6):
        t=31+28+31+30+31+g
    elif(m==7):
        t=31+28+31+30+31+30+g
    elif(m==8):
        t=31+28+31+30+31+30+31+g
    elif(m==9):
        t=31+28+31+30+31+30+31+31+g
    elif(m==10):
        t=31+28+31+30+31+30+31+31+30+g
    elif(m==11):
        t=31+28+31+30+31+30+31+31+30+31+g
    elif(m==12):
        t=31+28+31+30+31+30+31+31+30+31+30+g
    if(Bisestile(a)==1 and m>=3):
        t=t+1
    return t

def Formula(N,t,g=0,m=0):
    f=0
    if((N>1582) or (N==1582 and m>=10 and g>=15)):
        f=N+(N-1)//4-(N-1)//100+(N-1)//400+t
        f=f%7
    elif((N<1582) or (N==1582 and m<=10 and g<=4)):        
        f=N+(N-1)//4+t-2
        f=f%7
    return f

def DataG(g,m,a):
    gG=mG=aG=0
    bis=Bisestile(a)
    if(g>13): #13 è il numero di giorni che distaccano il calendario giuliano da quello gregoriano
        gG=g-13
        mG=m
        aG=a
    else:
        if(m>1):
            mG=m-1
            aG=a
            if(m==5 or m==7 or m==10 or m==12):
                gG=g-13+30
            elif(m==3 and bis==1):
                gG=g-13+29
            elif(m==3 and bis==0):
                gG=g-13+28
            else:
                gG=g-13+31
        else:
            aG=a-1
            mG=12
            gG=g-13+31
    
    return gG,mG,aG
    
def GiornoGiuliano(gi,me,an):
    a=(14-me)//12
    y=an+4800-a
    m=me+12*a-3
    if((an>1582) or (an==1582 and me>=10 and gi>=15)):
        JD=gi+(153*m+2)//5+365*y+y//4-y//100+y//400-32045
    elif((an<1582) or (an==1582 and me<=10 and gi <=4)):
        JD=gi+(153*m+2)//5+365*y+y//4-32083
    return JD

def GiornoSettimana(gi,me,an):
    if(me==1 or me==2):
        a=an-1
        b=a//4-a//100+a//400
        c=(a-1)//4-(a-1)//100+(a-1)//400
        s=b-c
        e=0
        f=gi-1+31*(me-1)
    else:
        a=an
        b=a//4-a//100+a//400
        c=(a-1)//4-(a-1)//100+(a-1)//400
        s=b-c
        e=s+1
        f=gi+(153*(me-3)+2)//5+58+s
    
    g=(a+b)%7
    d=(f+g-e)%7
    n=f+3-d
    
    if(n<0):
        sttmn=53-(g-s)//5
        print("Il giorno scelto cade nella ",sttmn," settimana dell'anno precedente.",sep='')
    elif(n>364+s):
        print("Il giorno scelto cade nella 1 settimana dell'anno succesivo.")
    else:
        sttmn=n//7+1
        print("Il giorno scelto cade nella ",sttmn," settimana dell'anno in corso.",sep='')
        
def MartirologioRomano(ep):
    if ep==1:
        mr="a"
    elif ep==2:
        mr="b"
    elif ep==3:
        mr="c"
    elif ep==4:
        mr="d"
    elif ep==5:
        mr="e"
    elif ep==6:
        mr="f"
    elif ep==7:
        mr="g"
    elif ep==8:
        mr="h"
    elif ep==9:
        mr="i"
    elif ep==10:
        mr="k"
    elif ep==11:
        mr="l"
    elif ep==12:
        mr="m"
    elif ep==13:
        mr="n"
    elif ep==14:
        mr="p"
    elif ep==15:
        mr="1"
    elif ep==16:
        mr="r"
    elif ep==17:
        mr="s"
    elif ep==18:
        mr="t"
    elif ep==19:
        mr="u"
    elif ep==20:
        mr="A"
    elif ep==21:
        mr="B"
    elif ep==22:
        mr="C"
    elif ep==23:
        mr="D"
    elif ep==24:
        mr="E"
    elif ep==25:
        mr="F"
    elif ep==26:
        mr="G"
    elif ep==27:
        mr="H"
    elif ep==28:
        mr="M"
    elif ep==29:
        mr="N"
    elif ep==0:
        mr="P"
    
    return mr
