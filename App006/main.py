import flet as ft
#se importa la libreria random
import random

def main(page: ft.Page):
#se crean las variables globales
    global numero_secreto,entrada_numero,text_resultado,boton_adivinar
    
    page.title="Adivina el numero"
    #se genera un numero aleatorio entre 1 y 100
    numero_secreto= random.randint(1,100)
    
    #se genera la interfaz grafica
    titulo=ft.Text("Adivina el numero",size=25,color="white")
    entrada_numero=ft.TextField(label="Tu adivinanza entre 1 y 100",width=300)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    text_resultado=ft.Text("",color="white")
    #se crea el contenedor de la interfaz grafica
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                text_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=300
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    page.add(contenedor_principal)
ft.app(main)
