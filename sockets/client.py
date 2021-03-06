import socket

HEADER = 8
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '10.0.0.222'
ADDR = (SERVER, PORT)

# setting up socket for client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# connect to server, instead of bind
client.connect(ADDR)

# ------- tested here-----------
'''
1 invalid literal for int() with base 10 error 
meaning something was recieved by the sever that was not able to convert 
to an int

Solution: an if clause within server's handle_client() method, 
where messages would only be recieved as long as they are not None

Solution worked
connection successful and active when run
'''
#-----------------------------------


# method for sending messages to server
def send(msg):
    #message needs to be encoded into a byte format to be sent to server
    #or perhaps to travel through a TCP connection?
    message = msg.encode(FORMAT)
    msg_length = len(message)

    # the length of message is converted to a string and encoded in utf-8 format
    send_length = str(msg_length).encode(FORMAT)

    #pad to make it a length of 8 bytes
    # so subtract 8 bytes by the length of the message to find whitespace length 
    # b' ' is the byte representation of the calculated length ( whitespace)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Bop!")

send(DISCONNECT_MESSAGE)
