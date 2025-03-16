
import flet as ft

def main(page: ft.Page):

    # aletrando fundo da pagina
    page.bgcolor = 'green' # alterando a cor d fundo d pagina com um variavel
    page.bgcolor = '#B12B12' # alterando a cor d fundo d pagina com um variavel
    page.bgcolor = ft.Colors.BLUE # alterando a cor d fundo padrao
    
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
    page.window.always_on_top= True # sempre no topo, sobrepondo
    page.window.title_bar_hidden = False # titulo da janela oculto
    page.window_frameless = True # sem bordas
    page.window.fullscreen = False # tela cheia
    page.window.height = 300 # altura da janela
    page.window.max_height = 900 # altura maxima da janela
    page.window.min_height = 200 # altura minima da janela
    page.window.width = 600 # largura da janela
    page.window.max_witdh = 900 # largura maxima da janela
    page.window.min_width = 200 # largura minima da janela
    page.window.resizable = True # inredimensionavel, nao pode puxar com o mouse os cantos da tela
    page.window.top = 100 # margem superior
    page.window.left = 100 # margem esquerda
    page.window_movable = False # movel
    page.window_prvent_close = True # previne fechamento
    page.window_progress_bar = 0.5 # barra de progresso
    print(page.platform) # mostra a plataforma


    # evento de redimensionamento e tamanho da fonte
    #Precisa habilitar  page.window.resizable = True
    def page_resize(e):
        print('Tamanho', page.window_witdh, page.window_height)

    page.on_resize = page_resize

    def page_event(e):
        match e.data:
            case 'moved':
                print('Moveu a janela')
            case 'resized':
                print('Redimensionou a janela')
            case 'minimize':
                print('Minimizou')
            case _:
                print('Outra ação')

    page.on_window_event = page_event


    # alinhamento
    page.add(
        ft.Text(value='Sou Programador FullStack'),
        ft.Container(ft.Text(value='Sou programador FullStack'), bgcolor='AMBER')
    )
    
    page.update() # parametro update, fica vazio mas renderiza a pagina de forma automatica

ft.app(target = main)
