import time

import flet as ft


def main(page: ft.Page):
    page.title = "Daily goals"

    def animate(e):
        pr.content = progress_ring1 if pr.content == progress_ring2 else progress_ring2
        pr.update()

    def plus_click(e):
        progress_ring1.value += 1.0 / 4
        progress_ring2.value += 1.0 / 4
        if progress_ring1.value >= 1.0:
            progress_ring_background.value = 0.0
            progress_ring1.value = 1.0
            page.update()
            time.sleep(0.3)
            pr.scale = 0.5
            pr.transition = ft.AnimatedSwitcherTransition.SCALE
            page.update()
            pr.content = done_icon
            pr.scale = 1.0
            pl_b.opacity = 0.0
        else:
            animate(e)
        page.update()

    progress_ring1 = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=15,
        color=ft.colors.DEEP_PURPLE_200
    )

    progress_ring2 = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=15,
        color=ft.colors.DEEP_PURPLE_200
    )

    progress_ring_background = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=15,
        color=ft.colors.WHITE
    )

    done_icon = ft.Icon(
        ft.icons.STAR_ROUNDED,
        size=100,
        tooltip='Молодец 🎉',
        color=ft.colors.DEEP_PURPLE_200
    )

    plus_btn = ft.IconButton(
        ft.icons.ADD,
        on_click=plus_click
    )

    pr = ft.AnimatedSwitcher(
        progress_ring1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=700,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
    )

    pl_b = ft.AnimatedSwitcher(
        plus_btn,
        animate_opacity=300,
    )

    page.add(
        ft.Column(
            [
                ft.Text("Коля круче всех!", style="headlineSmall"),
                ft.Stack(
                    [
                        progress_ring_background,
                        pr,
                    ]
                ),
                pl_b,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
    )

    progress_ring1.value = 0.0
    progress_ring2.value = 0.0
    progress_ring_background.value = 1.0
    page.padding = 0
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()


ft.app(target=main)  # Вывести в десктопе
#ft.app(target=main, view=ft.WEB_BROWSER)  # Вывести в вебе
