from colores import *
import pygame
from datos import lista

ANCHO_VENTANA = 850
ALTO_VENTANA = 600
lista_preguntas = []
lista_opciones_a = []
lista_opciones_b = []
lista_opciones_c = []
lista_temas = []
lista_respuesta = []
puntaje = 0
preguntar = False
contador_preguntas = -1
correcto = False
errores = 0

imagen = pygame.image.load("pygame\carrera_mental\carrera_mental.JPG")
# guardo todos los elementos de la lista original en listas individuales 
for elemento in lista:
    lista_preguntas.append(elemento["pregunta"])
    lista_opciones_a.append(elemento["a"])
    lista_opciones_b.append(elemento["b"])
    lista_opciones_c.append(elemento["c"])
    lista_temas.append(elemento["tema"])
    lista_respuesta.append(elemento["correcta"])


pygame.init()

fuente = pygame.font.SysFont("Arial", 30)
btn_pregunta = fuente.render("PREGUNTA", True, BLACK)
btn_reiniciar = fuente.render("REINICIAR", True, BLACK)
score = fuente.render("SCORE", True, BLACK)
texto_puntaje = fuente.render(str(puntaje), True, BLACK)
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

bandera_correr = True
while bandera_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: 
            bandera_correr = False  
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)
            # apreta el boton pregunta
            if ((posicion_click[0] > 300 and posicion_click[0] < 500) and 
                (posicion_click[1] > 20 and posicion_click[1] < 120)):
                correcto = False
                errores = 0
                # controlar el numero de preguntas
                if contador_preguntas < (len(lista_preguntas)-1):
                    contador_preguntas += 1
                else:
                    contador_preguntas = 0

                pregunta = fuente.render(lista_preguntas[contador_preguntas], True, BLACK)
                opcion_a = fuente.render(lista_opciones_a[contador_preguntas], True, BLACK)
                opcion_b = fuente.render(lista_opciones_b[contador_preguntas], True, BLACK)
                opcion_c = fuente.render(lista_opciones_c[contador_preguntas], True, BLACK)
                tema = fuente.render(lista_temas[contador_preguntas], True, BLACK)

                preguntar = True
            if preguntar == True:
# apreta algunas de las opciones-----------------------------------------------------------------------------
                #opcion a
                if ((posicion_click[0] > 20 and posicion_click[0] < 249) and 
                    (posicion_click[1] > 400 and posicion_click[1] < 460)): 
                    if lista_respuesta[contador_preguntas] == "a" and not correcto:
                        if errores < 2:
                            puntaje += 10
                            texto_puntaje = fuente.render(str(puntaje), True, BLACK)
                            correcto = True
                    else:
                        errores += 1

                #opcion b
                if ((posicion_click[0] > 310 and posicion_click[0] < 543) and 
                    (posicion_click[1] > 400 and posicion_click[1] < 460)): 
                    if lista_respuesta[contador_preguntas] == "b" and not correcto:
                        if errores < 2:
                            puntaje += 10
                            texto_puntaje = fuente.render(str(puntaje), True, BLACK)
                            correcto = True
                    else:
                        errores += 1

                #opcion c
                if ((posicion_click[0] > 600 and posicion_click[0] < 828) and 
                    (posicion_click[1] > 400 and posicion_click[1] < 460)): 
                    if lista_respuesta[contador_preguntas] == "c" and not correcto:
                        if errores < 2:
                            puntaje += 10
                            texto_puntaje = fuente.render(str(puntaje), True, BLACK)
                            correcto = True
                    else:
                        errores += 1

            # preciona el boton reiniciar
            if ((posicion_click[0] > 300 and posicion_click[0] < 500) and 
                (posicion_click[1] > 500 and posicion_click[1] < 580)):
                preguntar = False
                contador_preguntas = -1
                puntaje = 0
                texto_puntaje = fuente.render(str(puntaje), True, BLACK)


    pantalla.fill(VIOLET)
    pygame.draw.rect(pantalla,BLUE,(300,20,200,100))
    pantalla.blit(btn_pregunta,(340,50))
    if preguntar == True:
        pantalla.blit(pregunta,(20,300))
        pantalla.blit(tema,(20,250))

        if correcto == False and errores < 2: 
            pygame.draw.rect(pantalla, BLUE, [20, 400, 230, 60])
            pantalla.blit(opcion_a,(20,400))

            pygame.draw.rect(pantalla, BLUE, [310, 400, 235, 60])
            pantalla.blit(opcion_b,(310,400))

            pygame.draw.rect(pantalla, BLUE, [600, 400, 230, 60])
            pantalla.blit(opcion_c,(600,400))

    pygame.draw.rect(pantalla,BLUE,(300,500,200,80))
    pantalla.blit(btn_reiniciar,(340,520))

    pantalla.blit(score,(340,170))
    pantalla.blit(texto_puntaje,(340,200))

    pantalla.blit(imagen,(10,10),)

    pygame.display.flip()

pygame.quit()