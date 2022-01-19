import numpy as np
from collections import *

fichier=open("C:/Users/MFR LE VILLAGE/Documents/Sae15.txt", "r")
text=fichier.readlines()
nblines = len(text)
ipsr=''
ipde=''
flag=''

for ligne in text:
    if not ligne.startswith('\t'):
        tabl=ligne.split(" ")
        long=len(tabl)
        #print(tabl)
        for i in range(long):
            if tabl[2].startswith('ns') or tabl[4].startswith('ns') or 'OK' in tabl[long-1] or 'HTTP' in tabl[long-1]:
                break
            else:
                ipsr=ipsr+tabl[2][0:21]+';'
                ipde=ipde+tabl[4][0:21]+';'
                if tabl[5]=='Flags':
                    flag=flag+tabl[6]+';'
                else:
                    flag=flag+'none;'
                break
        
                
                
fichier.close()

fichier=open("C:/Users/MFR LE VILLAGE/Documents/Sae1.csv", "w")
fichier.write("Liste ip sources :;"+ipsr+"\nListe ip destination"+ipde+"\nListe des flags :;"+flag)
fichier.close()
"""
print (ipde,"\n",ipsr,"\n",longueur, "\n",flag,"\n",list_ip,"\n",nb_ip,"\n")"""