

import flet as ft

def main (page :ft.Page):
    page.fonts = {
        'Kanit': 'https://raw.githubusercontent.com/google/fonts/main/ofl/kanit/Kanit-Regular.ttf',
    }


    t1 = ft.Text(
        value = "Olá Mundo, seja ben vindo ao Flet",
        style = ft.TextThemeStyle.DISPLAY_LARGE,
        bcdolor = ft.colors.WHITE,
        color = ft.colors.BLACK,
        font_family = 'Kanit',
    )

    page.add(t1)

    page.update()
ft.app(target = main)