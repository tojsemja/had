
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
class hadata:
    def __init__(self,telo=[[1,1]],barva=zluta,klavesy,smer=1,smerova_klavesa=1):
        self.telo=telo
        self.barva=barva
        self.klavesy=klavesy
        self.smer=smer
        self.smerova_klavesa=smerova_klavesa

    def posun(self,tela_ostatnich,poloha_zed_xy,poloha_cil_xy,rychlost):
        konec = 1
        for i in range (len(self.telo)-1):
        
            self.telo[-i-1][0]=self.telo[-i-2][0]

            self.telo[-i-1][1]=self.telo[-i-2][1]        

        if(self.smer==1):
            self.telo[0][1]-=1
        elif(self.smer==2):
            self.telo[0][1]+=1
        elif(self.smer==3):
            self.telo[0][0]+=1
        elif(self.smer==4):
            self.telo[0][0]-=1
            
        if self.novy_smer==1:
            self.smer=1
        if self.novy_smer==2:
            self.smer=2
        if self.novy_smer==3:
            self.smer=3
        if self.novy_smer==4:
            self.smer=4

        if self.telo[0][1]>max_y: self.telo[0][1]=1
        if self.telo[0][1]<0: self.telo[0][1]=max_y-1
        if self.telo[0][0]>max_x: self.telo[0][1]=1
        if self.telo[0][0]<0):self.telo[0][1]=max_x-1
            if
        
        if self.telo[0] in self.telo[1::]:
                #print("harakiri")
                konec=0

            for j in range(len(tela_ostatnich)):
                
                if self.telo[0] in tela_ostatnich[j]:
                    konec=0
                    if len(self.telo)>1:
                        if self.telo[1] in tela_ostatnich[j]:
                            konec=1
                        
                    
                
                
            if self.telo[0] in poloha_zed_xy:
                #print("naraz")
                konec=0
        
            elif(self.telo[0][0]==poloha_cil_xy[0] and self.telo[0[1]==poloha_cil_xy[1]):
                #print("joj")
                rychlost+=rychlost/10
                
                    
                self.telo.append([-1,-1])
                poloha_zed_xy.append([int(random()*1000%max_x),int(random()*1000%max_y)])
            
            ##pygame.draw.circle(kolecko,tyrkysova,(polomer,polomer), polomer, 0)
            ##zvecovani velikosti kolecka
            ##polomer+=2
            ##for i in range (len(poloha_hada_x)-1):
            ##    poloha_hada_x[i]+=1
            ##for i in range (len(poloha_hada_y)-1):
            ##    poloha_hada_y[i]+=1
                poloha_cil_xy[0]=int(random()*1000)%max_x
                poloha_cil_xy[1]=int(random()*1000)%max_y

                
        return konec


    def ovladani(self,klavesa):
        if(klavesa==(self.klavesy[0])):
            if(self.smer!=2):
                self.smerova_klavesa=1
                    #print("jsem tu")
        elif(klavesa==(self.klavesy[i][1])):
            if(self.smer[i]!=1):
                self.smerova_klavesa=2
                    #print("jsem tu")
        elif(klavesa==(self.klavesy[i][2])):
            if(self.smer[i]!=4):
                self.smerova_klavesa=3
                    #print("jsem tu")
        elif(klavesa==(self.klavesy[i][3])):
            if(self.smer[i]!=3):
                self.smerova_klavesa=4
                    #print("jsem tu")


def cte(adresa):
    znak=[['']]
    soubor=open(adresa)
    blud=soubor.read()
    j=0
    k=0
    for i in blud:
        if i=='\n':
            znak.append([i])
            j=j+1
            k=0
        else:
            znak[j].append(i)
            k=k+1
    soubor.close()
    del znak[0][0]
    return znak

def cte_barva(adresa):
    barvy=[[0]]
    soubor=open(adresa)
    blud=soubor.read()
    j=0
    k=0

    for i in blud:
        if i=='\n':
            barvy.append([0])
            j=j+1
            k=0
        elif i==',':
            k+=1
            barvy[j].append(0)
        elif i in '0123456789': 
            barvy[j][k]=barvy[j][k]*10+int(i)

            
    soubor.close()
    del barvy[-1]
    return barvy



def kolize(x1,y1,r1,x2,y2,r2):
    if(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))<(r1+r2)):
        return 1
    else:
        return 2
def interval(cislo,okraj,kolik):
    ncmd=(int(random()*10000)*kolik)%cislo
    return ncmd


            
def vypis_hada(poloha_hada_xy,polomer,barva,screen):
    for i in poloha_hada_xy:
        pygame.draw.circle(screen, barva,(i[0]*polomer*2+polomer,i[1]*polomer*2+polomer),polomer,0)
        #print(screen, barva,(i[0]*polomer*2+polomer,i[1]*polomer*2+polomer),polomer,0)


#print(10%7)
pygame.init()
cmd=0,0
time=0
polomer=10
width=1200
height=650
konstanta=1
pocet_hracu=2

rychlost=2

while (konstanta <width and konstanta<height):
    konstanta=konstanta*10
size=5
text_size=20



screen = pygame.display.set_mode((width, height),)#pamatuje si obrazovku surface - screen -cokoli do ni zapisu se da prikazem vykreslit
konec=1
max_x=int(width/(polomer*2))
max_y=int(height/(polomer*2))


    #blue=pygame.colour.Colour('blue')#do blue ulzi hodnotu z fc(R,G,B) - ta bere jakekoli html barvy
    #pygame.draw.circle(screen,(0,0,255), (160,120), 60, 10)# bere surface a do nej neco vepise (nemusi jen screen)
    #pygame.draw.circle(screen,(0,125,125), (150,110), 30,)#pygame.draw.circle(do jake matice,(0,125,125), (150,110), 30,)
    #pygame.display.flip()#vykresli obrazovku


    #cerna=pygame.Surface((1600, 600))#vytvori novy surface
    #cerna=pygame.surface.blit(sreen)#nakopiruje surface




poloha_zed_xy=[[int(random()*1000%max_x),int(random()*1000%max_y)]]



poloha_cil_xy=[int(random()*1000)%max_x,int(random()*1000)%max_y]
#barva=colour.cmk(0,0.1,1.0)#nefunguje

text = pygame.font.SysFont('arial',text_size)


skreen_text = text.render("Ahoj svete",True,tyrkysova,(0,0,0) )#vypisuje do skreenu na pozici (0,0) text.render("text",vyrovnat?(True),barva,Pozadi(None))
screen.blit(skreen_text,(text_size,20))
pygame.display.flip()
if(rychlost<1000/2):
    
    pygame.time.set_timer(pygame.USEREVENT+1,1000)#pygame.time.set_timer(pzgame.USEREVENT+1,cas) tvori event kazdy cas
    pygame.time.set_timer(pygame.USEREVENT+2,1000//rychlost)
else:
    print("Prilis velka rychlost")
#pygame.event.poll zjistuje eventy



cil=pygame.Surface((polomer*2,polomer*2))
cil.fill((0,0,0,0))
pygame.draw.circle(cil,cervena,(int(polomer/2),int(polomer/2)), int(polomer/2), 0)


copy=pygame.Surface((width, height))
kolecko=pygame.Surface((polomer*2, polomer*2))

pygame.draw.circle(kolecko,tyrkysova,(polomer,polomer), polomer, 0)

hadi=[hadata(telo=[[int(random()*1000%max_x),int(random()*1000%max_y)]],barva=tyrkysova,[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT],smer=1,smerova_klavesa=1),hadata(telo=[[int(random()*1000%max_x),int(random()*1000%max_y)]],barva=tyrkysova,[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a],smer=1,smerova_klavesa=1)]


##barva=[tyrkysova,green]
##klavesy=[[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT],[pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a]]
poloha_hada_xy=[[[int(random()*1000)%max_x,int(random()*1000)%max_y]],[[int(random()*1000)%max_x,int(random()*1000)%max_y]]]
##poloha_hada_xy=[[[int(random()*1000)%max_x,int(random()*1000)%max_y]]]
##for i in range (pocet_hracu-1):
##    poloha_hada_xy[0].append([[int(random()*1000)%max_x,int(random()*1000)%max_y]])

screen.blit(copy,(0,0),None,0)

while(konec==1):
    
    event=pygame.event.wait()#ceka na event
    #mous= pygame.mouse.get_pos()
   
    #skreen_text = text.render(str(time),True,tyrkysova,(0,0,0))
    #screen.blit(skreen_text,(text_size,20))
    
    if(event.type==pygame.QUIT):
        konec=0
        #print(height,width,polomer)
        break

    for i in poloha_hada_xy:
        if(i[0][1]>max_y or i[0][1]<0 or i[0][0]>max_x or  i[0][0]<0):
            konec=0

    if(konec==0):
        #print("koncim")
        break
    
    
    if(event.type==(pygame.USEREVENT+1)):
        time+=1
        
    if(event.type==(pygame.USEREVENT+2)):
        for i in range(hadi)
            i.posun(tela_ostatnich,poloha_zed_xy,poloha_cil_xy,rychlost)
            pygame.time.set_timer(pygame.USEREVENT+2,int(1000//rychlost))
            

    if(event.type==pygame.KEYDOWN):###prepsat na nastavitelne
        for i in range(hadi)
            i.ovladani(pygame.KEYDOWN)
        
    
    
    screen.fill(cerna)
    for i in poloha_zed_xy:
        pygame.draw.rect(screen, zluta, (i[0]*polomer*2,i[1]*polomer*2,polomer*2,polomer*2),0)


    for i in range(hadi)
        vypis_hada(i.telo,polomer,i.barva,screen)                 

    
    pygame.draw.circle(screen, cervena,(poloha_cil_xy[0]*polomer*2+polomer,poloha_cil_xy[1]*polomer*2+polomer),polomer,0)
    #print('kreslim')
    pygame.display.flip()
    
    
   
pygame.quit()






