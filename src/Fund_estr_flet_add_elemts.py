import flet as ft

def main(page: ft.Page): # função principal do Flet


    # METODO EM QUE CONSIGO ALTERAR O CODIGO EM QQ PARTE
    mensagen = ft.Text(value='Óla Mundo!') # escrevo uma msg numa variavel
    page.add(mensagen, mensagen) # repito a msg com se estive add um elemento a pagina



    # METODO ESTATICO
    page.add(ft.Text(value='Meu nome é Sergio'))
    page.add(ft.Text(value='Estático 1'), ft.Text(value='Estático 2'))

    elementos = [
        ft.Text(value='varios elementos em uma lista 1'),
        ft.Text(value='varios elementos em uma lista 2'),
        ft.Text(value='varios elementos em uma lista 3'),
        ft.Text(value='varios elementos em uma lista 4'),
        ft.Text(value='varios elementos em uma lista 5'),
    ]
    # condições fora da lista para executar
    page.add(*elementos)

ft.app(target=main)