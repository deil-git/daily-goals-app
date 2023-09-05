import time

import flet as ft


class Goal(ft.UserControl):
    def __init__(self, goal_name, goal_icon, goal_value):
        super().__init__()
        self.completed = False
        self.goal_name = goal_name
        self.goal_icon = goal_icon
        self.goal_value = goal_value
        self.plus_btn = ft.IconButton(
            ft.icons.ADD,
            on_click=self.plus_click
        )
        self.done_icon = ft.Icon(
            ft.icons.STAR_ROUNDED,
            size=100,
            tooltip='Молодец 🎉',
            color=ft.colors.DEEP_PURPLE_200,
            scale=0,
        )
        self.goal_icon = ft.Icon(
            goal_icon,
            size=100,
            tooltip='Делай 💻',
            color=ft.colors.DEEP_PURPLE_200
        )
        self.progress_ring_background = ft.ProgressRing(
            width=100,
            height=100,
            stroke_width=15,
            color=ft.colors.WHITE,
            value=1.0
        )
        self.progress_ring = ft.ProgressRing(
            width=100,
            height=100,
            stroke_width=15,
            color=ft.colors.DEEP_PURPLE_200,
            value=0.0,
        )
        self.goal_text = ft.Text(
            goal_name,
            size=16,
            weight=ft.FontWeight.W_600,
            text_align=ft.TextAlign.CENTER,
            animate_opacity=300,
        )
        self.pl_b = ft.AnimatedSwitcher(
            self.plus_btn,
            animate_opacity=300,
        )
        self.pr_icon = ft.AnimatedSwitcher(
            self.goal_icon,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=1,
            switch_in_curve=ft.AnimationCurve.DECELERATE,
            scale=ft.transform.Scale(scale=0.5),
            animate_scale=ft.animation.Animation(1100, ft.AnimationCurve.EASE),
        )

    def build(self):
        return ft.Container(
            ft.Column(
                [
                    ft.Container(
                        self.goal_text,
                        width=160,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Stack(
                        [
                            ft.Container(
                                content=self.progress_ring_background,
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                content=self.progress_ring,
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                content=self.pr_icon,
                                alignment=ft.alignment.center,

                            ),
                        ],
                    ),
                    ft.Container(
                        self.pl_b,
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

    def plus_click(self, e):
        temp_pr_value = round(1.0 / self.goal_value, 2)
        for i in range(15):
            self.progress_ring.value += temp_pr_value / 15
            time.sleep(0.025)
            self.update()
        if self.progress_ring.value >= 1.0:
            time.sleep(0.3)
            self.pr_icon.scale = 0
            self.update()
            self.pr_icon.content = self.done_icon
            self.update()
            time.sleep(0.6)
            self.done_icon.scale = 0.85
            self.pr_icon.scale = 0.85
            self.goal_text.opacity = 0.0
            self.pl_b.opacity = 0.0
        self.update()


def main(page: ft.Page):
    page.title = "Daily goals"
    page.padding = 0
    page.window_width = 700
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    page.add(
        ft.Row(
            # TODO: Row wrapping
            [
                Goal("Программирование", ft.icons.COMPUTER, 4),
                Goal("Рисование", ft.icons.BRUSH, 6)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.app(target=main, view=ft.FLET_APP)
