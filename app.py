import random

import flet as ft
from goal import Goal


class App(ft.UserControl):
    def build(self):
        self.settings_visible = False
        self.list_complete_goals_value = {}
        self.list_goals_value = {}
        self.main_pr_text = ft.Text("0 %", weight=ft.FontWeight.W_600, width=70,
                                    text_align=ft.TextAlign.CENTER)
        self.main_pr = ft.ProgressBar(value=0, width=400, color=ft.colors.WHITE)
        self.goals = ft.GridView(height=530, width=415, child_aspect_ratio=0.8, spacing=10, padding=5, max_extent=260,)
        self.red = ft.Radio(value=ft.colors.RED_500, fill_color=ft.colors.RED_500, scale=1.2)
        self.green = ft.Radio(value=ft.colors.GREEN_500, fill_color=ft.colors.GREEN_500, scale=1.2)
        self.blue = ft.Radio(value=ft.colors.BLUE_500, fill_color=ft.colors.BLUE_500, scale=1.2)
        self.yellow = ft.Radio(value=ft.colors.YELLOW_500, fill_color=ft.colors.YELLOW_500, scale=1.2)
        self.purple = ft.Radio(value=ft.colors.DEEP_PURPLE_400, fill_color=ft.colors.DEEP_PURPLE_400, scale=1.2)
        self.grey = ft.Radio(value=ft.colors.BLUE_GREY_400, fill_color=ft.colors.BLUE_GREY_400, scale=1.2)
        self.pink = ft.Radio(value=ft.colors.PINK_400, fill_color=ft.colors.PINK_400, scale=1.2)
        self.cyan = ft.Radio(value=ft.colors.CYAN_300, fill_color=ft.colors.CYAN_300, scale=1.2)
        self.orange = ft.Radio(value=ft.colors.DEEP_ORANGE_400, fill_color=ft.colors.DEEP_ORANGE_400, scale=1.2)
        self.color_list = [self.red.value, self.green.value, self.blue.value,
                    self.yellow.value, self.purple.value, self.grey.value,
                    self.pink.value, self.cyan.value, self.orange.value]
        self.text_hint_list = ["Супер цель", "Прикол", "АААААААА"]
        self.color_radio_btn = ft.RadioGroup(
            content=ft.Row(
                [
                    self.red, self.green, self.blue,
                    self.yellow, self.purple, self.grey,
                    self.pink, self.cyan, self.orange,
                ],
                wrap=True,
                spacing=10,
                width=120,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        self.icon_user = ft.IconButton(icon=ft.icons.QUESTION_MARK)
        self.name_from_user = ft.TextField(hint_text=random.choice(self.text_hint_list), width=220)
        self.counter_from_user = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=100, read_only=True)
        self.counter_mn_btn = ft.IconButton(
                            ft.icons.REMOVE,
                            on_click=self.counter_minus,
                            disabled=True,
                            width=40,
                        )
        self.counter_pl_btn = ft.IconButton(
                            ft.icons.ADD,
                            on_click=self.counter_plus,
                            width=40,
                        )
        self.comb_for_dialog = ft.Column(
            [
                ft.Container(width=1, height=2),
                ft.Text("Иконка и название", opacity=0.7),
                ft.Row(
                    [
                        self.icon_user,
                        self.name_from_user,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(width=1, height=10),
                ft.Text("Цвет цели", opacity=0.7),
                self.color_radio_btn,
                ft.Container(width=1, height=10),
                ft.Text("Число повторений", opacity=0.7),
                ft.Row(
                    [
                        self.counter_mn_btn,
                        self.counter_from_user,
                        self.counter_pl_btn,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            height=390,
            width=300,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.create_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Настройте цель", text_align=ft.TextAlign.CENTER),
        content=self.comb_for_dialog,
        actions=[
            ft.TextButton("Добавить", icon=ft.icons.CHECK_CIRCLE_ROUNDED, on_click=self.create_close_dlg, icon_color=ft.colors.GREEN_500),
            ft.Container(height=1, width=15),
            ft.TextButton("Отменить", icon=ft.icons.CANCEL_ROUNDED, on_click=self.close_dlg, icon_color=ft.colors.RED_500),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Диалог закрыт!"),
        )

        return ft.Column(
            [
                ft.Column(
                    [
                        self.main_pr_text,
                        self.main_pr,
                        ft.Row(
                            [
                                ft.IconButton(icon=ft.icons.STAR_ROUNDED, on_click=self.open_dlg_modal,
                                              width=30, height=30, icon_size=15, ),
                                ft.IconButton(icon=ft.icons.SETTINGS, on_click=self.settings_clicked,
                                              width=30, height=30, icon_size=14, ),
                                ft.IconButton(icon=ft.icons.NOTE_ADD, on_click=self.add_clicked,
                                              width=30, height=30, icon_size=14, ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    width=600,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                self.goals
            ],
            width=600,
            height=630,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def settings_clicked(self, e):
        for i in range(len(self.goals.controls)):
            if self.goals.controls[i].edit_btn.visible:
                self.settings_visible = False
                self.goals.controls[i].edit_btn.visible = False
                self.goals.controls[i].remove_btn.visible = False
                self.goals.controls[i].progress_ring_background.visible = True
                self.goals.controls[i].progress_ring.visible = True
            else:
                self.settings_visible = True
                self.goals.controls[i].edit_btn.visible = True
                self.goals.controls[i].remove_btn.visible = True
                self.goals.controls[i].progress_ring_background.visible = False
                self.goals.controls[i].progress_ring.visible = False
            self.goals.controls[i].update()

    def add_clicked(self, e):
        goal = Goal("Программирование", ft.icons.COMPUTER, 4, ft.colors.RED_500,
                    self.goal_delete, self.update_main_pr, self.settings_visible)
        self.goals.controls.append(goal)
        self.list_goals_value[goal] = goal.goal_value
        self.list_complete_goals_value[goal] = 0
        temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
        self.main_pr.value = temp / 100
        self.main_pr_text.value = f"{temp} %"
        self.update()

    def goal_delete(self, goal):
        self.list_goals_value.pop(goal)
        self.list_complete_goals_value.pop(goal)
        self.goals.controls.remove(goal)
        if sum(self.list_goals_value.values()) != 0:
            temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
            self.main_pr.value = temp / 100
            self.main_pr_text.value = f"{temp} %"
        else:
            self.main_pr_text.value = f"0 %"
            self.main_pr.value = 0
        self.update()

    def update_main_pr(self, goal):
        self.list_complete_goals_value[goal] = goal.goal_complete_value
        temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
        self.main_pr.value = temp / 100
        self.main_pr_text.value = f"{temp} %"
        self.update()

    def open_dlg_modal(self, e):
        self.page.dialog = self.create_dialog
        self.create_dialog.open = True
        self.color_radio_btn.value = random.choice(self.color_list)
        self.name_from_user.hint_text = random.choice(self.text_hint_list)
        self.page.update()

    def create_close_dlg(self, e):
        if self.name_from_user.value == '':
            self.name_from_user.value = self.name_from_user.hint_text
        goal = Goal(self.name_from_user.value, ft.icons.COMPUTER, int(self.counter_from_user.value),
                    self.color_radio_btn.value, self.goal_delete, self.update_main_pr, self.settings_visible)
        self.goals.controls.append(goal)
        self.list_goals_value[goal] = goal.goal_value
        self.list_complete_goals_value[goal] = 0
        temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
        self.main_pr.value = temp / 100
        self.main_pr_text.value = f"{temp} %"
        self.update()
        self.create_dialog.open = False
        self.name_from_user.value = ''
        self.counter_from_user.value = str(1)
        self.page.update()

    def close_dlg(self, e):
        self.create_dialog.open = False
        self.page.update()

    def counter_minus(self, e):
        if int(self.counter_from_user.value) >= 999:
            self.counter_pl_btn.disabled = False
        self.counter_from_user.value = str(int(self.counter_from_user.value) - 1)
        if int(self.counter_from_user.value) <= 1:
            self.counter_mn_btn.disabled = True
        self.page.update()

    def counter_plus(self, e):
        self.counter_mn_btn.disabled = False
        self.counter_from_user.value = str(int(self.counter_from_user.value) + 1)
        if int(self.counter_from_user.value) >= 999:
            self.counter_pl_btn.disabled = True
        self.page.update()
