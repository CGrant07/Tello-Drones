# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nCarson Grant")
print("Program Name: Square")
print("Date: 2.6.2024")
print("Drone WIFI = DD7E")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 6)
        sendmsg("battery?")
        sendmsg('takeoff')
        """
        # Square - Pilot = Bryson LaMew - CoPilot - Carson Grant
        sendmsg('up 100', 6)
        sendmsg('forward 60', 6)
        sendmsg('cw 90', 6)
        sendmsg('forward 60', 6)
        sendmsg('cw 90', 6)
        sendmsg('forward 60', 6)
        sendmsg('cw 90', 6)
        sendmsg('forward 60', 6)
        """
        # Triangle - Pilot = Carson Grant - CoPilot = Bryson LaMew
        """
        sendmsg('up 100', 6)
        sendmsg('forward 60', 6)
        sendmsg('cw 135', 6)
        sendmsg('forward 60', 6)
        sendmsg('cw 135', 6)
        sendmsg('forward 60', 6)
        """
        # Circle - Pilot = Bryson Lamew - CoPilot = Carson Grant
        sendmsg('curve 100 100 0 100 0 0 50')
        sendmsg('curve -100 -100 0 -100 0 0 50')


        sendmsg('land')

        print('\nGreat Flight!!!')

else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')



breakr = True
sock.close()