import ipaddress
import socket
import json
from datetime import datetime
listDict = []

ipRes =  ipaddress.IPv4Interface(input("IP du RÉSEAU privé (192.168.2.0/24): "))
if ipRes.is_private != True:
    input("Il faut une addresse privée !")
    exit()

RangePort = input("Entrez le range de ports à analyser sous le format suivant (20-25) : ")
ExplodedPorts = str(RangePort).split("-")
LowerPort = int(ExplodedPorts[0])
UpperPort = int(ExplodedPorts[1])

#Ip qu'il faut check
toutes_les_addresses = list(ipRes.network.hosts())
indexLowPort = LowerPort

for addresse in toutes_les_addresses:
    listPorts = []
    addresseSTR = str(addresse)
    for i in range(LowerPort, UpperPort+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp
        s.settimeout(0.5)
        try:
            s.connect((addresseSTR, i))
            listPorts.append(i)
        except:
            pass
    #Insert dans json listport
    print(addresseSTR)
    if listPorts:
        dictTemp = {
        "IpAdress": addresseSTR,
        "PortsOuverts": listPorts
        }
        listDict.append(dictTemp) 
jsonDict = json.dumps(listDict, indent=4)   
maintenant = datetime.now()
annee = maintenant.year
mois = maintenant.month
jour = maintenant.day 
with open(f'C:\\python\\{annee}-{mois}-{jour}.json', 'w') as FichierJSON:
    FichierJSON.write(jsonDict)
    
