
import flet as ft

def main(page: ft.Page):

    # aletrando fundo da pagina
    page.bgcolor = 'green' # alterando a cor d fundo d pagina com um variavel
    page.bgcolor = '#B12B12' # alterando a cor d fundo d pagina com um variavel
    page.bgcolor = ft.Colors.WHITE # alterando a cor d fundo padrao
    
    #Formas de alinhamento na horizontal o de texto
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH # alinhamento horizontal    
    #page.horizontal_alignmet = ft.CrossAxisAlignment.CENTER # alinhamento central
    
    #Formas de alinhamento na vertical o de texto
    page.vertical_alignment = ft.MainAxisAlignment.START  # alinhamento vertical

    # Formas de Espaçamento
    #page.padding = ft.padding.all(30) # margem de 10px
    #page.padding = ft.padding.symmetric(vertical=100, horizontal=10)
    #page.padding = ft.padding.only(top=20, left=10, right=100, bottom=50) # será usado no curso
    page.padding = 20
    page.spacing = 100
    page.title = 'Page App' # titulo da Pagina
    page.window_always_on_top = True # sempre no topo
    page.window_title_bar = True # barra de titulo

    # alinhamento
    page.add(
        ft.Text(value='Sou Programador FullStack'),
        ft.Container(ft.Text(value='Sou programador FullStack'), bgcolor='AMBER')
    )
    
    page.update() # parametro update, fica vazio mas renderiza a pagina de forma automatica

ft.app(target = main)
