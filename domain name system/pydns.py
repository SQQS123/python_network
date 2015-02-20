import socket

class dns():
    def _init_(self):
        pass
    def send(self,second,first,root):
        len_root = '%s'%chr(len(root))
        len_first = '%s'%chr(len(first))
        if second:
            len_second ='%s'%chr(len(second))
            q = b'\x5c\x6d\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00%s%s%s%s%s%s\x00\x00\x01\x00\x01'%(len_second,second,len_first,first,len_root,root)
            print q
        
