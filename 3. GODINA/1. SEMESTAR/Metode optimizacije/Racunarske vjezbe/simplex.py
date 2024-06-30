#racunanje minimuma simpleks metodom u slucaju sa 2 promenljive i 2 ogranicenja
import numpy as np

g1 = np.array([[600000, 60000, 15000]])
g2 = np.array([[540000, 60000, 0]])
y = np.array([[0, -15000000, -3000000]])

tabela = np.ones((3, 3)) #, dtype=np.int32
tabela[0]=g1
tabela[1]=g2
tabela[2]=y

podeljena_prva_kolona=np.zeros((2, 1))
problem='maksimum'

def fun1(tabela, k):
    for i in range(2):
        #izbegavanje deljenja nulom
        if tabela[i, k]!=0 :
            podeljena_prva_kolona[i]=np.divide(tabela[i, 0], tabela[i, k])
        else:
            podeljena_prva_kolona[i]=0

    brojac=tabela[0][0]
    for i in range(2):
        if(podeljena_prva_kolona[i]>0 and podeljena_prva_kolona[i]<brojac):
                brojac=podeljena_prva_kolona[i]
                j=i #index pivot vrste
        else:
            continue

    pivot=tabela[j][k]
    #elementi van pivot vrste i kolone
    for i in range(3):
        for m in range(3):
            if(i!=j and m!=k):
                tabela[i][m]= tabela[i][m]- ((tabela[i][k]*tabela[j][m])/pivot)
                tabela[i][m]=round(tabela[i][m], 2)

    tabela[j][k]=round(1/pivot, 2)

    #pivot kolona
    for i in range(3):
        if(i!=j):
            tabela[i][k]=-tabela[i][k]/pivot
            tabela[i][k]=round(tabela[i][k], 2)
        else:
            continue

    #pivot vrsta   
    for i in range(3): 
        if(i!=k):
            tabela[j][i]=tabela[j][i]/pivot
            tabela[j][i]=round(tabela[j][i], 2)
        else:
            continue
    
    provera(tabela)

#provera poslednje vrste - da li je kraj
def provera(tabela):
    brojac=0
    if(problem=='minimum'):
        for i in range(3):
            if(tabela[-1][i]>brojac):
                brojac=tabela[-1][i]
                k=i #index pivot kolone
    elif(problem=='maksimum'):
        for i in range(3):
            if(abs(tabela[-1][i])>abs(brojac) and tabela[-1][i]<0):
                brojac=tabela[-1][i]
                k=i #index pivot kolone

    else:
        print("Niste uneli problem")

    print(tabela)
    if brojac==0:
        print("kraj")
    else:
        fun1(tabela, k) 


provera(tabela)