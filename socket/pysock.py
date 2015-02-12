import socket
class new_server():
    def _init_(self):
        pass
    def open_UDP(self,host,port):
        UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        UDP.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return UDP
    def open_TCP(self,host,port):
        TCP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        TCP.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return TCP
        
