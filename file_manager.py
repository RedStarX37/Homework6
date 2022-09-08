import sys
import socket


def view_os_info():
  print(sys.platform)


def view_creator():
    print(socket.gethostname())


view_creator()
view_os_info()