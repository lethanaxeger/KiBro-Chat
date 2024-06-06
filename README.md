# KiBro-Chat

Me and my friend made this web-based application for Final Practice in my university. So while learning how to use flet Framework I decided to commit it in my github.. it isn't a bad idea, hm?

## What does this do?
KiBro or 'Kita Ngobrol' is a web-based chatting platform using flet framework. It only sending a text message only. It's just basic websocket program that run in flet Framework with enchance UI develop.

## Why not using HTML and CSS?
We already try to using it and we decide to search something more simple than complicated by making 3 different extensions code. It makes way easier and faster than developing using HTML and CSS with python for the back-end programm.

## How to use this?
This program works in python enviroment using flet as Framework. It's pretty easy and you can develop it whenever you want by adding some extras to make it super-chat-web-app. This program runs at client side but need to run the server first. Don't worry, it will run by change a bit in server.py and c_socket.py

### If the python isn't installed
- Installing the python
  > https://www.python.org/downloads/release/
- or you're in linux based OS
  > $ sudo apt-get install python3.8

- Installing flet framework
  > pip install -U flet
- or you're in linux based OS
  > $ sudo pip install -U flet

### Now, you're ready to use this code. All you need to do is:
- Cloning this repository
  > git clone https://github.com/lethanaxeger/Kibro-Chat
  
- Change your directory to Kibro-Chat (Change the [path] following where the Kibro-Chat is saved)
  > cd [path]\Kibro-Chat
  
- Change the port in server.py and c_socket.py (Both must same, otherwise it won't connected otherwise)
  > ![port_c_socket](https://github.com/lethanaxeger/KiBro-Chat/assets/53499521/8144fe33-3a06-4839-9931-a8b47e84a516)
  
- Run the server.py first
  > py .\server.py
  
- Run the main.py
  > py .\main.py

Voila!, KiBro is running in your web. You can access it in any devices. Just add the same IP and PORT from your local device.
  
### If you're using python instead py, just change it to python
  > python [example]
