import ipaddress
import math
import json



listDict = []
toSubstract = 0

nbHosts = int(input("Nombre de hosts (Entre 2 et 65534): "))

if (nbHosts < 2 or nbHosts > 65534):
    print("Veuillez entrer un nombre de hosts valide !")
nbHosts+=2

ipAddr =  ipaddress.IPv4Interface(input("IP du RÉSEAU de départ (192.168.2.0/24): "))
if ipAddr.is_private != True:
    input("Il faut une addresse privée !")
    exit()
   

ExplodedIP = str(ipAddr.network).split("/")
prefixInit = int(ExplodedIP[1])

nextPrefix = 32

for i in range(33):
    if (math.pow(2, i) == nbHosts):
        toSubstract = i
        break
    elif (nbHosts >= math.pow(2, (i-1)) and nbHosts <= math.pow(2, i)):
        toSubstract = i
        break

nbHosts = 2**i

    

newPrefix = nextPrefix - toSubstract
liste_sousreseaux = list(ipaddress.ip_network(ipAddr).subnets(new_prefix=newPrefix))

for sr in liste_sousreseaux:
    #print(f"Adresse du sous réseau : {sr}")
    #print(f"Nombre de hosts : {nbHosts}")
    toutes_les_addresses = list(sr.hosts())
    #print(f"1ère adresse du réseau : {toutes_les_addresses[0]}")
    #print(f"Dernière adresse du réseau : {toutes_les_addresses[-1]}")
    #print(f"Adresse de broadcast : {sr.broadcast_address}")
    #print(15 * "-")
    dictTemp = {
        "Reseau": str(sr),
        "premiere": str(toutes_les_addresses[0]),
        "derniere": str(toutes_les_addresses[-1]),
        "broadcast": str(sr.broadcast_address),
        "nbr": nbHosts-2
    }
    listDict.append(dictTemp) 
jsonDict = json.dumps(listDict, indent=4)

with open(f'C:\\python\\{ExplodedIP[0]}--{prefixInit}--{newPrefix}.json', 'w') as FichierJSON:
    FichierJSON.write(jsonDict)

