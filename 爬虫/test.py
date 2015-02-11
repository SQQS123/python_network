#-*-coding:utf-8-*-
import pylink
link = pylink.get_link()
lista = link.get_sourse()
for i in lista:
    link.link(i)


