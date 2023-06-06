import flet as ft

def main(page: ft.page):
    page.title = "Yoginator"
    page.window_center()
    page.update()

    font = str("Arial")
    FS1 = int(24)
    FS2 = int(18)

    bgc1 = ft.colors.TEAL_ACCENT_100 #60
    bgc2 = ft.colors.TEAL_ACCENT_400 #30
    bgc3 = ft.colors.TEAL_ACCENT_700 #10

    def open_manual():
        pass

    def quit():
        pass

    def website():
        pass


    def route_change(route):
        page.views.clear()
        page.views.append( #homepage
            ft.View(route='/', controls=[
                ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), center_title=True, leading_width=40,
                          title=ft.Text("sign in or sign up"), bgcolor=bgc3,
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
                      ft.TextField(label="username", border_radius=10, content_padding=20 , width=400, autofocus=True, bgcolor=bgc2, focused_bgcolor=bgc3),
                      ft.TextField(label="password", border_radius=10, content_padding=20 , width= 400, bgcolor=bgc2, focused_bgcolor=bgc3),
                      ft.ElevatedButton(text="Sign in", icon=ft.icons.LOGIN, bgcolor=bgc3 , on_click=lambda _:page.go("/main menu")),
                      ft.Divider(height=300, thickness=0, color=bgc3),
                      ft.Row(controls=[
                         ft.Text(value="Don't have an account?"),
                         ft.ElevatedButton(text="Sign up", bgcolor=bgc3, icon=ft.icons.HANDSHAKE, on_click=lambda _:page.go("/signup"))
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

        if page.route == "/main menu": #main menu
            page.views.append(
                ft.View(route= "/main menu", controls=[
                    ft.AppBar(leading=ft.Icon(ft.icons.SCIENCE_OUTLINED), center_title=True, leading_width=40,
                              title=ft.Text("Main menu"), bgcolor=bgc3,
                              actions=[
                                  ft.PopupMenuButton(items=[
                                      ft.PopupMenuItem(text="help", on_click=open_manual()),
                                      ft.PopupMenuItem(text="website", on_click=website()),
                                      ft.PopupMenuItem(text="log_out", on_click=lambda _: page.go("/"))
                                  ]
                                  )
                              ]
                    ),
                    ft.ElevatedButton(content=ft.Text(value="perform catalysis", size=18, font_family="Arial", italic=True, weight=ft.FontWeight.BOLD), width=400, height=50, bgcolor=bgc2,
                        style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                        tooltip="perform a classical catalysis with catalyst, substrate, solvent, additives and a good portion of luck ;)",
                        on_click=lambda _: page.go("/c1")),
                    ft.ElevatedButton(content=ft.Text(value="reprocessing catalysis", size=18, font_family="Arial", italic=True, weight=ft.FontWeight.BOLD), width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                        style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                        tooltip="reprocess a previously performed catalysis. Begins after (manual) filtration.",
                        on_click=lambda _: page.go("/pc1")),
                    ft.ElevatedButton(content=ft.Text(value="serial dilution", size=18, font_family="Arial", italic=True, weight=ft.FontWeight.BOLD), width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                        style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                        tooltip="serial dilution",
                        on_click=lambda _: page.go("/rc1")),
                    ft.ElevatedButton(content=ft.Text(value="standard", size=18, font_family="Arial", italic=True, weight=ft.FontWeight.BOLD), width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                        style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                        tooltip="preparing a standard solution of one substrate in one solvent",
                        on_click=lambda _: page.go("/s1")),
                    ft.ElevatedButton(content=ft.Text(value="calibration curve", size=18, font_family="Arial", italic=True, weight=ft.FontWeight.BOLD), width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                        style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                        tooltip="preparing a several samples with different concentration one substrate in one solvent",
                        on_click=lambda _: page.go("/cc1")),
                    ft.ElevatedButton(content=ft.Text(value="flush", size=18, font_family="Arial", italic=True, weight=ft.FontWeight.BOLD), width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                        style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400, ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                        tooltip="flushing the equipment in contact with liquids",
                        on_click=lambda _: page.go("/f1")),
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )


        if page.route == "/c1": #catalysis 1
            page.views.append(
                ft.View(route="/c1", controls=[
                       ft.ElevatedButton(text="flush", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                      tooltip="flushing the equipment in contact with liquids",
                                      on_click=lambda _: page.go("/f1")
                                      ),
                                    ],
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
            )

        if page.route == "/pc1": #processing catalysis 1
            page.views.append(
                ft.View(route="/pc1", controls=[
                    ft.ElevatedButton(text="perform catalysis", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                      tooltip="perform a classical catalysis with catalyst, substrate, solvent, additives and a good portion of luck ;)",
                                      on_click=lambda _: page.go("/")),
                    ft.ElevatedButton(text="reprocessing catalysis", width=400, height=50,
                                      bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                      tooltip="reprocess a previously performed catalysis. Begins after (manual) filtration.",
                                      on_click=lambda _: page.go("/pc1")),
                    ft.ElevatedButton(text="serial dilution", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                      tooltip="serial dilution",
                                      on_click=lambda _: page.go("/rc1")),
                    ft.ElevatedButton(text="standard", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                      tooltip="preparing a standard solution of one substrate in one solvent",
                                      on_click=lambda _: page.go("/s1")),
                    ft.ElevatedButton(text="calibration curve", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
                                      tooltip="preparing a several samples with different concentration one substrate in one solvent",
                                      on_click=lambda _: page.go("/cc1")),
                    ft.ElevatedButton(text="flush", width=400, height=50, bgcolor=ft.colors.TEAL_ACCENT_700,
                                      style=ft.ButtonStyle(color={ft.MaterialState.HOVERED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.FOCUSED: ft.colors.TEAL_ACCENT_400,
                                                                  ft.MaterialState.DEFAULT: ft.colors.TEAL_ACCENT_100}),
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
