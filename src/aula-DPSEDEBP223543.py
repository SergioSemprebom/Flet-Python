import flet as ft

def main(page: ft.Page):
    mensage = ft.Text(value='Sou DEV em o Nome de JESUS!')
    page.add(mensage)
ft.app(target  = main)