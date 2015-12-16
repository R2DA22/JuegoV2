import pygame,sys,time,random
from pygame.locals import *
import zmq
import math
import json
import GIFImage


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def posicion(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1, imagen2,x,y):
        self.imagen_normal= imagen1
        self.imagen_seleccion= imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=x,y

    def accion(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual= self.imagen_seleccion
        else:
            self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)



    

def seleccionar_personaje(cursor):
    fondo=pygame.image.load("objetos/seleccion.png")
    img1=pygame.image.load("objetos/pj1.png")
    img2=pygame.image.load("objetos/pj2.png")
    img3=pygame.image.load("objetos/pj3.png")
    img4=pygame.image.load("objetos/pj4.png")
    seleccionar1= pygame.image.load("objetos/botones/3.png")
    seleccionar12= pygame.image.load("objetos/botones/3.3.png")
    
    salir1= pygame.image.load("objetos/botones/2.png")
    salir2= pygame.image.load("objetos/botones/2.2.png")
    boton1= Boton(seleccionar1,seleccionar12,90,450)
    boton2= Boton(seleccionar1,seleccionar12,326,450)
    boton3= Boton(seleccionar1,seleccionar12,562,450)
    boton4= Boton(seleccionar1,seleccionar12,798,450)
    boton6= Boton(salir1,salir2,800,550)

    cerrar= False

    while not cerrar:
        tecla= pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==QUIT:
                cerrar=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):
                    pygame.mixer.music.stop()
                    Game(2)
                elif cursor.colliderect(boton2.rect):
                    pygame.mixer.music.stop()
                    Game(0)
                elif cursor.colliderect(boton3.rect):
                    pygame.mixer.music.stop()
                    Game(1)
                elif cursor.colliderect(boton4.rect):
                    pygame.mixer.music.stop()
                    Game(5)
                if cursor.colliderect(boton6.rect):
                    cerrar=True
                
        cursor.posicion()
        PANTALLA.blit(fondo,(0,0))
        PANTALLA.blit(img1,(30,150))
        PANTALLA.blit(img2,(266,150))
        PANTALLA.blit(img3,(502,150))
        PANTALLA.blit(img4,(738,150))
        boton1.accion(PANTALLA,cursor)
        boton2.accion(PANTALLA,cursor)
        boton3.accion(PANTALLA,cursor)
        boton4.accion(PANTALLA,cursor)
        boton6.accion(PANTALLA,cursor)
        pygame.display.flip()

    pygame.quit()



def inicio():
    fondo=pygame.image.load("objetos/inicio.png")
    jugar1= pygame.image.load("objetos/botones/1.png")
    jugar2= pygame.image.load("objetos/botones/1.1.png")
    salir1= pygame.image.load("objetos/botones/2.png")
    salir2= pygame.image.load("objetos/botones/2.2.png")
    cursor= Cursor()
    boton1= Boton(jugar1,jugar2,700,100)
    boton2= Boton(salir1,salir2,700,200)

    cerrar= False

    while not cerrar:
        tecla= pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==QUIT:
                cerrar=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):
                    seleccionar_personaje(cursor)
                if cursor.colliderect(boton2.rect):
                    cerrar=True
                
        cursor.posicion()
        PANTALLA.blit(fondo,(0,0))
        boton1.accion(PANTALLA,cursor)
        boton2.accion(PANTALLA,cursor)
        pygame.display.flip()
    pygame.quit()
    


class Objetosinvi (pygame.sprite.Sprite):
    def __init__(self,x,y,objeto):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("objetos/"+objeto+".png")
        self.posx= x
        self.posy= y
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y= self.posx,self.posy
       
class Objetos (pygame.sprite.Sprite):
    def __init__(self,x,y,objeto):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("objetos/"+str(objeto)+".png")
        self.posx= x
        self.posy= y
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y= self.posx,self.posy

class Fondos (pygame.sprite.Sprite):
    def __init__(self,x,y,fondo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("fondos/"+str(fondo)+".png")
        self.posx= x
        self.posy= y
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y= self.posx,self.posy
        self.fondo=fondo
        
    def Cambiomapa(self,x,y,fondo):
        self.image=pygame.image.load("fondos/"+str(fondo)+".png")
    def Cambiominimapa(self,x,y,fondo):
        self.image=pygame.image.load("fondos/mini/"+str(fondo)+".png")

class Jugador(pygame.sprite.Sprite):
    def __init__(self,nombre,direc,x,y,fondo,personaje):
        pygame.sprite.Sprite.__init__(self)
        self.personaje=personaje
        self.li0= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/0.png")
        self.li1= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/1.png")
        self.li2= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/2.png")
        self.li3= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/3.png")
        self.li4= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/4.png")
        self.li5= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/5.png")
        self.li6= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/6.png")
        self.li7= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/7.png")
        self.li8= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/8.png")
        self.li9= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/9.png")
        self.ld0= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/0.png")
        self.ld1= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/1.png")
        self.ld2= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/2.png")
        self.ld3= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/3.png")
        self.ld4= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/4.png")
        self.ld5= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/5.png")
        self.ld6= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/6.png")
        self.ld7= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/7.png")
        self.ld8= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/8.png")
        self.ld9= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/9.png")
        self.t0= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/0.png")
        self.t1= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/1.png")
        self.t2= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/2.png")
        self.t3= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/3.png")
        self.t4= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/4.png")
        self.t5= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/5.png")
        self.t6= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/6.png")
        self.t7= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/7.png")
        self.t8= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/8.png")
        self.t9= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/9.png")
        self.f0= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/0.png")
        self.f1= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/1.png")
        self.f2= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/2.png")
        self.f3= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/3.png")
        self.f4= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/4.png")
        self.f5= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/5.png")
        self.f6= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/6.png")
        self.f7= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/7.png")
        self.f8= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/8.png")
        self.f9= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/9.png")

        self.Ali1= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/1.png")
        self.Ali2= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/2.png")
        self.Ali3= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/3.png")
        self.Ali4= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/4.png")
        self.Ali5= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/5.png")
        self.Ali6= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/6.png")
        self.Ali7= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/7.png")
        self.Ali8= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/8.png")
        self.Ali9= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/9.png")
        self.Ali10= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterali/10.png")

        self.Ald1= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/1.png")
        self.Ald2= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/2.png")
        self.Ald3= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/3.png")
        self.Ald4= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/4.png")
        self.Ald5= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/5.png")
        self.Ald6= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/6.png")
        self.Ald7= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/7.png")
        self.Ald8= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/8.png")
        self.Ald9= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/9.png")
        self.Ald10= pygame.image.load("Animaciones/"+str(self.personaje)+"/laterald/10.png")

        self.At1= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/1.png")
        self.At2= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/2.png")
        self.At3= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/3.png")
        self.At4= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/4.png")
        self.At5= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/5.png")
        self.At6= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/6.png")
        self.At7= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/7.png")
        self.At8= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/8.png")
        self.At9= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/9.png")
        self.At10= pygame.image.load("Animaciones/"+str(self.personaje)+"/trasero/10.png")

        self.Af1= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/1.png")
        self.Af2= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/2.png")
        self.Af3= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/3.png")
        self.Af4= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/4.png")
        self.Af5= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/5.png")
        self.Af6= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/6.png")
        self.Af7= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/7.png")
        self.Af8= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/8.png")
        self.Af9= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/9.png")
        self.Af10= pygame.image.load("Animaciones/"+str(self.personaje)+"/frontal/10.png")

        self.leonli0= pygame.image.load("Personajes/"+str(4)+"/laterali/0.png")
        self.leonli1= pygame.image.load("Personajes/"+str(4)+"/laterali/1.png")
        self.leonli2= pygame.image.load("Personajes/"+str(4)+"/laterali/2.png")
        self.leonli3= pygame.image.load("Personajes/"+str(4)+"/laterali/3.png")
        self.leonli4= pygame.image.load("Personajes/"+str(4)+"/laterali/4.png")
        self.leonli5= pygame.image.load("Personajes/"+str(4)+"/laterali/5.png")
        self.leonli6= pygame.image.load("Personajes/"+str(4)+"/laterali/6.png")
        self.leonli7= pygame.image.load("Personajes/"+str(4)+"/laterali/7.png")
        self.leonli8= pygame.image.load("Personajes/"+str(4)+"/laterali/8.png")
        self.leonli9= pygame.image.load("Personajes/"+str(4)+"/laterali/9.png")
        self.leonli10= pygame.image.load("Personajes/"+str(4)+"/laterali/10.png")

        self.leonld0= pygame.image.load("Personajes/"+str(4)+"/laterald/0.png")
        self.leonld1= pygame.image.load("Personajes/"+str(4)+"/laterald/1.png")
        self.leonld2= pygame.image.load("Personajes/"+str(4)+"/laterald/2.png")
        self.leonld3= pygame.image.load("Personajes/"+str(4)+"/laterald/3.png")
        self.leonld4= pygame.image.load("Personajes/"+str(4)+"/laterald/4.png")
        self.leonld5= pygame.image.load("Personajes/"+str(4)+"/laterald/5.png")
        self.leonld6= pygame.image.load("Personajes/"+str(4)+"/laterald/6.png")
        self.leonld7= pygame.image.load("Personajes/"+str(4)+"/laterald/7.png")
        self.leonld8= pygame.image.load("Personajes/"+str(4)+"/laterald/8.png")
        self.leonld9= pygame.image.load("Personajes/"+str(4)+"/laterald/9.png")
        self.leonld10= pygame.image.load("Personajes/"+str(4)+"/laterald/10.png")

        self.leont0= pygame.image.load("Personajes/"+str(4)+"/trasera/0.png")
        self.leont1= pygame.image.load("Personajes/"+str(4)+"/trasera/1.png")
        self.leont2= pygame.image.load("Personajes/"+str(4)+"/trasera/2.png")
        self.leont3= pygame.image.load("Personajes/"+str(4)+"/trasera/3.png")
        self.leont4= pygame.image.load("Personajes/"+str(4)+"/trasera/4.png")
        self.leont5= pygame.image.load("Personajes/"+str(4)+"/trasera/5.png")
        self.leont6= pygame.image.load("Personajes/"+str(4)+"/trasera/6.png")
        self.leont7= pygame.image.load("Personajes/"+str(4)+"/trasera/7.png")
        self.leont8= pygame.image.load("Personajes/"+str(4)+"/trasera/8.png")
        self.leont9= pygame.image.load("Personajes/"+str(4)+"/trasera/9.png")
        self.leont10= pygame.image.load("Personajes/"+str(4)+"/trasera/10.png")

        self.leonf0= pygame.image.load("Personajes/"+str(4)+"/frontal/0.png")
        self.leonf1= pygame.image.load("Personajes/"+str(4)+"/frontal/1.png")
        self.leonf2= pygame.image.load("Personajes/"+str(4)+"/frontal/2.png")
        self.leonf3= pygame.image.load("Personajes/"+str(4)+"/frontal/3.png")
        self.leonf4= pygame.image.load("Personajes/"+str(4)+"/frontal/4.png")
        self.leonf5= pygame.image.load("Personajes/"+str(4)+"/frontal/5.png")
        self.leonf6= pygame.image.load("Personajes/"+str(4)+"/frontal/6.png")
        self.leonf7= pygame.image.load("Personajes/"+str(4)+"/frontal/7.png")
        self.leonf8= pygame.image.load("Personajes/"+str(4)+"/frontal/8.png")
        self.leonf9= pygame.image.load("Personajes/"+str(4)+"/frontal/9.png")
        self.leonf10= pygame.image.load("Personajes/"+str(4)+"/frontal/10.png")


        self.Aleonli1= pygame.image.load("Animaciones/"+str(4)+"/laterali/1.png")
        self.Aleonli2= pygame.image.load("Animaciones/"+str(4)+"/laterali/2.png")
        self.Aleonli3= pygame.image.load("Animaciones/"+str(4)+"/laterali/3.png")
        self.Aleonli4= pygame.image.load("Animaciones/"+str(4)+"/laterali/4.png")
        self.Aleonli5= pygame.image.load("Animaciones/"+str(4)+"/laterali/5.png")
        self.Aleonli6= pygame.image.load("Animaciones/"+str(4)+"/laterali/6.png")
        self.Aleonli7= pygame.image.load("Animaciones/"+str(4)+"/laterali/7.png")
        self.Aleonli8= pygame.image.load("Animaciones/"+str(4)+"/laterali/8.png")
        self.Aleonli9= pygame.image.load("Animaciones/"+str(4)+"/laterali/9.png")
        self.Aleonli10= pygame.image.load("Animaciones/"+str(4)+"/laterali/10.png")

       
        self.Aleonld1= pygame.image.load("Animaciones/"+str(4)+"/laterald/1.png")
        self.Aleonld2= pygame.image.load("Animaciones/"+str(4)+"/laterald/2.png")
        self.Aleonld3= pygame.image.load("Animaciones/"+str(4)+"/laterald/3.png")
        self.Aleonld4= pygame.image.load("Animaciones/"+str(4)+"/laterald/4.png")
        self.Aleonld5= pygame.image.load("Animaciones/"+str(4)+"/laterald/5.png")
        self.Aleonld6= pygame.image.load("Animaciones/"+str(4)+"/laterald/6.png")
        self.Aleonld7= pygame.image.load("Animaciones/"+str(4)+"/laterald/7.png")
        self.Aleonld8= pygame.image.load("Animaciones/"+str(4)+"/laterald/8.png")
        self.Aleonld9= pygame.image.load("Animaciones/"+str(4)+"/laterald/9.png")
        self.Aleonld10= pygame.image.load("Animaciones/"+str(4)+"/laterald/10.png")

       
        self.Aleont1= pygame.image.load("Animaciones/"+str(4)+"/trasero/1.png")
        self.Aleont2= pygame.image.load("Animaciones/"+str(4)+"/trasero/2.png")
        self.Aleont3= pygame.image.load("Animaciones/"+str(4)+"/trasero/3.png")
        self.Aleont4= pygame.image.load("Animaciones/"+str(4)+"/trasero/4.png")
        self.Aleont5= pygame.image.load("Animaciones/"+str(4)+"/trasero/5.png")
        self.Aleont6= pygame.image.load("Animaciones/"+str(4)+"/trasero/6.png")
        self.Aleont7= pygame.image.load("Animaciones/"+str(4)+"/trasero/7.png")
        self.Aleont8= pygame.image.load("Animaciones/"+str(4)+"/trasero/8.png")
        self.Aleont9= pygame.image.load("Animaciones/"+str(4)+"/trasero/9.png")
        self.Aleont10= pygame.image.load("Animaciones/"+str(4)+"/trasero/10.png")

        
        self.Aleonf1= pygame.image.load("Animaciones/"+str(4)+"/frontal/1.png")
        self.Aleonf2= pygame.image.load("Animaciones/"+str(4)+"/frontal/2.png")
        self.Aleonf3= pygame.image.load("Animaciones/"+str(4)+"/frontal/3.png")
        self.Aleonf4= pygame.image.load("Animaciones/"+str(4)+"/frontal/4.png")
        self.Aleonf5= pygame.image.load("Animaciones/"+str(4)+"/frontal/5.png")
        self.Aleonf6= pygame.image.load("Animaciones/"+str(4)+"/frontal/6.png")
        self.Aleonf7= pygame.image.load("Animaciones/"+str(4)+"/frontal/7.png")
        self.Aleonf8= pygame.image.load("Animaciones/"+str(4)+"/frontal/8.png")
        self.Aleonf9= pygame.image.load("Animaciones/"+str(4)+"/frontal/9.png")
        self.Aleonf10= pygame.image.load("Animaciones/"+str(4)+"/frontal/10.png")

        self.imagenes=[[self.li0,self.li1,self.li2,self.li3,self.li4,self.li5,self.li6,self.li7,self.li8,self.li9],[self.ld0,self.ld1,self.ld2,self.ld3,self.ld4,self.ld5,self.ld6,self.ld7,self.ld8,self.ld9],[self.t0,self.t1,self.t2,self.t3,self.t4,self.t5,self.t6,self.t7,self.t8,self.t9],[self.f0,self.f1,self.f2,self.f3,self.f4,self.f5,self.f6,self.f7,self.f8,self.f9]]
        self.ataques=[[self.Ali1,self.Ali2,self.Ali3,self.Ali4,self.Ali5,self.Ali6,self.Ali7,self.Ali8,self.Ali9,self.Ali10],[self.Ald1,self.Ald2,self.Ald3,self.Ald4,self.Ald5,self.Ald6,self.Ald7,self.Ald8,self.Ald9,self.Ald10],[self.At1,self.At2,self.At3,self.At4,self.At5,self.At6,self.At7,self.At8,self.At9,self.At10],[self.Af1,self.Af2,self.Af3,self.Af4,self.Af5,self.Af6,self.Af7,self.Af8,self.Af9,self.Af10]]
        self.leon=[[self.leonli0,self.leonli1,self.leonli2,self.leonli3,self.leonli4,self.leonli5,self.leonli6,self.leonli7,self.leonli8,self.leonli9,self.leonli10],[self.leonld0,self.leonld1,self.leonld2,self.leonld3,self.leonld4,self.leonld5,self.leonld6,self.leonld7,self.leonld8,self.leonld9,self.leonld10],[self.leont0,self.leont1,self.leont2,self.leont3,self.leont4,self.leont5,self.leont6,self.leont7,self.leont8,self.leont9,self.leont10],[self.leonf0,self.leonf1,self.leonf2,self.leonf3,self.leonf4,self.leonf5,self.leonf6,self.leonf7,self.leonf8,self.leonf9,self.leonf10]]
        self.ataqueleon=[[self.Aleonli1,self.Aleonli2,self.Aleonli3,self.Aleonli4,self.Aleonli5,self.Aleonli6,self.Aleonli7,self.Aleonli8,self.Aleonli9,self.Aleonli10],[self.Aleonld1,self.Aleonld2,self.Aleonld3,self.Aleonld4,self.Aleonld5,self.Aleonld6,self.Aleonld7,self.Aleonld8,self.Aleonld9,self.Aleonld10],[self.Aleont1,self.Aleont2,self.Aleont3,self.Aleont4,self.Aleont5,self.Aleont6,self.Aleont7,self.Aleont8,self.Aleont9,self.Aleont10],[self.Aleonf1,self.Aleonf2,self.Aleonf3,self.Aleonf4,self.Aleonf5,self.Aleonf6,self.Aleonf7,self.Aleonf8,self.Aleonf9,self.Aleonf10]]
        self.nombre=nombre
        self.salud=100
        self.vidas=3
        self.vida=self.salud
        self.manatotal=100
        self.mana=self.manatotal
        self.x=x
        self.y=y
        self.i=1
        self.personaje_Actualy=0
        self.direc=direc
        self.pasos=20
        self.pasosy=10
        self.vx=0
        self.vy=0
        self.t=0
        self.animacionsalto=False
        self.animacion=False
        self.personaje_Actual=0
        self.image=self.imagenes[self.personaje_Actual][0]
        self.ancho_image,self.alto_image= self.image.get_size()
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=self.x,self.y
        self.direcchoque=0
        self.choque=False
        self.fondo=fondo
        self.muestramapa=False
        self.choqueobjetos=False
        self.copia=self.personaje
        self.gastarmana=False
        self.dano=5
        self.nombreinterfas=Nombre()
        self.manainterfas=Mana()
        self.vidainterfas=Vida()
        self.lastimar=False
        self.moving=False
        self.Orientacion=direc
        self.transformado=False

           
    def chocarpbjetos(self,ob):
        activado=True
        for col in ob:
            if pygame.sprite.collide_rect(self,col):
                if self.Orientacion==2 and activado:
                    self.y+=25
                    activado=False
                    
                if self.Orientacion==3 and activado:
                    self.y-=25
                    activado=False
                    
                if self.Orientacion==1 and activado:
                    self.x-=25
                    activado=False

                if self.Orientacion==0 and activado:
                    self.x+=25
                    activado=False

                self.rect.x=self.x
                self.rect.y=self.y

    def chocarpvp(self,socket_server,ob):
    	    
            if pygame.sprite.collide_rect(self,ob):              
                    """if ob.Orientacion==0 and (self.Orientacion==0 or self.Orientacion==3 or self.Orientacion==2):
                        self.x=self.x
                        
                        
                    elif ob.Orientacion==1 and (self.Orientacion==1 or self.Orientacion==3 or self.Orientacion==2):
                        self.x=self.x
                        

                    elif ob.Orientacion==2 and (self.Orientacion==0 or self.Orientacion==2 or self.Orientacion==1):
                        self.y=self.y
                        
                    elif ob.Orientacion==3 and (self.Orientacion==0 or self.Orientacion==3 or self.Orientacion==1):
                        self.y=self.y
                        
                    else:
                        if self.Orientacion==0:
                            self.x+=25

                        if self.Orientacion==1:
                            self.x-=25
                            
                        if self.Orientacion==2:
                            self.y+=25
                            
                        if self.Orientacion==3:
                            self.y-=25"""
                            
                        
                    if(self.lastimar):
                        ob.vida-=self.dano
                        self.lastimar=False
                        if(ob.vida <= 0):
                            print ("perdio una vida")
                            ob.vidas-=1
                            ob.vida=100
                            valor=random.randint(1,18) 
                            ob.fondo=valor
                            action="dead"
                        else:
                        	action="dano"


                        dic={"mapa":ob.fondo,"vidas": ob.vidas,"vida": ob.vida,"username":ob.nombre}
                        socket_server.send_multipart([action,json.dumps(dic,sort_keys=True)])

            else:
            	self.lastimar=False 

    def transformar(self):
        self.transformado=True
        self.personaje=4
        self.image=self.leon[self.Orientacion][self.personaje_Actual]
        self.dano+=5
        self.gastarmana =True 
        

    def destransformar(self):
        self.transformado=False
        self.personaje=self.copia
        self.dano-=5
        self.gastarmana =False 
                   
                         

    def perdidavida(self):
      if(self.vida <= self.salud-10):
        self.vida=self.vida-10

    def perdidamana(self):
        self.mana=self.mana-10

    def aumentovida(self):
        if(self.vida <= self.salud-10):
            self.vida=self.vida+10
            self.perdidamana()
        else:
            self.perdidamana()

    def aumentomana(self):
        if(self.mana <= self.manatotal-10):
            self.vida=self.mana+10

    def move(self):
          if self.vx < 0:
            self.Orientacion=0
          if self.vx > 0:
            self.Orientacion=1
          if self.vy < 0:
            self.Orientacion=2
          if self.vy > 0:
            self.Orientacion=3

          if self.moving:
            self.personaje_Actual+=1
            if self.personaje_Actual > 9:
                self.personaje_Actual=1
           
            self.x+=self.vx
            self.y+=self.vy 
          else:
            self.t=0
            self.personaje_Actual=0
          self.rect.x=self.x
          self.rect.y=self.y
          if self.transformado:
            self.image=self.leon[self.Orientacion][self.personaje_Actual]
          else:
            self.image=self.imagenes[self.Orientacion][self.personaje_Actual]
         
          

         
    

    def interfase(self):
         propiedades= pygame.sprite.Group()
         self.vidainterfas.vid(self.vida,self.rect.x,self.rect.y)
         self.manainterfas.man(self.mana,self.rect.x,self.rect.y)
         self.nombreinterfas.nom(self.nombre,self.rect.x,self.rect.y)
         propiedades.add(self.vidainterfas)
         propiedades.add(self.manainterfas)
         propiedades.add(self.nombreinterfas)
         return propiedades
        
    def anima(self):

        if(self.Orientacion==2):
            if(self.personaje_Actualy<9):
                self.personaje_Actualy=self.personaje_Actualy+1
            else:
             self.personaje_Actualy=0
             self.animacion=False
             self.lastimar=True

        if(self.Orientacion==3):
            if(self.personaje_Actualy<9):
                self.personaje_Actualy=self.personaje_Actualy+1
            else:
                self.personaje_Actualy=0
                self.animacion=False
                self.lastimar=True

        if(self.Orientacion==0 ):
            if(self.personaje_Actualy<9):
             
             self.personaje_Actualy=self.personaje_Actualy+1
            else:
                self.personaje_Actualy=0
                self.animacion=False
                self.lastimar=True

        if(self.Orientacion==1 ):
            if(self.personaje_Actualy<9):
             
             self.personaje_Actualy=self.personaje_Actualy+1
            else:
                self.personaje_Actualy=0
                self.animacion=False
                self.lastimar=True
        self.rect.x=self.x
        self.rect.y=self.y
        if self.transformado:
            self.image=self.ataqueleon[self.Orientacion][self.personaje_Actualy]
        else:
            self.image=self.ataques[self.Orientacion][self.personaje_Actualy]

        
        

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,nombre,direc,x,y,cx,cy,peligro,dano,vida,mana,personaje):
        pygame.sprite.Sprite.__init__(self)
        self.nombre=nombre
        self.vida=vida
        self.mana=mana
        self.x=x
        self.y=y
        self.Cx=cx
        self.Cy=cy
        self.xaux=x
        self.yaux=y
        self.i=1
        self.direc=direc
        self.pasos=5
        self.dano=dano

        if(direc==4):
         self.Pj=pygame.image.load("Personajes/"+str(personaje)+"/laterali/"+str(0)+".png")
        if(direc==2):
         self.Pj=pygame.image.load("Personajes/"+str(personaje)+"/frontal/"+str(0)+".png")
        if(direc==6):
         self.Pj=pygame.image.load("Personajes/"+str(personaje)+"/laterald/"+str(0)+".png")
        if(direc==8):
         self.Pj=pygame.image.load("Personajes/"+str(personaje)+"/trasera/"+str(0)+".png")

        self.Peligro=peligro
        self.iy=1
        self.animacion=True
        self.personaje=personaje
        self.image=self.Pj
        self.ancho_image,self.alto_image= self.image.get_size()
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=self.x,self.y
        self.choque=True
        self.ataca=False
        self.bajarvida=0
        self.nombreinterfas=Nombre()
        self.manainterfas=Mana()
        self.vidainterfas=Vida()


    def atacar(self,jugador):
        self.anima(self.personaje)
        self.ataca=True

    def distancia(self,jugadorx,jugadory):
        aux=math.sqrt(math.pow((jugadorx-self.x),2)+math.pow((jugadory-self.y),2))
        return aux        

    def interfase(self):
         propiedades= pygame.sprite.Group()
         self.vidainterfas.vid(self.vida,self.rect.x,self.rect.y)
         self.manainterfas.man(self.mana,self.rect.x,self.rect.y)
         self.nombreinterfas.nom(self.nombre,self.rect.x,self.rect.y)
         propiedades.add(self.vidainterfas)
         propiedades.add(self.manainterfas)
         propiedades.add(self.nombreinterfas)
         return propiedades

    def perseguir(self,jugadorx,jugadory,direc):
            if(jugadorx<self.x):
                  if(9>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/"+str(self.i)+".png")
                    self.x-=self.pasos
                    self.i+=1
                    self.direc=4
                  else: self.i=1

            if(jugadorx>self.x):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/"+str(self.i)+".png")
                    self.x+=self.pasos
                    self.i+=1
                    self.direc=6
                  else: self.i=1

            if(jugadory>self.y):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/"+str(self.i)+".png")
                    self.y+=self.pasos
                    self.i+=1
                    self.direc=2
                  else: self.i=1

            if(jugadory<self.y):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/"+str(self.i)+".png")
                    self.y-=self.pasos
                    self.i+=1
                    self.direc=8
                  else: self.i=1
            self.rect.x=self.x
            self.rect.y=self.y
            self.image=self.Pj

    def rutina(self):
            if((self.xaux-self.Cx<=self.x  and  self.yaux<=self.y) or (self.yaux-self.Cy<=self.y and self.xaux-self.Cx>=self.x  ) or (self.yaux-self.Cy>=self.y and self.xaux>=self.x  ) or (self.xaux <= self.x and self.yaux>=self.y )):

              if(self.xaux-self.Cx<=self.x  and  self.yaux<=self.y):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/"+str(self.i)+".png")
                    self.x-=self.pasos
                    self.i+=1
                    self.direc=4
                  else: self.i=1

              if(self.yaux-self.Cy<=self.y and self.xaux-self.Cx>=self.x  ):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/"+str(self.i)+".png")
                    self.y-=self.pasos
                    self.i+=1
                    self.direc=8
                  else: self.i=1

              if(self.yaux-self.Cy>=self.y and self.xaux>=self.x  ):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/"+str(self.i)+".png")
                    self.x+=self.pasos
                    self.i+=1
                    self.direc=6
                  else: self.i=1

              if(self.xaux <= self.x and self.yaux>=self.y ):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/"+str(self.i)+".png")
                    self.y+=self.pasos
                    self.i+=1
                    self.direc=2
                  else: self.i=1

            else:
              if(self.xaux<=self.x ):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/laterali/"+str(self.i)+".png")
                    self.x-=self.pasos
                    self.i+=1
                    self.direc=4
                  else: self.i=1

              elif(self.yaux>=self.y):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/frontal/"+str(self.i)+".png")
                    self.y+=self.pasos
                    self.i+=1
                    self.direc=2
                  else: self.i=1

              elif(self.xaux>=self.x):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/laterald/"+str(self.i)+".png")
                    self.x+=self.pasos
                    self.i+=1
                    self.direc=6
                  else: self.i=1

              elif(self.yaux<=self.y  ):
                  if(10>=self.i):
                    self.Pj= pygame.image.load("Personajes/"+str(self.personaje)+"/trasera/"+str(self.i)+".png")
                    self.y-=self.pasos
                    self.i+=1
                    self.direc=8
                  else: self.i=1
            self.rect.x=self.x
            self.rect.y=self.y
            self.image=self.Pj
          
    def anima(self,ani):
        self.animacion=True
        self.bajarvida=0
        if(self.direc==2):
            if(self.direc==2 and self.iy<=10):
                self.Pj= pygame.image.load("Animaciones/"+str(ani)+"/frontal/"+str(self.iy)+".png")
                self.iy=self.iy+1
                self.direc=2
            else:
             self.iy=1
             self.animacion=False
             self.direc=2
             self.bajarvida=1

        if(self.direc==8):
            if(self.direc==8 and self.iy<=10):
                self.Pj= pygame.image.load("Animaciones/"+str(ani)+"/trasero/"+str(self.iy)+".png")
                self.iy=self.iy+1
                self.direc=8
            else:
                self.iy=1
                self.animacion=False
                self.direc=8
                self.bajarvida=1

        if(self.direc==4 ):
            if(self.direc==4 and self.iy<=10):
             self.Pj= pygame.image.load("Animaciones/"+str(ani)+"/laterali/"+str(self.iy)+".png")
             self.iy=self.iy+1
             self.direc=4
            else:
                self.iy=1
                self.animacion=False
                self.direc=4
                self.bajarvida=1

        if(self.direc==6 ):
            if(self.direc==6 and self.iy<=10):
             self.Pj= pygame.image.load("Animaciones/"+str(ani)+"/laterald/"+str(self.iy)+".png")
             self.iy=self.iy+1
             self.direc=6
            else:
                self.iy=1
                self.animacion=False
                self.direc=6
                self.bajarvida=1
                
        self.rect.x=self.x
        self.rect.y=self.y
        self.image=self.Pj
        
    def __del__(self):
        print("muerto")

class Vida (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_caption("Modulo de fuentes")
        fuente =pygame.font.SysFont("Arial", 30)
        texto1 = fuente.render("",0,(255, 0, 0))
        self.image=texto1
        self.rect=self.image.get_rect()
        
    def vid(self,vida,x,y):
        pygame.display.set_caption("Modulo de fuentes")
        fuente =pygame.font.SysFont("Arial", 20)
        texto2 = fuente.render(str(vida),0,(255, 0, 0))
        self.image=texto2
        self.rect.x=x
        self.rect.y=y
        self.vida=vida
        
class Mana (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_caption("Modulo de fuentes")
        fuente =pygame.font.SysFont("Arial", 30)
        texto1 = fuente.render("",0,(255, 0, 0))
        self.image=texto1
        self.rect=self.image.get_rect()
        
    def man(self,vida,x,y):
        pygame.display.set_caption("Modulo de fuentes")
        fuente =pygame.font.SysFont("Arial", 20)
        texto2 = fuente.render(str(vida),0,(255, 255, 0))
        self.image=texto2
        self.rect.x=x+110
        self.rect.y=y
        
class Nombre (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_caption("Modulo de fuentes")
        fuente =pygame.font.SysFont("Arial", 30)
        texto1 = fuente.render("",0,(255, 255, 0))
        self.image=texto1
        self.rect=self.image.get_rect()
        
    def nom(self,vida,x,y):
        pygame.display.set_caption("Modulo de fuentes")
        fuente =pygame.font.SysFont("Arial", 20)
        texto2 = fuente.render(str(vida),0,(255, 0, 255))
        self.image=texto2
        self.rect.x=x+50
        self.rect.y=y-30


class AnimacionMapa (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        
    def Goanimacion(self,socket_server,fondo,players,enemigos,jugador,jugadores,objetos,retornar,nombre_vida_mana):
        
       #CARGAR ELEMENTOS DEL MAPA EN CUESTION
        retornar.add(objetos)     
        retornar.add(enemigos)
       #INTERFAS VIDA MANA NOMBRE
        """aux=0
        iterador=0
        index=0
        for col in enemigos:
            nombre_vida_mana.add(col.interfase())
            retornar.add(nombre_vida_mana)
            bandera=0
            bandera2=1
        #SI SE DESTRUYE UN ENEMIGO SAQUELO DE LISTA ENEMIGOS LISTA MAPA Y QUITE LA INTERFAS
            if(col.vida<=0):
                retornar.remove(col)
                enemigos.remove(col)
                retornar.remove(col.interfase())
                nombre_vida_mana.remove(col.interfase()) 
        #COLICION ENEMIGOS CON JUGADORES
            for jugador in jugadores:
          #SI JUGADOR ESTA COLISIONANDO CON ENEMIGO 
                if pygame.sprite.collide_rect(col,jugador):    
                    col.atacar(jugador)
                    bandera2=1
                    bandera=1
                    if(col.bajarvida):
                        jugador.vida=jugador.vida-col.dano
                elif(jugador.x+col.Peligro>col.x and jugador.y+col.Peligro>col.y and jugador.y<col.y+col.Peligro and jugador.x<col.x+col.Peligro ): 
                        temp=col.distancia(jugador.x,jugador.y)
                        if aux==0: 
                            aux=temp
                            index=jugador.personaje
                        elif temp < aux:
                            aux=temp
                            index=jugador.personaje
                        bandera2=0
                        bandera=1   
            
            if bandera2==0:                      
                for jugador in jugadores:
                    if jugador.personaje == index:
                        atacar_jugador=players[jugador.nombre]        
                col.perseguir(atacar_jugador.x,atacar_jugador.y,atacar_jugador.direc)
            if bandera==0:
                col.choque=True
                col.rutina()
                col.ataca=False"""

        #COLICION JUGADORES
        for col in jugadores:
            if col.nombre != jugador.nombre:
                    jugador.chocarpvp(socket_server,col)
        for  gamer in players.values():
            if not gamer.animacion:
                
                gamer.move()
                gamer.chocarpbjetos(objetos)#COLICION JUGADORES CON OBJETOS
            else:
                gamer.anima()
        #jugador.chocarpbjetos(objetos)
        
        
         

        return retornar

    def KillAnimacion(self,enemigos,objetos,retornar,nombre_vida_mana):
         retornar.remove(enemigos)
         retornar.remove(objetos)
         retornar.remove(nombre_vida_mana)
         return retornar

def manejo_mapas(fondo,player,x,y,fondo_aux,socket_server):
    fondo.Cambiomapa(-330,0,fondo_aux)
    player.x=x
    player.y=y
    player.fondo=fondo_aux
    fondo.fondo=fondo_aux
    if(player.muestramapa):
        fondo.Cambiominimapa(-330,0,player.fondo)
    dic={"mapa":fondo_aux,"username":player.nombre}
    socket_server.send_multipart(["mapeo",json.dumps(dic,sort_keys=True)])



def from_server(action,player,username,dic1,fondo): 
    if action=="move":
        
        if player.nombre != username:
             if(dic1["i"] <= 10):  
                player.personaje_Actual=dic1["i"]
             else:
                player.personaje_Actual=0
             player.rect.x=dic1["posx"]
             player.rect.y=dic1["posy"]
             player.x=dic1["posx"]
             player.y=dic1["posy"]
             player.Orientacion=dic1["direc"]
             player.t=dic1["t"]
             player.vx=dic1["vx"]
             player.vy=dic1["vy"]
             player.moving=True
             player.image=player.imagenes[player.Orientacion][player.personaje_Actual]
    if action == "golpe":
        print "golpe"
        player.animacion=True

    if action=="mapeo":
        player.fondo=dic1["mapa"]
    if action  == "dano" or action=="dead":
        
        player.vida=dic1["vida"]
        player.vidas=dic1["vidas"]
        player.fondo=dic1["mapa"]
        if player.nombre==username:
             fondo.Cambiomapa(-330,0,dic1["mapa"])
             fondo.fondo=dic1["mapa"]
    if action == "transformar":
        if dic1["morph"]:
             player.transformar()
        else:
             player.destransformar()
    if action == "stop":
        player.moving=False
        

#_________________________________________INICIO DEL JUEGO_______________________________________
def Game(n):

  init =False
  players={}
  #____________________________________________________________Establecer conexion con el servidor
  ctx = zmq.Context()
  socket_server = ctx.socket(zmq.XREQ)
  socket_server.connect('tcp://'+sys.argv[2]+':5555')

  msg="connect"
  username=sys.argv[1]
  socket_server.send_multipart([msg,username,json.dumps(n,sort_keys=True)])
  poller = zmq.Poller()
  poller.register(socket_server, zmq.POLLIN)
  ANCHO = int(1000)
  ALTO = int(700)
  pygame.init()
  pygame.key.set_repeat(1,50)
  PANTALLA= pygame.display.set_mode([ANCHO,ALTO])
  #MAPEO
  mapeo= pygame.sprite.Group()
  jugadores= pygame.sprite.Group()
  nombre_vida_manajugador= pygame.sprite.Group()
  terminar= False
  fondo=pygame.image.load("fondos/fondoEspera.png")
  c = GIFImage.GIFImage("fondos/buscando.gif")
  PANTALLA.blit(fondo,(0,0))
  counter=True
  speed=20
  t=0
  leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
  count_move=0
  count_shut=0
  while not terminar:
    
    if not init:
         for event in pygame.event.get():
               if event.type == QUIT:
                    pygame.quit()
                    return
         c.render(PANTALLA, (350, 200))
         pygame.display.flip()
    socks = dict(poller.poll(1))
    if socket_server in socks and socks[socket_server] == zmq.POLLIN:
      j=0
      action=socket_server.recv()
      
     
      if action=="connect":
          number_players=int(json.loads(socket_server.recv()))
          while j<number_players:
            dic=json.loads(socket_server.recv())
            jugador_temp=Jugador(dic["username"],dic["direc"],dic["posx"],dic["posy"],dic["fondo"],dic["personaje"])
            players[dic["username"]]=jugador_temp
            if 1==dic["fondo"]:
            	jugadores.add(jugador_temp)
                mapeo.add(jugador_temp)
                nombre_vida_manajugador.add(jugador_temp.interfase())
                mapeo.add(nombre_vida_manajugador)
            j+=1
          if counter:
              counter=False
              init=True
              #FONDO INICIAL
              fondos= pygame.sprite.Group()
              fondo= Fondos(-330,0,players[username].fondo)
              fondos.add(fondo)
              #INICIALIZARPERSONAJEPRINCIPAL
              AnimacionMapas=AnimacionMapa()
              #MAPA 1_____________________________________________________________INICIO MAPA 1
              enemigos= pygame.sprite.Group()
              objetos= pygame.sprite.Group()

              #__________________ENEMIGOS

              #enemigo=Enemigo("Ronal",8,200,400,100,100,100,1,100,100,0)
              #enemigos.add(enemigo)
              mapeo.add(enemigos)

              #___________________OBJETOS 
              ob1= Objetosinvi(850,550,"150-150")
              ob2= Objetosinvi(700,580,"150-150")
              ob3= Objetosinvi(550,600,"150-150")
              ob4= Objetosinvi(400,620,"150-150")
              ob5= Objetosinvi(-30,620,"150-150")
              ob6= Objetosinvi(-30,550,"150-150")
              ob7= Objetosinvi(300,-70,"50-50")
              ob8= Objetosinvi(400,-80,"150-150")
              ob9= Objetosinvi(840,190,"50-50")
              ob10= Objetosinvi(460,260,"10-10")

              objetos.add(ob1)
              objetos.add(ob2)
              objetos.add(ob3)
              objetos.add(ob4)
              objetos.add(ob5)
              objetos.add(ob6)
              objetos.add(ob7)
              objetos.add(ob8)
              objetos.add(ob9)
              objetos.add(ob10)

              mapeo.add(objetos)
              #_________________________________________________________________FIN DE MAPA 1

              #MAPA 2___________________________________________________________INICIO MAPA 2
              enemigos2= pygame.sprite.Group()
              objetos1= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("Ronal",8,200,400,100,100,100,1,100,100,0)
              enemigo1=Enemigo("Reinosa",2,400,400,400,300,250,1,100,100,0)
              enemigo2=Enemigo("Cristian",6,500,500,400,400,200,1,100,100,0)
              enemigo3=Enemigo("Risitas",4,400,500,400,400,150,1,100,100,0)
              enemigo4=Enemigo("Ronal",8,550,530,400,400,100,1,100,100,0)

              enemigos2.add(enemigo)
              enemigos2.add(enemigo1)
              enemigos2.add(enemigo2)
              enemigos2.add(enemigo3)
              enemigos2.add(enemigo4)"""


              #___________________OBJETOS 

              ob1= Objetosinvi(0,650,"50-50")
              ob2= Objetosinvi(50,650,"50-50")
              ob3= Objetosinvi(100,650,"50-50")
              ob4= Objetosinvi(420,660,"50-50")
              ob5= Objetosinvi(190,-50,"150-150")
              ob6= Objetosinvi(0,0,"50-50")
              ob7= Objetosinvi(30,-30,"50-50")
              ob8= Objetosinvi(350,330,"10-10")


              ob10= Objetosinvi(600,390,"10-10")
              ob11= Objetosinvi(620,410,"10-10")
              ob12= Objetosinvi(640,430,"10-10")
              ob13= Objetosinvi(660,450,"10-10")
              ob14= Objetosinvi(680,470,"10-10")
              ob15= Objetosinvi(700,480,"10-10")
              ob16= Objetosinvi(720,500,"10-10")
              ob17= Objetosinvi(740,490,"10-10")
              ob18= Objetosinvi(760,500,"10-10")
              ob19= Objetosinvi(780,510,"10-10")
              ob20= Objetosinvi(790,500,"10-10")

              ob22= Objetosinvi(1000,0,"1000")
              objetos1.add(ob22)


              objetos1.add(ob1)
              objetos1.add(ob2)
              objetos1.add(ob3)
              objetos1.add(ob4)
              objetos1.add(ob5)
              objetos1.add(ob6)
              objetos1.add(ob7)
              objetos1.add(ob8)

              objetos1.add(ob10)
              objetos1.add(ob11)
              objetos1.add(ob12)
              objetos1.add(ob13)
              objetos1.add(ob14)
              objetos1.add(ob15)
              objetos1.add(ob16)
              objetos1.add(ob17)
              objetos1.add(ob18)
              objetos1.add(ob19)
              objetos1.add(ob20)


              #____________________________________________________________________FIN DE MAPA 2



              #MAPA 3___________________________________________________________INICIO MAPA 3
              enemigos3= pygame.sprite.Group()
              objetos2= pygame.sprite.Group()
              #__________________ENEMIGOS
              """enemigo=Enemigo("Ronal",8,200,400,100,100,100,1,100,100,1)
              enemigo1=Enemigo("Reinosa",2,400,400,400,400,250,1,100,100,1)
              enemigo2=Enemigo("Cristian",6,400,500,300,400,200,1,100,100,1)
              enemigo3=Enemigo("Risitas",4,400,600,400,400,150,1,100,100,1)
              enemigo4=Enemigo("Ronal",8,500,300,200,200,100,1,100,100,1)

              enemigos3.add(enemigo)
              enemigos3.add(enemigo1)
              enemigos3.add(enemigo2)
              enemigos3.add(enemigo3)
              enemigos3.add(enemigo4)"""



              #___________________OBJETOS


              ob21= Objetosinvi(0,750,"1000")
              objetos2.add(ob21)

              ob22= Objetosinvi(0,-750,"1000")
              objetos2.add(ob22)

              #____________________________________________________________________FIN DE MAPA 3




              #MAPA 4_______________________________________________________________INICIO MAPA 4
              enemigos4= pygame.sprite.Group()
              objetos4= pygame.sprite.Group()
              #__________________ENEMIGOS
              #enemigo=Enemigo("ELPODEROSOYPITUDOBOSFINAL",8,500,450,400,400,200,5,1000,100,3)

              #enemigos4.add(enemigo)


              #___________________OBJETOS


              ob23= Objetosinvi(0,700,"1000")


              objetos4.add(ob23)




              #______________________________________________________________________FIN DE MAPA 4


              #MAPA 5___________________________________________________________INICIO MAPA 5
              enemigos5= pygame.sprite.Group()
              objetos5= pygame.sprite.Group()
              #__________________ENEMIGOS
              """enemigo=Enemigo("Ronal",8,200,300,100,100,100,1,100,100,2)
              enemigo1=Enemigo("Reinosa",2,600,300,500,300,250,1,100,100,2)
              enemigo2=Enemigo("Cristian",6,400,400,300,400,200,1,100,100,2)
              enemigo3=Enemigo("Risitas",4,400,500,400,400,150,1,100,100,2)
              enemigo4=Enemigo("Ronal",8,500,200,200,200,100,1,100,100,2)

              enemigos5.add(enemigo)
              enemigos5.add(enemigo1)
              enemigos5.add(enemigo2)
              enemigos5.add(enemigo3)
              enemigos5.add(enemigo4)"""


              #___________________OBJETOS
              #MAPA 5___________________________________________________________Fin MAPA 5






              #MAPA 6___________________________________________________________INICIO MAPA 6
              enemigos6= pygame.sprite.Group()
              objetos6= pygame.sprite.Group()

              #__________________ENEMIGOS
              #enemigo=Enemigo("Feo1",8,200,400,100,100,100,1,100,100,0)
              #enemigo1=Enemigo("Feo2",2,400,400,400,300,250,1,100,100,1)


              #enemigos6.add(enemigo)
              #enemigos6.add(enemigo1)



              #___________________OBJETOS 


              ob22= Objetosinvi(800,0,"1000")
              ob20= Objetosinvi(700,500,"1000")
              ob19= Objetosinvi(0,700,"1000")
              objetos6.add(ob19)
              objetos6.add(ob22)
              objetos6.add(ob20)

              #____________________________________________________________________FIN DE MAPA 6


              #MAPA 6___________________________________________________________INICIO MAPA 7
              enemigos7= pygame.sprite.Group()
              objetos7= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("sol",8,200,400,100,100,100,1,100,100,2)
              enemigo1=Enemigo("luna",2,400,400,400,300,250,1,100,100,2)

              enemigos7.add(enemigo)
              enemigos7.add(enemigo1)"""



              #___________________OBJETOS 

              ob19= Objetosinvi(740,-300,"1000")
              ob20= Objetosinvi(1000,400,"1000")
              objetos7.add(ob19)
              objetos7.add(ob20)

              #____________________________________________________________________FIN DE MAPA 7


              #MAPA 8___________________________________________________________INICIO MAPA 8
              enemigos8= pygame.sprite.Group()
              objetos8= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("nose",8,200,400,100,100,100,1,100,100,0)
              enemigo1=Enemigo("nose2",2,400,400,400,300,250,1,100,100,0)

              enemigos8.add(enemigo)
              enemigos8.add(enemigo1)"""



              #___________________OBJETOS 

              ob1= Objetosinvi(400,-650,"1000")
              ob3= Objetosinvi(0,-680,"1000")
              ob2= Objetosinvi(740,0,"1000")
              objetos8.add(ob1)
              objetos8.add(ob2)
              objetos8.add(ob3)




              #____________________________________________________________________FIN DE MAPA 8




              #MAPA 9___________________________________________________________INICIO MAPA 9
              enemigos9= pygame.sprite.Group()
              objetos9= pygame.sprite.Group()

              #__________________ENEMIGOS




              #___________________OBJETOS 

              ob1= Objetosinvi(0,700,"1000")
              ob3= Objetosinvi(0,-800,"1000")
              ob2= Objetosinvi(-200,200,"1000")
              objetos9.add(ob1)
              objetos9.add(ob2)
              objetos9.add(ob3)

              #____________________________________________________________________FIN DE MAPA 9


              #MAPA 10___________________________________________________________INICIO MAPA 10
              enemigos10= pygame.sprite.Group()
              objetos10= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("lool",8,200,400,100,100,100,1,100,100,2)
              enemigo1=Enemigo("leel",2,400,400,400,300,250,1,100,100,2)

              enemigos10.add(enemigo)
              enemigos10.add(enemigo1)"""



              #___________________OBJETOS 

              ob1= Objetosinvi(-1000,0,"1000")
              ob3= Objetosinvi(-540,-720,"1000")
              ob2= Objetosinvi(730,-720,"1000")

              objetos10.add(ob2)
              objetos10.add(ob1)
              objetos10.add(ob3)


              #MAPA 11___________________________________________________________INICIO DE MAPA 11


              enemigos11= pygame.sprite.Group()
              objetos11= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("zion",8,200,400,100,100,100,1,100,100,1)
              enemigo1=Enemigo("wid",2,400,400,400,300,250,1,100,100,0)

              enemigos11.add(enemigo)
              enemigos11.add(enemigo1)"""



              #___________________OBJETOS 

              ob1= Objetosinvi(-1000,0,"1000")
              ob2= Objetosinvi(1000,0,"1000")
              ob3= Objetosinvi(-850,550,"1000")
              ob10= Objetosinvi(550,270,"10-10")

              objetos11.add(ob3)
              objetos11.add(ob10)
              objetos11.add(ob2)
              objetos11.add(ob1)


              #____________________________________________________________________FIN DE MAPA 11


              #MAPA 12___________________________________________________________INICIO DE MAPA 12


              enemigos12= pygame.sprite.Group()
              objetos12= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("zion",8,200,400,100,100,100,1,100,100,2)
              enemigo1=Enemigo("wid",2,400,400,400,300,250,1,100,100,2)

              enemigos12.add(enemigo)
              enemigos12.add(enemigo1)"""


              #___________________OBJETOS 

              ob12= Objetosinvi(-1000,0,"1000")
              ob13= Objetosinvi(800,-400,"1000")
              ob14= Objetosinvi(1000,-0,"1000")

              objetos12.add(ob14)
              objetos12.add(ob13)
              objetos12.add(ob12)

              #____________________________________________________________________FIN DE MAPA 12


              #MAPA 13___________________________________________________________INICIO DE MAPA 13


              enemigos13= pygame.sprite.Group()
              objetos13= pygame.sprite.Group()

              #__________________ENEMIGOS


              #___________________OBJETOS 

              ob1= Objetosinvi(-1000,0,"1000")
              ob3= Objetosinvi(0,-720,"1000")
              ob2= Objetosinvi(800,-590,"1000")
              ob4= Objetosinvi(950,0,"1000")

              objetos13.add(ob2)
              objetos13.add(ob1)
              objetos13.add(ob3)
              objetos13.add(ob4)


              #____________________________________________________________________FIN DE MAPA 13



              #MAPA 14___________________________________________________________INICIO DE MAPA 14


              enemigos14= pygame.sprite.Group()
              objetos14= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("z",8,200,400,100,100,100,1,100,100,0)
              enemigo1=Enemigo("w",2,400,400,400,300,250,1,100,100,0)




              enemigos14.add(enemigo)
              enemigos14.add(enemigo1)"""


              #___________________OBJETOS


              ob2= Objetosinvi(-1000,0,"1000")


              objetos14.add(ob2)

              #MAPA 15___________________________________________________________INICIO DE MAPA 15


              enemigos15= pygame.sprite.Group()
              objetos15= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("zzzz",8,200,400,100,100,100,1,100,100,0)
              enemigo1=Enemigo("weri",2,400,400,400,300,250,1,100,100,0)

              enemigos15.add(enemigo)
              enemigos15.add(enemigo1)"""



              #___________________OBJETOS




              ob1= Objetosinvi(-1000,0,"1000")
              ob3= Objetosinvi(0,-750,"1000")
              ob20= Objetosinvi(200,600,"10-10")
              ob21= Objetosinvi(220,600,"10-10")
              ob5= Objetosinvi(900,370,"10-10")

              objetos15.add(ob5)
              objetos15.add(ob20)
              objetos15.add(ob21)
              objetos15.add(ob1)
              objetos15.add(ob3)




              #MAPA 16___________________________________________________________INICIO DE MAPA 16


              enemigos16= pygame.sprite.Group()
              objetos16= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("zion",8,200,400,100,100,100,1,100,100,1)
              enemigo1=Enemigo("xion",2,400,400,400,300,250,1,100,100,1)

              enemigos16.add(enemigo)
              enemigos16.add(enemigo1)"""


              #___________________OBJETOS


              ob5= Objetosinvi(-1000,0,"1000")
              ob6= Objetosinvi(20,390,"10-10")
              ob7= Objetosinvi(800,350,"50-50")
              objetos16.add(ob6)
              objetos16.add(ob5)
              objetos16.add(ob7)



              #MAPA 17_______________________________________________________________INICIO MAPA 17
              enemigos17= pygame.sprite.Group()
              objetos17= pygame.sprite.Group()
              #__________________ENEMIGOS
              """enemigo=Enemigo("LEO",8,500,450,400,400,200,5,1000,100,3)
              enemigo1=Enemigo("LEO HIJO",8,600,350,400,400,200,5,500,100,3)
              enemigo2=Enemigo("ZION",8,300,650,400,400,200,5,500,100,3)

              enemigos17.add(enemigo)
              enemigos17.add(enemigo1)
              enemigos17.add(enemigo2)"""


              #___________________OBJETOS


              ob5= Objetosinvi(-1000,0,"1000")
              ob6= Objetosinvi(0,700,"1000")

              objetos17.add(ob6)
              objetos17.add(ob5)



              #______________________________________________________________________FIN DE MAPA 17




              #MAPA 18___________________________________________________________INICIO MAPA 18
              enemigos18= pygame.sprite.Group()
              objetos18= pygame.sprite.Group()

              #__________________ENEMIGOS
              """enemigo=Enemigo("Ronal",8,200,300,100,100,100,1,100,100,2)
              enemigo1=Enemigo("Reinosa",2,600,300,500,300,250,1,100,100,2)
              enemigo2=Enemigo("Cristian",6,400,400,300,400,200,1,100,100,2)
              enemigo3=Enemigo("Risitas",4,400,500,400,400,150,1,100,100,2)
              enemigo4=Enemigo("Ronal",8,500,200,200,200,100,1,100,100,2)

              enemigos18.add(enemigo)
              enemigos18.add(enemigo1)
              enemigos18.add(enemigo2)
              enemigos18.add(enemigo3)
              enemigos18.add(enemigo4)"""


              #___________________OBJETOS


              ob5= Objetosinvi(-0,-790,"1000")
              ob6= Objetosinvi(0,700,"1000")
              ob7= Objetosinvi(1000,0,"1000")
              objetos18.add(ob7)
              objetos18.add(ob6)
              objetos18.add(ob5)


              #___________________________________________________________Fin MAPA 18


              




              #INTERFAS VIDA MANA NOMBRE
              nombre_vida_mana3= pygame.sprite.Group()
              nombre_vida_mana2= pygame.sprite.Group()
              nombre_vida_mana1= pygame.sprite.Group()
              nombre_vida_mana= pygame.sprite.Group()
              nombre_vida_mana4= pygame.sprite.Group()
              nombre_vida_mana6= pygame.sprite.Group()
              nombre_vida_mana7= pygame.sprite.Group()
              nombre_vida_mana8= pygame.sprite.Group()
              nombre_vida_mana9= pygame.sprite.Group()
              nombre_vida_mana10= pygame.sprite.Group()
              nombre_vida_mana11= pygame.sprite.Group()
              nombre_vida_mana12= pygame.sprite.Group()
              nombre_vida_mana13= pygame.sprite.Group()
              nombre_vida_mana14= pygame.sprite.Group()
              nombre_vida_mana15= pygame.sprite.Group()
              nombre_vida_mana16= pygame.sprite.Group()
              nombre_vida_mana17= pygame.sprite.Group()
              nombre_vida_mana18= pygame.sprite.Group()

              #INICIO MUSICA FONDO
              #pygame.mixer.music.load("musica/2.mp3")
              #pygame.mixer.music.play(-1)
              sumatoria =0
              perdimana =0
      if action == "disconnect":
             number_players=int(json.loads(socket_server.recv()))
             dic=json.loads(socket_server.recv())
             p=players[dic["username"]]
             del players[dic["username"]]
             mapeo.remove(p)
             mapeo.remove(p.interfase())
             nombre_vida_manajugador.remove(p.interfase())
             jugadores.remove(p)  
      if action=="move" or action=="stop" or action=="golpe" or action =="mapeo" or action == "dano" or action=="dead" or action=="transformar":
            number_players=int(json.loads(socket_server.recv()))
            dic=json.loads(socket_server.recv())
            id_player = dic["username"]
            from_server(action,players[id_player],username,dic,fondo)


    if init:
      
      for event in pygame.event.get():
      	
         tecla= pygame.key.get_pressed()
         mouse=pygame.mouse.get_focused()
         if event.type==pygame.QUIT:
           
           terminar = True
           

         #FUNCIONES PERSONAJE PRINCIPAL INICIO 
         if event.type == pygame.KEYDOWN: 
             if event.key == pygame.K_ESCAPE:
               terminar = True
               socket_server.send_multipart(["disconnect",username])
                
             #for i in tecla:
              # sumatoria =sumatoria+i
             if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    leftsigueapretada=True
                    players[username].vx=-speed
                    if count_move == 0:
                        dic={"username":username,"posx":players[username].rect.x,"posy":players[username].rect.y,"direc":players[username].Orientacion,"i":players[username].personaje_Actual,"t":players[username].t,"vx":players[username].vx,"vy":players[username].vy}
                        socket_server.send_multipart(["move",json.dumps(dic,sort_keys=True)])
                        count_move=1
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada=True
                    players[username].vx=speed
                    if count_move == 0:
                        dic={"username":username,"posx":players[username].rect.x,"posy":players[username].rect.y,"direc":players[username].Orientacion,"i":players[username].personaje_Actual,"t":players[username].t,"vx":players[username].vx,"vy":players[username].vy}
                        socket_server.send_multipart(["move",json.dumps(dic,sort_keys=True)])
                        count_move=1
                if event.key== pygame.K_UP:
                    upsigueapretada=True
                    players[username].vy=-speed
                    if count_move == 0:
                        dic={"username":username,"posx":players[username].rect.x,"posy":players[username].rect.y,"direc":players[username].Orientacion,"i":players[username].personaje_Actual,"t":players[username].t,"vx":players[username].vx,"vy":players[username].vy}
                        socket_server.send_multipart(["move",json.dumps(dic,sort_keys=True)])
                        count_move=1
                if event.key == pygame.K_DOWN:
                    downsigueapretada=True
                    players[username].vy=speed
                    if count_move == 0:
                        dic={"username":username,"posx":players[username].rect.x,"posy":players[username].rect.y,"direc":players[username].Orientacion,"i":players[username].personaje_Actual,"t":players[username].t,"vx":players[username].vx,"vy":players[username].vy}
                        socket_server.send_multipart(["move",json.dumps(dic,sort_keys=True)])
                        count_move=1

                if event.key == pygame.K_SPACE :
                    players[username].animacion=True
                    if count_shut==0:
                        dic={"username":username}
                        socket_server.send_multipart(["golpe",json.dumps(dic,sort_keys=True)])
                        count_shut=1
               

                if event.key == pygame.K_z :
                    if(players[username].personaje == players[username].copia and players[username].mana>0): 
                       players[username].transformar()
                       dic={"username":players[username].nombre,"morph":True}
                       socket_server.send_multipart(["transformar",json.dumps(dic,sort_keys=True)]) 
                if event.key == pygame.K_x:
                    if(players[username].personaje!=players[username].copia):
                       players[username].destransformar()
                       dic={"username":players[username].nombre,"morph":False}
                       socket_server.send_multipart(["transformar",json.dumps(dic,sort_keys=True)]) 

                if event.key == pygame.K_m:
                   fondo.Cambiominimapa(-330,0,players[username].fondo)
                   players[username].muestramapa=True 

                if event.key == pygame.K_n:
                   fondo.Cambiomapa(-330,0,players[username].fondo)
                   players[username].muestramapa=False
               
         if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada=False
                    if rightsigueapretada:
                        players[username].vx=speed
                    else:
                        players[username].vx=0 
                        count_move=0
                        dic={"username":username}
                        socket_server.send_multipart(["stop",json.dumps(dic,sort_keys=True)]) 
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada=False
                    if leftsigueapretada:
                        players[username].vx=-speed
                    else:
                        players[username].vx=0 
                        count_move=0
                        dic={"username":username}
                        socket_server.send_multipart(["stop",json.dumps(dic,sort_keys=True)])  
                if event.key== pygame.K_UP:
                    upsigueapretada=False
                    if downsigueapretada:
                        players[username].vy=speed
                    else:
                        players[username].vy=-0 
                        count_move=0
                        dic={"username":username}
                        socket_server.send_multipart(["stop",json.dumps(dic,sort_keys=True)]) 
                if event.key == pygame.K_DOWN:
                    downsigueapretada=False
                    if upsigueapretada:
                        players[username].vy=-speed
                    else:
                        players[username].vy=0 
                        count_move=0
                        dic={"username":username}
                        socket_server.send_multipart(["stop",json.dumps(dic,sort_keys=True)]) 
                if event.key == pygame.K_SPACE :
                    count_shut=0
        
    #FUNCIONES PERSONAJE PRINCIPAL FIN
    #ANIMACIONES PERSONAJE PRINCIPAL INICIO
      players[username].t+=1
      if players[username].t > 9:
        players[username].t=0
      if (players[username].vx,players[username].vy)==(0,0):
        players[username].moving=False
      else:
        players[username].moving=True

      for p in jugadores:
       nombre_vida_manajugador.update(p.interfase())
       mapeo.update(nombre_vida_manajugador)
       if(perdimana>10 and p.gastarmana):
        p.mana-=10
        perdimana=0

       if(p.mana<=0):
        p.destransformar()   

      perdimana+=1     
  #ANIMACIONES PERSONAJE PRINCIPAL FIN     

  #MODIFICADORES DE LOS MAPAS___________________________________________________________________________________________________-

     #MAPA 1 INICIO______________________________________________________MAPA 1 INICIO
      if(fondo.fondo==1):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos,players[username],jugadores,objetos,mapeo,nombre_vida_mana)) 
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos,objetos,mapeo,nombre_vida_mana)

  #MAPA 2 _________________________________________________________MAPA 2 INICIO
           
      if(fondo.fondo==2):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos2,players[username],jugadores,objetos1,mapeo,nombre_vida_mana1))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos2,objetos1,mapeo,nombre_vida_mana1)
           
  #MAPA 3 _________________________________________________________MAPA 3 INICIO
    
      if(fondo.fondo==3):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos3,players[username],jugadores,objetos2,mapeo,nombre_vida_mana2))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos3,objetos2,mapeo,nombre_vida_mana2)

  #MAPA 4______________________________________________________INICIO MAPA 4
      if(fondo.fondo==5):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos4,players[username],jugadores,objetos4,mapeo,nombre_vida_mana3))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos4,objetos4,mapeo,nombre_vida_mana3)     

  #MAPA 5______________________________________________________INICIO MAPA 5

      if(fondo.fondo==4):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos5,players[username],jugadores,objetos5,mapeo,nombre_vida_mana4))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos5,objetos5,mapeo,nombre_vida_mana4)
    #INICIO MAPA 6______________________________________________________INICIO MAPA 6

      if(fondo.fondo==6):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos6,players[username],jugadores,objetos6,mapeo,nombre_vida_mana6))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos6,objetos6,mapeo,nombre_vida_mana6)  

#INICIO MAPA 7______________________________________________________INICIO MAPA 7

      if(fondo.fondo==7):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos7,players[username],jugadores,objetos7,mapeo,nombre_vida_mana7))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos7,objetos7,mapeo,nombre_vida_mana7)  


#INICIO MAPA 8______________________________________________________INICIO MAPA 8

      if(fondo.fondo==8):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos8,players[username],jugadores,objetos8,mapeo,nombre_vida_mana8))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos8,objetos8,mapeo,nombre_vida_mana8)  


#INICIO MAPA 9______________________________________________________INICIO MAPA 9

      if(fondo.fondo==9):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos9,players[username],jugadores,objetos9,mapeo,nombre_vida_mana9))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos9,objetos9,mapeo,nombre_vida_mana9)  

#INICIO MAPA 10______________________________________________________INICIO MAPA 10

      if(fondo.fondo==10):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos10,players[username],jugadores,objetos10,mapeo,nombre_vida_mana10))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos10,objetos10,mapeo,nombre_vida_mana10)  

#INICIO MAPA 11______________________________________________________INICIO MAPA 11

      if(fondo.fondo==11):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos11,players[username],jugadores,objetos11,mapeo,nombre_vida_mana11))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos11,objetos11,mapeo,nombre_vida_mana11)  

#INICIO MAPA 12______________________________________________________INICIO MAPA 12

      if(fondo.fondo==12):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos12,players[username],jugadores,objetos12,mapeo,nombre_vida_mana12))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos12,objetos12,mapeo,nombre_vida_mana12)  


#INICIO MAPA 13______________________________________________________INICIO MAPA 13

      if(fondo.fondo==13):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos13,players[username],jugadores,objetos13,mapeo,nombre_vida_mana13))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos13,objetos13,mapeo,nombre_vida_mana13)


#INICIO MAPA 14______________________________________________________INICIO MAPA 14

      if(fondo.fondo==14):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos14,players[username],jugadores,objetos14,mapeo,nombre_vida_mana14))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos14,objetos14,mapeo,nombre_vida_mana14)


#INICIO MAPA 15______________________________________________________INICIO MAPA 15

      if(fondo.fondo==15):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos15,players[username],jugadores,objetos15,mapeo,nombre_vida_mana15))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos15,objetos15,mapeo,nombre_vida_mana15)

#INICIO MAPA 16______________________________________________________INICIO MAPA 16

      if(fondo.fondo==16):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos16,players[username],jugadores,objetos16,mapeo,nombre_vida_mana16))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos16,objetos16,mapeo,nombre_vida_mana16)

#INICIO MAPA 17______________________________________________________INICIO MAPA 17

      if(fondo.fondo==17):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos17,players[username],jugadores,objetos17,mapeo,nombre_vida_mana17))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos17,objetos17,mapeo,nombre_vida_mana17)


#INICIO MAPA 18______________________________________________________INICIO MAPA 17

      if(fondo.fondo==18):   
        mapeo=(AnimacionMapas.Goanimacion(socket_server,fondo,players,enemigos18,players[username],jugadores,objetos18,mapeo,nombre_vida_mana18))   
      else: 
        mapeo=AnimacionMapas.KillAnimacion(enemigos18,objetos18,mapeo,nombre_vida_mana18)

      
           
#INICIO MANEJO DE MAPAS _______________________________________________________________
      p=players[username]
      if(p.x>1000 or p.x<0 or p.y<0 or  p.y>0 ):
            if(1==p.fondo and p.y>ALTO):
                
                manejo_mapas(fondo,p,500,0,2,socket_server)
                 

            if(1==p.fondo and p.x>1000):
                
                manejo_mapas(fondo,p,0,p.y,6,socket_server)

            if(6==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,1000,300,1,socket_server)

            if(6==p.fondo and p.y<0):
               
                manejo_mapas(fondo,p,400,680,7,socket_server)

            if(7==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,200,20,6,socket_server)

            if(7==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,200,680,8,socket_server)

            if(7==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,990,300,4,socket_server)

            if(4==p.fondo and p.x>1000):
                
                manejo_mapas(fondo,p,0,300,7,socket_server)

                 

            if(7==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,200,680,8,socket_server)

            if(8==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,200,0,7,socket_server)


            if(8==p.fondo and p.x<0):
               
                manejo_mapas(fondo,p,1000,350,9,socket_server)

            if(9==p.fondo and p.x>1000):
               
                manejo_mapas(fondo,p,0,350,8,socket_server)

            if(9==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,1000,350,10,socket_server)             

            if(10==p.fondo and p.x>1000):
                
                manejo_mapas(fondo,p,0,40,9,socket_server)

            if(10==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,350,0,11,socket_server)


            if(10==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,p.x,680,13,socket_server)

            if(13==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,550,0,10,socket_server)



            if(11==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,350,680,10,socket_server)  


            if(11==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,350,0,12,socket_server)

            if(12==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,350,680,11,socket_server)

            if(12==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,430,0,4,socket_server)  

            if(4==p.fondo and p.y<0):
               
                manejo_mapas(fondo,p,300,680,12,socket_server)

            if(4==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,980,480,15,socket_server)  

            if(15==p.fondo and p.x>980):
                
                manejo_mapas(fondo,p,0,450,4,socket_server)           
     

            if(2==p.fondo and p.y<-20):
                
                manejo_mapas(fondo,p,250,700,1,socket_server)

            if(2==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,140,1000,16,socket_server)

            if(16==p.fondo and p.x>1000):
                
                manejo_mapas(fondo,p,0,350,2,socket_server) 


            if(1==p.fondo and p.x<0):
               
                manejo_mapas(fondo,p,1000,p.y,3,socket_server)

            if(3==p.fondo and p.x>1000):
               
                manejo_mapas(fondo,p,0,320,1,socket_server)

            if(3==p.fondo and p.x<0):
               
                manejo_mapas(fondo,p,980,320,14,socket_server)

            if(14==p.fondo and p.x>1000):
                
                manejo_mapas(fondo,p,0,320,3,socket_server)

            if(14==p.fondo and p.y>700):
               
                manejo_mapas(fondo,p,350,0,16,socket_server)

            if(16==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,350,689,14,socket_server)

            if(16==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,350,0,17,socket_server)

            if(17==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,350,689,16,socket_server)


            if(14==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,500,690,15,socket_server)

            if(15==p.fondo and p.y>700):
                
                manejo_mapas(fondo,p,500,0,14,socket_server)


                 

            if(1==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,p.x,680,4,socket_server)  

            if(4==p.fondo and p.y>700):
               
                manejo_mapas(fondo,p,700,20,1,socket_server)       

            if(2==p.fondo and p.y>700):
               
                manejo_mapas(fondo,p,400,50,5,socket_server) 

            if(5==p.fondo and p.y<0):
                
                manejo_mapas(fondo,p,180,680,2,socket_server)

            if(17==p.fondo and p.x>1000):
                
                manejo_mapas(fondo,p,0,200,5,socket_server)

            if(5==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,990,200,17,socket_server)

            if(5==p.fondo and p.x>1000):
               
                manejo_mapas(fondo,p,0,200,18,socket_server)

            if(18==p.fondo and p.x<0):
                
                manejo_mapas(fondo,p,990,200,5,socket_server) 
                


            for p in players.values():
                if p.fondo != fondo.fondo:
                    mapeo.remove(p)
                    mapeo.remove(p.interfase())
                    nombre_vida_manajugador.remove(p.interfase())
                    jugadores.remove(p)
                if p.fondo== fondo.fondo and not mapeo.has(p):
                    mapeo.add(p)
                    mapeo.add(p.interfase())
                    jugadores.add(p)
                    nombre_vida_manajugador.add(p.interfase())
        


      #FIN MANEJO DE MAPAS _______________________________________________________________

      fondos.draw(PANTALLA)
      mapeo.draw(PANTALLA)
      time.sleep(0.005)
      pygame.display.flip()
  pygame.quit()
    

if __name__=="__main__":
 ALTO= 640
 ANCHO= 1000

 pygame.init()

 PANTALLA= pygame.display.set_mode([ANCHO,ALTO])
 pygame.key.set_repeat(100,10)
 inicio()
