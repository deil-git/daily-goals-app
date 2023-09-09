import time

import flet as ft


class Goal(ft.UserControl):
    def __init__(self, goal_name, goal_icon, goal_value, goal_delete, update_main_pr, settings_visible):
        super().__init__()
        self.settings_visible = settings_visible
        self.update_main_pr = update_main_pr
        self.goal_delete = goal_delete
        self.completed = False
        self.goal_name = goal_name
        self.goal_icon = goal_icon
        self.goal_value = goal_value
        self.goal_complete_value = 0
        self.counter = 0
        self.goal_count = ft.Text(
            f'{self.counter}/{self.goal_value}',
            weight=ft.FontWeight.W_600,
            text_align=ft.TextAlign.CENTER,
            animate_opacity=300,
            width=30
        )
        self.edit_btn = ft.IconButton(
            # TODO : Доделать
            ft.icons.EDIT,
            on_click=self.delete_clicked,
            icon_size=25,
            bgcolor=ft.colors.BLACK,
            icon_color=ft.colors.GREEN_600,
            visible=settings_visible,
            height=100,
        )
        self.remove_btn = ft.IconButton(
            ft.icons.DELETE,
            on_click=self.delete_clicked,
            icon_size=25,
            bgcolor=ft.colors.BLACK,
            icon_color=ft.colors.RED_600,
            visible=settings_visible,
            height=100,
        )
        self.plus_btn = ft.IconButton(
            ft.icons.ADD,
            on_click=self.plus_click,
            width=40,
        )
        self.minus_btn = ft.IconButton(
            ft.icons.REMOVE,
            on_click=self.minus_click,
            width=40,
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
            tooltip='Делай',
            color=ft.colors.DEEP_PURPLE_200
        )
        self.progress_ring_background = ft.ProgressRing(
            width=100,
            height=100,
            stroke_width=15,
            color=ft.colors.WHITE,
            value=1.0,
            visible=not settings_visible,
        )
        self.progress_ring = ft.ProgressRing(
            width=100,
            height=100,
            stroke_width=15,
            color=ft.colors.DEEP_PURPLE_200,
            value=0.0,
            visible=not settings_visible,
        )
        self.goal_text = ft.Text(
            goal_name,
            size=15,
            weight=ft.FontWeight.W_600,
            text_align=ft.TextAlign.CENTER,
            animate_opacity=300,
        )
        self.pl_b = ft.AnimatedSwitcher(
            self.plus_btn,
            animate_opacity=300,
        )
        self.mn_b = ft.AnimatedSwitcher(
            self.minus_btn,
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
            ft.Stack(
                [
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
                                    ft.Row(
                                        [
                                            self.edit_btn,
                                            self.remove_btn,
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=60,
                                    ),
                                ],
                            ),
                            ft.Row(
                                [
                                    self.mn_b,
                                    self.goal_count,
                                    self.pl_b,
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                            ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                ]
            ),
            bgcolor=ft.colors.BLACK,
            width=200,
            height=260,
            border_radius=30,
        )

    def plus_click(self, e):
        if self.counter == self.goal_value:
            return
        self.goal_complete_value += 1
        self.update_main_pr(self)
        self.counter += 1
        self.goal_count.value = f'{self.counter}/{self.goal_value}'
        temp_pr_value = round(1.0 / self.goal_value, 2)
        for i in range(30):
            self.progress_ring.value += temp_pr_value / 29.9
            time.sleep(0.01)
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
            self.mn_b.opacity = 0.0
            self.goal_count.opacity = 0.0
        self.update()

    def minus_click(self, e):
        if self.counter == 0:
            return
        self.goal_complete_value -= 1
        self.update_main_pr(self)
        self.counter -= 1
        self.goal_count.value = f'{self.counter}/{self.goal_value}'
        temp_pr_value = round(1.0 / self.goal_value, 2)
        for i in range(30):
            self.progress_ring.value -= temp_pr_value / 29.9
            time.sleep(0.01)
            self.update()

    def delete_clicked(self, e):
        self.goal_delete(self)
