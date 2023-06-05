import flet as ft

def openManual():
    pass

def quit():
    pass

def website():
    pass

def main(page: ft.page):
    page.title = "Yoginator"
    page.window_center()
    page.bgcolor = ft.colors.TEAL_100
    #page.vertical_aligment = "center"
    #page.horizontal_aligment = "center"
    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(route='/', controls=[ft.Container(height=800, width=350, bgcolor="red")]
            )
        )



    page.on_route_change = route_change
    page.go('/')


    page.appbar = ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), center_title=True, leading_width=40, title=ft.Text("sign in or sign up"), bgcolor=ft.colors.TEAL_400,
                            actions=[
                                ft.PopupMenuButton(items=[
                                    ft.PopupMenuItem(text="help", on_click=openManual()),
                                    ft.PopupMenuItem(text="website", on_click=website()),
                                    ft.PopupMenuItem(text="quit", on_click=quit())
                                    ]
                                )
                            ]
                            )

    page.add(
        ft.Column(
            controls=[
                ft.Text(),
                ft.TextField(label="username", border_radius=10, content_padding=20 , width=400, autofocus=True, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                ft.TextField(label="password", border_radius=10, content_padding=20 , width= 400, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                ft.FilledTonalButton(text="Sign in", icon=ft.icons.LOGIN),
                ft.Divider(height=300, thickness=0, color=ft.colors.TEAL_700),
                ft.Row(controls=[
                    ft.Text(value="Don't have an account?"),
                    ft.FilledTonalButton(text="Sign up", icon=ft.icons.HANDSHAKE)],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            )
    )




if __name__ == "__main__":
    ft.app(target=main)
