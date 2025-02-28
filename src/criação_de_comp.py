import flet as ft


def main(page: ft.Page):
    t1 = ft.Text(
        value='Olá seja bem vindo ao GED, Gestão Eletonica de Documentação', # Criando um texto
        style = ft.TextThemeStyle.DISPLAY_LARGE, # Formatando o estilo do Texto
        bgcolor = ft.colors.AMBER # Fundo das letras
    )
    page.add(t1) # Obrigatorio para um texto
ft.app(target=main) # Obirgatorio