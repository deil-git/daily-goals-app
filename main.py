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
            pr_icon.scale = 0
            page.update()
            pr_icon.content = done_icon
            page.update()
            time.sleep(0.6)
            done_icon.scale = 0.85
            pr_icon.scale = 0.85
            goal_text.opacity = 0.0
            pl_b.opacity = 0.0
        else:
            animate(e)
        page.update()

    progress_ring1 = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=15,
        color=ft.colors.DEEP_PURPLE_200,
        value=0.0,
    )

    progress_ring2 = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=15,
        color=ft.colors.DEEP_PURPLE_200,
        value=0.0,
    )

    progress_ring_background = ft.ProgressRing(
        width=100,
        height=100,
        stroke_width=15,
        color=ft.colors.WHITE,
        value=1.0
    )

    goal_icon = ft.Icon(
        ft.icons.COMPUTER,
        size=100,
        tooltip='Делай 💻',
        color=ft.colors.DEEP_PURPLE_200
    )

    done_icon = ft.Icon(
        ft.icons.STAR_ROUNDED,
        size=100,
        tooltip='Молодец 🎉',
        color=ft.colors.DEEP_PURPLE_200,
        scale=0,
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

    pr_icon = ft.AnimatedSwitcher(
        goal_icon,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        scale=ft.transform.Scale(scale=0.5),
        animate_scale=ft.animation.Animation(1100, ft.AnimationCurve.EASE),
    )

    pl_b = ft.AnimatedSwitcher(
        plus_btn,
        animate_opacity=300,
    )

    goal_text = ft.Text(
        "Программирование",
        size=16,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        animate_opacity=300,
    )

    pr_temp = ft.Container(
        ft.Column(
            [
                ft.Container(
                    goal_text,
                    width=160,
                    height=40,
                    alignment=ft.alignment.center,
                ),
                ft.Stack(
                    [
                        ft.Container(
                            content=progress_ring_background,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=pr,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=pr_icon,
                            alignment=ft.alignment.center,

                        ),
                    ],
                ),
                ft.Container(
                    pl_b,
                    width=110,
                    height=40,
                    alignment=ft.alignment.center,
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.colors.BLACK,
        width=200,
        height=260,
        border_radius=30,
    )

    page.add(
        ft.Row(
            # TODO: Row wrapping
            [
                pr_temp,
                pr_temp
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.padding = 0
    page.window_width = 700
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()


ft.app(target=main, view=ft.FLET_APP)
