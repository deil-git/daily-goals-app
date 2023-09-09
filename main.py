import flet as ft
from app import App


def main(page: ft.Page):
    page.title = "Daily goals"
    page.padding = 10
    page.window_width = 600
    page.window_height = 630
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    app = App()

    page.add(
        app
    )


ft.app(target=main, view=ft.FLET_APP)
