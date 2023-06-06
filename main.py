import flet as ft

def main(page: ft.page):
    page.title = "Yoginator"
    page.window_center()
    page.bgcolor = ft.colors.TEAL_100
    #page.vertical_aligment = "center"
    #page.horizontal_aligment = "center"
    page.update()

    def open_manual():
        pass

    def quit():
        pass

    def website():
        pass

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(route='/', controls=[
                                    ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), center_title=True, leading_width=40, title=ft.Text("sign in or sign up"), bgcolor=ft.colors.TEAL_400,
                                                actions=[
                                                    ft.PopupMenuButton(items=[
                                                        ft.PopupMenuItem(text="help", on_click=open_manual()),
                                                        ft.PopupMenuItem(text="website", on_click=website()),
                                                        ft.PopupMenuItem(text="quit", on_click=quit())
                                                    ]
                                                    )

                                                ]
                                    ),
                                    ft.Column(controls=[
                                                        ft.Text(),
                                                        ft.TextField(label="username", border_radius=10, content_padding=20 , width=400, autofocus=True, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                                                        ft.TextField(label="password", border_radius=10, content_padding=20 , width= 400, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                                                        ft.FilledTonalButton(text="Sign in", icon=ft.icons.LOGIN, on_click=lambda _:page.go("/store")),
                                                        ft.Divider(height=300, thickness=0, color=ft.colors.TEAL_700),
                                                        ft.Row(controls=[
                                                                        ft.Text(value="Don't have an account?"),
                                                                        ft.FilledTonalButton(text="Sign up", icon=ft.icons.HANDSHAKE)
                                                                        ],
                                                                         alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER)
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        spacing=20)
                                    ]
            )
        )



        if page.route =="/store":
            page.views.append(
                ft.View("/store",
                    [
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/"))
                    ]
                )
            )
    page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)
