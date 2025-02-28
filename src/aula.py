import flet as ft

def main(page: ft.Page):
    mensage = ft.Text(value='Olá seja bem vindo ao GED, Gestão Eletronica de Documentação')
    page.add(mensage)

    
ft.app(target  = main)