import flet as ft
from goal import Goal


class App(ft.UserControl):
    def build(self):
        self.settings_visible = False
        self.list_complete_goals_value = {}
        self.list_goals_value = {}
        self.main_pr_text = ft.Text("0 %", weight=ft.FontWeight.W_600, width=70,
                                    text_align=ft.TextAlign.END)
        self.main_pr = ft.ProgressBar(value=0, width=400, color=ft.colors.DEEP_PURPLE_200, bgcolor=ft.colors.WHITE)
        self.goals = ft.GridView(height=530, width=415, child_aspect_ratio=0.8, spacing=10, padding=5, max_extent=260,)

        return ft.Column(
            [
                ft.Row(
                    [
                        self.main_pr_text,
                        self.main_pr,
                        ft.IconButton(icon=ft.icons.SETTINGS, on_click=self.settings_clicked, width=30, height=30,
                                      icon_size=14, ),
                        ft.IconButton(icon=ft.icons.NOTE_ADD, on_click=self.add_clicked, width=30, height=30,
                                      icon_size=14, ),
                    ],
                    width=600,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
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
            else:
                self.settings_visible = True
                self.goals.controls[i].edit_btn.visible = True
                self.goals.controls[i].remove_btn.visible = True
            self.goals.controls[i].update()

    def add_clicked(self, e):
        goal = Goal("Программирование", ft.icons.COMPUTER, 4,
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
