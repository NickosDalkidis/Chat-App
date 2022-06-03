from http import client
from os import name
from threading import Thread

import clients as clients


def handle_client(args):
    pass


def accept_incoming_connections(SERVER=None, addresses=None):
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave!"+
                          "Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client, BUFSIZ=None):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")


welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
client.send(bytes(welcome, "utf8"))
msg = "%s has joined the chat!" % name


def broadcast(param):
    pass


broadcast(bytes(msg, "utf8"))
clients[client] = name


class Mpampis:
    pass


while True:
    msg = client.recv(Mpampis)
    if msg != bytes("{quit}", "utf8"):
        broadcast(msg, name + ": ")
    else:
        client.send(bytes("{quit}", "utf8"))
        client.close()
        del clients[client]
        broadcast(bytes("%s has left the chat." % name, "utf8"))
        break