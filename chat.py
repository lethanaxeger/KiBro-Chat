import flet as ft
import c_socket as cs
import threading
import socket

# Class for declerate Message
class Message:
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

# Class for chat message element
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = "start"
        self.controls = [
            # Avatar
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            # Username
            ft.Column(
                [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
        ]
        
        

    #For catch username inisials
    def get_initials(self, user_name: str):
        return user_name[:1].capitalize() if user_name else "U"

    #Set thhe bgcolor of avatar
    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER, ft.colors.BLUE, ft.colors.BROWN, ft.colors.CYAN,
            ft.colors.GREEN, ft.colors.INDIGO, ft.colors.LIME, ft.colors.ORANGE,
            ft.colors.PINK, ft.colors.PURPLE, ft.colors.RED, ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

# Logic in chat page
def chat_page(page):
    page.horizontal_alignment = "stretch"
    page.title = "Flet Chat"
    page.clean()

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False

            # Create socket for client
            cs.client_socket
            # Connect to server section here
            cs.client_socket.connect
            
            # Start a thread to receive messages from the server
            receive_thread = threading.Thread(target=on_message)
            receive_thread.start()

            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(Message(user_name=join_user_name.value, text=f"{join_user_name.value} has joined the chat.", message_type="login_message"))
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(Message(page.session.get("user_name"), new_message.value, message_type="chat_message"))
            new_message.value = ""
            new_message.focus()
            page.update()

            # Sending message to server at this section
            while True:
                pesan = new_message.value
                cs.client_socket.send(pesan.encode())

    def on_message(message: Message):
        if message.message_type == "chat_message":
            # message = cs.client_socket.recv(1024).decode()
            # # print(message) #For debungging purposes
            # # If an error occurs, close the client socket
            # cs.client_socket.close()
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # For login (username) purpose
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_chat_click)],
        actions_alignment="end",
    )

    # Chat list
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # Format for incoming new chat
    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Page layout
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
            # Background
            image_src="/images/kibronewwwww.png",
            bgcolor=ft.colors.BLUE_GREY_600,
            # opacity=0.5,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )
    
# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
#client_socket.connect(('127.0.0.1', 5555)) //Localhost IP
client_socket.connect((cs.IP, 5555))