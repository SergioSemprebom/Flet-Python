import flet as ft



def main(page: ft.Page):
    #page.bgcolor='green'
    #page.bgcolor='#FFFFFF'
    page.bgcolor= ft.colors.GREEN

    mensagem = ft.Text(value='olá Ged')
    page.add(mensagem)

    page.add(ft.Text(value='Construindo Gestão Eletronica Documental;'))

    page.add(ft.Text(value='Pensamentos bons que elevam a alegria no SENHOR.'))

    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.padding = 20
    page.spacing = 20
    page.title = 'Flet App'
    page.window_always_on_top = True
    page.window_title_bar_buttons_hidden = True
    page.windows_frameless = False
    page.windows_full_screen = True

    
    

    page.add(

        ft.Text(value='Estamos inovando!'),
        ft.Container(ft.Text(value='Todos os resultados são positivos!'), bgcolor='white'),
        ft.Container(ft.Text(value='Todos os resultados são Metadados!'), bgcolor='white'),
    )

    Cliente=[
        ft.Text(value='AMOR'),
        ft.Text(value='PAZ'),
        ft.Text(value='ALEGRIA'),

    ]
    page.add(*Cliente)

    page.update()
ft.app(target = main)
