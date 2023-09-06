import flet as ft
from goal import Goal


class App(ft.UserControl):
    def build(self):
        self.goals = ft.Column()

        return ft.Column(
            controls=[
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                self.goals
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def add_clicked(self, e):
        goal = Goal("Программирование", ft.icons.COMPUTER, 4, self.goal_delete)
        self.goals.controls.append(goal)
        self.update()

    def goal_delete(self, goal):
        self.goals.controls.remove(goal)
        self.update()
