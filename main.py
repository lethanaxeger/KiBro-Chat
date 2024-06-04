import flet as ft
import chat
import c_socket as cs
    
# Main page section
def main_page(page):
    page.title = "Kita Ngobrol"
    page.bgcolor = ft.colors.LIGHT_BLUE_50
    page.padding = 50

    # Logo (cosmetic)
    logo = ft.Image(
        src="/images/logobaru.png",  # Ganti dengan URL logo Anda
        width=500,
        height=500,
        fit=ft.ImageFit.CONTAIN,
    )

    # Membuat tombol untuk navigasi ke halaman chat
    button1 = ft.ElevatedButton("Yuk Ngobrol....", on_click=lambda e:chat.chat_page(page))
    
    # Menambahkan logo dan tombol ke halaman
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=2),  # Spasi di atas logo untuk menggeser ke atas
                    logo,
                    ft.Container(height=2),  # Spasi antara logo dan tombol
                    ft.Row(
                        [button1],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
        )
    )

ft.app(target=main_page, view=ft.WEB_BROWSER, host=cs.IP, port=5555) #server.port=80 when server.py ready