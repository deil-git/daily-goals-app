import flet as ft
from app import App


def main(page: ft.Page):
    page.title = "Daily goals"
    page.padding = 0
    page.window_width = 700
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    app = App()

    page.add(
        ft.Row(
            # TODO: Row wrapping
            [
                app
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.app(target=main, view=ft.FLET_APP)
