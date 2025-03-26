import pyaudio
import socket

#default port
port = 80

#setup server
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created successfully")
    s.bind(("0.0.0.0", port))
    s.listen(1)
    print(f"Server listening on port {port}")

except socket.error as err:
    print("socket creation failed with error as %s", err)


#audio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,output=True)

conn, addr = s.accept()
print(f"Connection from {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        stream.write(data)

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.close()
    server_socket.close()