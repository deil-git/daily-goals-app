import flet as ft


def main(page: ft.Page):
    page.title = "Daily goals"

    def animate(e):
        c.content = progress_ring if c.content == done_icon else done_icon
        c.update()

    def plus_click(e):
        progress_ring.value += 1.0 / 4
        if progress_ring.value >= 1.0:
            c.content = done_icon
            plus_btn.visible = False
        page.update()

    progress_ring = ft.ProgressRing(
        width=64,
        height=64,
        stroke_width=15,
        color=ft.colors.DEEP_PURPLE_100
    )

    c = ft.AnimatedSwitcher(
        progress_ring,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    done_icon = ft.Icon(
        ft.icons.STAR_ROUNDED,
        size=64,
        tooltip='Молодец 🎉',
        color=ft.colors.DEEP_PURPLE_100
    )

    plus_btn = ft.IconButton(
        ft.icons.ADD,
        on_click=plus_click
    )

    page.add(
        ft.Column(
            [
                ft.Text("Коля круче всех!", style="headlineSmall"),
                c,
                plus_btn,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
    )

    page.padding = 0
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    progress_ring.value = 0.0
    page.update()


ft.app(target=main)  # Вывести в десктопе
# ft.app(target=main, view=ft.WEB_BROWSER)  # Вывести в вебе
