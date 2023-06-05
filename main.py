import flet as ft

def main(page: ft.page):
    page.title = "Yoginator"
    page.window_center()
    page.bgcolor = ft.colors.TEAL_100
    #page.vertical_aligment = "center"
    #page.horizontal_aligment = "center"
    page.update()

    page.appbar = ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), leading_width=40, title=ft.Text("sign in or sign up"), bgcolor=ft.colors.TEAL_400,
                            actions=[
                                ft.PopupMenuButton(items=[
                                    ft.PopupMenuItem(text="help"),
                                    ft.PopupMenuItem(), #divider
                                    ft.PopupMenuItem(text="quit")
                                    ]
                                )

                            ]
                            )

    page.add(
        ft.Column(
            controls=[
                ft.TextField(label="username", border_radius=10, content_padding=20 , autofocus=True, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                ft.TextField(label="password", border_radius=10, content_padding=20 , bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                ft.IconButton(ft.icons.LOGIN, icon_color=ft.colors.TEAL_700, bgcolor=ft.colors.TEAL_ACCENT_400),
                ft.Divider(height=300, thickness=0, color=ft.colors.TEAL_700),
                ft.Row(controls=[ft.Text(value="Don't have an account?"), ft.TextButton(text="sign up")], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )




if __name__ == "__main__":
    ft.app(target=main)
