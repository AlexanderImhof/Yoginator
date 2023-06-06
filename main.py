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


    AppBar1 = ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), center_title=True, leading_width=40, title=ft.Text("sign in or sign up"), bgcolor=ft.colors.TEAL_ACCENT_700,
                        actions=[
                                ft.PopupMenuButton(items=[
                                ft.PopupMenuItem(text="help", on_click=open_manual()),
                                ft.PopupMenuItem(text="website", on_click=website()),
                                ft.PopupMenuItem(text="quit", on_click=quit())
                                                ]
                                )
                        ]
    )

    AppBar2 = ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), center_title=True, leading_width=40,
                        title=ft.Text("Main menu"), bgcolor=ft.colors.TEAL_ACCENT_700,
                        actions=[
                            ft.PopupMenuButton(items=[
                                ft.PopupMenuItem(text="help", on_click=open_manual()),
                                ft.PopupMenuItem(text="website", on_click=website()),
                                ft.PopupMenuItem(text="log_out", on_click=lambda _:page.go("/"))
                            ]
                            )
                        ]
                        )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(route='/', controls=[
                                    AppBar1,
                                    ft.Column(controls=[
                                                        ft.Text(),
                                                        ft.TextField(label="username", border_radius=10, content_padding=20 , width=400, autofocus=True, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                                                        ft.TextField(label="password", border_radius=10, content_padding=20 , width= 400, bgcolor=ft.colors.TEAL_100, focused_bgcolor=ft.colors.TEAL_ACCENT_400),
                                                        ft.FilledTonalButton(text="Sign in", icon=ft.icons.LOGIN, on_click=lambda _:page.go("/main menu")),
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


        if page.route == "/main menu":
            page.views.append(
                ft.View(route="/main menu", controls=[
                                                AppBar2,
                                                ft.ElevatedButton(text="perform catalysis",width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                                    style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                                    tooltip="perform a classical catalysis with catalyst, substrate, solvent, additives and a good portion of luck ;)",
                                                    on_click=lambda _: page.go("/")),
                                                ft.ElevatedButton(text="reprocessing catalysis", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                                    style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                                    tooltip="reprocess a previously performed catalysis. Begins after (manual) filtration.",
                                                    on_click=lambda _: page.go("/pc1")),
                                                ft.ElevatedButton(text="serial dilution", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                                    style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                                    tooltip="serial dilution",
                                                    on_click=lambda _: page.go("/rc1")),
                                                ft.ElevatedButton(text="standard", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                                    style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                                    tooltip="preparing a standard solution of one substrate in one solvent",
                                                    on_click=lambda _: page.go("/s1")),
                                                ft.ElevatedButton(text="calibration curve", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                                    style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                                    tooltip="preparing a several samples with different concentration one substrate in one solvent",
                                                    on_click=lambda _: page.go("/cc1")),
                                                ft.ElevatedButton(text="flush", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                                    style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                                    tooltip="flushing the equipment in contact with liquids",
                                                    on_click=lambda _: page.go("/f1")),
                                                ],
                                                vertical_alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
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
