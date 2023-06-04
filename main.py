import flet as ft


def main(page: ft.page):
    page.title = "Yoginator"
    page.window_center()
    page.bgcolor = ft.colors.TEAL_100
    page.update()

    username = ft.TextField(label="username", autofocus=True, )
    password = ft.TextField(label="password")
    signin = ft.ElevatedButton(text="sign in", icon=f"IconLogIn.png", icon_color="#3776A1")
    divider = ft.Divider(height=1, thickness=1, color=ft.colors.TEAL_700)
    signup = ft.ElevatedButton(text="sign up", icon="IconLogIn", icon_color="#3776A1")

    page.add(ft.Column(controls=[username, password, signin, divider, signup], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER,width=500, height=20))

if __name__ == "__main__":
    ft.app(target=main)
