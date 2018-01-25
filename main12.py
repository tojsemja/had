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
    def __init__(self,polomer,barva,klavesy,rychlost ,start=[1,1],smer=1,smer_novy=1):
        self.body=[start]
        self.smer=smer
        self.smer_novy=smer_novy
        self.polomer=polomer
        self.barva=barva

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


    def move(self,poloha_zed_xy,poloha_cil_xy,max_x,max_y):

        if self.novy_smer==1:
            self.smer=1
        if self.novy_smer==2:
            self.smer=2
        if self.novy_smer==3:
            self.smer=3
        if self.novy_smer==4:
            self.smer=4
        posun()
            

        
        if self.body[0][1]>max_y:
            self.body[0][1]=self.body[0][1]-max_y-1
        if self.body[0][1]<0:
            self.body[0][1]=self.body[0][1]+max_y+1
            
        if self.body[0][0]>max_x:
            self.body[0][0]=self.body[0][0]-max_x-1
        if self.body[0][0]<0:
            self.body[0][0]=self.body[0][0]+max_x+1
        
        if self.body[0] in self.body[1::]:
            print("harakiri")
            konec=0
            
        if self.body[0] in poloha_zed_xy:
            print("naraz")
            konec=0

        elif(self.body[0][0]==poloha_cil_xy[0] and self.body[0][1]==poloha_cil_xy[1]):
            print("joj")
            self.rychlost+=self.rychlost/10
            
                
            self.body.append([-1,-1])
            poloha_zed_xy.append([int(random()*1000%max_x),int(random()*1000%max_y)])
            poloha_cil_xy[0]=int(random()*1000)%max_x
            poloha_cil_xy[1]=int(random()*1000)%max_y

            pygame.time.set_timer(pygame.USEREVENT+2,int(1000//rychlost))###!!!CHYBA osetrit presunem jinam.

    def nacteni(self,button):
        if(button==self.klavesy[0]):
            if(self.smer!=2):
                self.novy_smer=1
                #print("jsem tu")
        elif(button==(self.klavesy[1])):
            if(self.smer!=1):
                self.novy_smer=2
                #print("jsem tu")
        elif(button==(self.klavesy[i][2])):
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
            
pocet_hracu=2
x=2
polomer=10
rychlost=2
klavesy=[[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a],rychlost]
barva=[tyrkysova,green]

pygame.init()
cmd=0,0
time=0
polomer=10
width=1200
height=650

screen = pygame.display.set_mode((width, height),)#pamatuje si obrazovku surface - screen -cokoli do ni zapisu se da prikazem vykreslit
konec=1
max_x=int(width/(polomer*2))
max_y=int(height/(polomer*2))

poloha_zed_xy=[[int(random()*1000%max_x),int(random()*1000%max_y)]]

poloha_cil_xy=[int(random()*1000)%max_x,int(random()*1000)%max_y]



        

## start = [(2x+1),y] for x in range(3)
hadove=[(Had(polomer,barva[x],klavesy[x],rychlost,[(int(random()*1000)%max_x),(int(random()*1000)%max_y)]) for x in range (pocet_hracu))]

while(konec==1):           

    event=pygame.event.wait()

    if(event.type==pygame.QUIT):
        konec=0
        #print(height,width,polomer)
        break
    for i in hadove:
            i.nacteni()
    if(event.type==(pygame.USEREVENT+2)):
        for i in hadove:
            i.move()
        


    screen.fill(cerna)
    for i in poloha_zed_xy:
        pygame.draw.rect(screen, zluta, (i[0]*polomer*2,i[1]*polomer*2,polomer*2,polomer*2),0)
    a=event.key
    for i in hadove:
        i.vypis_hada(a)
    pygame.draw.circle(screen, cervena,(poloha_cil_xy[0]*polomer*2+polomer,poloha_cil_xy[1]*polomer*2+polomer),polomer,0)
    pygame.display.flip()




































































