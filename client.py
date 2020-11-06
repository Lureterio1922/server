import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.0.144",7932))

sock.sendall(b"Idy spat,spat pora")



data = sock.recv(1024).decode("utf-8")
print(f"Message'{data}'" )

sock.close()