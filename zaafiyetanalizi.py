#! /usr/bin/env python
# encoding=utf-8

import os
os.system("sudo apt-get install figlet")
os.system("clear")
print ("\33[1;31m")
os.system("figlet ZAAFIYET ANALIZI")
print ("""
       \33[1;32mrex - murphyy
nikto zaaafiyet tarama aracı kullanmak için bir kabuk yani 0 dan oluşturulmuş  bir zaaafiyettarama aracı değildir
       bu aracı kullanabilmeniz için sisteminizde nikto kurulu olmalıdır
       """)

hedef = input("\33[1;33mHedefi gir aslanım: ")
os.system("nikto -h" + hedef)