import flet as ft

def main(page: ft.page):
    t = ft.Text(value="Hallo Benutzer", color="#3776A1")
    page.add(t)

ft.app(target=main)