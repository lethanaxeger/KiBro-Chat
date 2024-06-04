# KiBro-Chat
!- This is log of progress of develop this app. If there's any suggestion, please leave some. I would appreciate it. -!

Juny, 03 2024
- Update main.py
  > change the 'from flet import *' to 'import flet as ft' for more functional and stable
  > change all the flet element's by adding ft.

- Fix bug at main.py at logo
  > at src variable f is undenified make the code cannot run. By deleting it, the code works perfectly fine

- Separating chat function from main.py to new chat.py
  > For develop purposes
  > Makes easy to bugging than make it in one file

Juny, 04 2024
- Adding server.py and c_socket.py
  > Making a manual socket for LAN connection
  > Code can be accessible at least in LAN

- Integrating the server.py and c_socket.py with main.py and chat.py
  > Adding socket library in main.py and chat.py
  > Import c_socket.py to chat.py and main.py for client connection
  > Add client_socket and client_connect in chat.py at def on_message():
  > Add host=cs.IP in main.py at ft.app()

- Fix bug at chat.py
  > Deleting pesan = cs.client_socket.recv().decode() at on_message instead only printing ChatMessage(message)

- Adding transparent logo for container chat
  > Adding the transparent logo at chat.py in ft.container
