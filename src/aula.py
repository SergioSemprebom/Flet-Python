# Aula inicial básica de Flet utilizando a funcção def main() obrigatório por conversão


import flet as ft

def main(page: ft.Page): # main a função por conversão obrigatoria, (page: ft.Page) parametro principal obrigatorio
    mensage = ft.Text(value='Olá seja bem vindo ao GED, Gestão Eletronica de Documentação')
    page.add(mensage)

    
ft.app(target  = main) # como se fosse o print, e metodo renderiza a minha função