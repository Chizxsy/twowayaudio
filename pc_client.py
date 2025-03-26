import pyaudio
import socket

#default port
port = 80

#setup server
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created successfully")
    s.connect(("raspiip", port))

except socket.error as err:
    print("socket creation failed with error as %s", err)

#audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,output=True)

try:
    while True:
        data = stream.read(1024)
        s.sendall(data)
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    s.close()
