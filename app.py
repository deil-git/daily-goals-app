import flet as ft
from goal import Goal


class App(ft.UserControl):
    def build(self):
        self.list_complete_goals_value = {}
        self.list_goals_value = {}
        self.main_pr_value = ft.Text("0 %", weight=ft.FontWeight.W_600, width=70,
                                     text_align=ft.TextAlign.END)
        self.main_pr = ft.ProgressBar(value=0, width=400, color=ft.colors.DEEP_PURPLE_200, bgcolor=ft.colors.WHITE)
        self.goals = ft.Row(wrap=True)

        return ft.Column(
            [
                ft.Row(
                    [
                        self.main_pr_value,
                        self.main_pr,
                        ft.IconButton(icon=ft.icons.SETTINGS, on_click=self.add_clicked, width=30, height=30,
                                      icon_size=15,),
                        ft.IconButton(icon=ft.icons.ADD, on_click=self.add_clicked, width=30, height=30,
                                      icon_size=15,),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Container(
                    self.goals,
                    width=415,
                    alignment=ft.alignment.center,
                )
            ],
            width=600,
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def add_clicked(self, e):
        goal = Goal("Программирование", ft.icons.COMPUTER, 4,
                    self.goal_delete, self.update_main_pr)
        self.goals.controls.append(goal)
        self.list_goals_value[goal] = goal.goal_value
        temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
        self.main_pr.value = temp / 100
        self.main_pr_value.value = f"{temp} %"
        self.update()

    def goal_delete(self, goal):
        self.goals.controls.remove(goal)
        self.list_goals_value.pop(goal)
        self.list_complete_goals_value.pop(goal)
        temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
        self.main_pr.value = temp / 100
        self.main_pr_value.value = f"{temp} %"
        self.update()

    def update_main_pr(self, goal):
        self.list_complete_goals_value[goal] = goal.goal_complete_value
        temp = int(round((sum(self.list_complete_goals_value.values()) / sum(self.list_goals_value.values())), 2) * 100)
        self.main_pr.value = temp / 100
        self.main_pr_value.value = f"{temp} %"
        self.update()
