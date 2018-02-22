
#! python3
import pygame
from math import sqrt
from random import random
##konstanty
tyrkysova=(50,230,180)
cervena=(255,50,50)
zluta=(150,150,0)
cerna=(0,0,0)

green=(50,250,50)




class Had:
    def __init__(self,polomer,barva,klavesy,jmeno ,rychlost=10 ,start=[1,1],smer=1,smer_novy=1):
        self.body=[start]
        self.zivy=True
        self.klavesy=[(x )for x in klavesy]
        self.smer=smer
        self.novy_smer=smer_novy
        self.polomer=polomer
        self.barva=barva
        self.rychlost=rychlost
        
        self.score = 0
        self.jmeno = str(jmeno)

    def posun(self):
        for i in range (len(self.body)-1):
            
            self.body[-i-1][0]=self.body[-i-2][0]

            self.body[-i-1][1]=self.body[-i-2][1]

                
        if(self.smer==1):
            self.body[0][1]-=1
        elif(self.smer==2):
            self.body[0][1]+=1
        elif(self.smer==3):
            self.body[0][0]+=1
        elif(self.smer==4):
            self.body[0][0]-=1
            
        if self.body[0][1]>=max_y:
            self.body[0][1]=0
        if self.body[0][1]<0:
            self.body[0][1]=max_y-1     
        if self.body[0][0]>=max_x:
            self.body[0][0]=0
        if self.body[0][0]<0:
            self.body[0][0]=max_x-1


    def move(self,casovac,mapa,pricitani): ##poloha_zed_xy,poloha_cil_xy,max_x,max_y):
        konec=1
        if(event.type==(pygame.USEREVENT+casovac) and self.zivy):
            
            ##print("bu")
            if self.novy_smer==1:
                self.smer=1
            if self.novy_smer==2:
                self.smer=2
            if self.novy_smer==3:
                self.smer=3
            if self.novy_smer==4:
                self.smer=4

            x=self.body[-1][0]
            y=self.body[-1][1]
            self.posun()
            policko=mapa[self.body[0][0]][self.body[0][1]]
            mapa[x][y]='o'
            mapa[self.body[0][0]][self.body[0][1]]='h'

            
            if policko=='h':
                print("harakiri")
                self.zivy=False
                
            if policko=='z':
                print("naraz")
                self.zivy=False
                for i in range(len(poloha_zed_xy)):
                    
                    if poloha_zed_xy[i][0]==self.body[0][0] and poloha_zed_xy[i][1]==self.body[0][1]:
                        del poloha_zed_xy[i]
                        break
            if self.zivy==False:
                pygame.time.set_timer(pygame.USEREVENT+casovac,int(2000/self.rychlost))

            elif(policko=='c'):
                self.ji(mapa,casovac,pricitani)
                
                    

    
        if len(self.body)>0 and event.type==(pygame.USEREVENT+casovac) and (self.zivy)==False:

                mapa[self.body[-1][0]][self.body[-1][1]]='o'
                del self.body[-1]
                
        return konec

    def ji(self,mapa,casovac,pricitani):
        self.score+=1
        self.rychlost+=pricitani
        
            
        self.body.append([-1,-1])
        i=0
        
        poloha_zed_xy.append([int(random()*1000%max_x),int(random()*1000%max_y)])
        poloha_cil_xy[0]=int(random()*1000)%max_x
        poloha_cil_xy[1]=int(random()*1000)%max_y
        while mapa[poloha_cil_xy[0]] [poloha_cil_xy[1]] != 'o' and  mapa[poloha_zed_xy[0]] [poloha_zed_xy[1]] != 'o' and (poloha_zed_xy[-1][0] == poloha_cil_xy[0]and poloha_zed_xy[-1][1] == poloha_cil_xy[1])and i<10000 :
            i=i+1
            poloha_zed_xy.append([int(random()*1000%max_x),int(random()*1000%max_y)])
            poloha_cil_xy[0]=int(random()*1000)%max_x
            poloha_cil_xy[1]=int(random()*1000)%max_y
        #print(casovac)
        pygame.time.set_timer(pygame.USEREVENT+casovac,int(1000/self.rychlost))

        mapa[poloha_zed_xy[-1][0]][poloha_zed_xy[-1][1]]='z'
        mapa[poloha_cil_xy[0]][poloha_cil_xy[1]]='c'
                
    def nacteni(self,button):
        if(button==self.klavesy[0]):
            if(self.smer!=2):
                self.novy_smer=1
                #print("jsem tu")
        elif(button==(self.klavesy[1])):
            if(self.smer!=1):
                self.novy_smer=2
                #print("jsem tu")
        elif(button==(self.klavesy[2])):
            if(self.smer!=4):
                self.novy_smer=3
                #print("jsem tu")
        elif(button==(self.klavesy[3])):
            if(self.smer!=3):
                self.novy_smer=4
                #print("jsem tu")
        
    
    def vypis_hada(self,screen):
        for i in self.body:
            pygame.draw.circle(screen, self.barva,(i[0]*self.polomer*2+self.polomer,i[1]*self.polomer*2+self.polomer),self.polomer,0)

def cte_barva(adresa):
    barvy=[[0]]
    with open(adresa) as soubor:
        
        blud=soubor.readlines()
    jmeno=[]
    barva=[]
    k=0
    for i in range(len(blud)):
        
        inf=blud[i].split(' ')
        if len(inf)<4:
            k=k+1
            continue
        jmeno.append(inf[0])
        barva.append([int(inf[1]),int(inf[2]),int(inf[3])])
    #del barva[0]
    #del jmeno[0]
    return barva,i-k+1,jmeno

            

x=2
polomer=10
rychlost=10.0
pricitani=0.3

barva,pocet_hracu,jmeno=cte_barva("barvy.txt")
klavesy=[[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a]]#Predelat na moznost navoleni ve hre
pygame.init()
cmd=0,0
time=0
polomer=10
width=1200
height=650
text_size=3*polomer

pygame.time.set_timer(pygame.USEREVENT+1,int(1000/rychlost))
pygame.time.set_timer(pygame.USEREVENT+2,1000)#pygame.time.set_timer(pzgame.USEREVENT+1,cas) tvori event kazdy cas
odsazeni=2
for i in range (pocet_hracu):
    pygame.time.set_timer(pygame.USEREVENT+odsazeni+i+1,int(1000/rychlost))

screen = pygame.display.set_mode((width, height),)#pamatuje si obrazovku surface - screen -cokoli do ni zapisu se da prikazem vykreslit
konec=1
samota=True
max_x=int(width/(polomer*2))
max_y=int(height/(polomer*2))
mapa=[['o' for i in range(max_y)] for j in range(max_x)]

poloha_zed_xy=[[int(random()*1000%max_x),int(random()*1000%max_y)]]
mapa[poloha_zed_xy[0][0]][poloha_zed_xy[0][1]]='z'
poloha_cil_xy=[int(random()*1000)%max_x,int(random()*1000)%max_y]
mapa[poloha_cil_xy[0]][poloha_cil_xy[1]]='c'


        

## start = [(2x+1),y] for x in range(3)
hadove=[(Had(polomer,barva[x],klavesy[x],jmeno[x],rychlost,[(int(random()*1000)%max_x),(int(random()*1000)%max_y)])) for x in range (pocet_hracu)]


while(konec==1 and samota):           
    event=pygame.event.wait()
    samota=False
    for i in hadove:
        if len(i.body)>0:
            samota=True

    if(event.type==pygame.QUIT):
        konec=0
        print(height,width,polomer)
        break
    if(event.type==pygame.KEYDOWN):
        a=event.key
        for i in hadove:
            
            i.nacteni(a)
    for i in range(pocet_hracu):
        konec=hadove[i].move(i+1+odsazeni,mapa,pricitani)
        if konec==0:
            break
        


    screen.fill(cerna)
    for i in poloha_zed_xy:
        pygame.draw.rect(screen, zluta, (i[0]*polomer*2,i[1]*polomer*2,polomer*2,polomer*2),0)
        
    for i in hadove:
        i.vypis_hada(screen)
    pygame.draw.circle(screen, cervena,(poloha_cil_xy[0]*polomer*2+polomer,poloha_cil_xy[1]*polomer*2+polomer),polomer,0)
    pygame.display.flip()

##pygame.quit()
for i in range(len(hadove)):
    text = pygame.font.SysFont('arial', text_size)
    screen_text = text.render(str(hadove[i].jmeno),True,hadove[i].barva,(0,0,0) )
    screen.blit(screen_text, (text_size,(i+1)*text_size))
    screen_text = text.render(str(hadove[i].score+1),True,hadove[i].barva,(0,0,0) )
    screen.blit(screen_text, (text_size*(len(hadove[i].jmeno)+1),(i+1)*text_size))

pygame.display.flip()

while event.type!=pygame.KEYDOWN:
    event=pygame.event.wait()

pygame.quit()
































