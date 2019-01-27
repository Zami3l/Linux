#Importation
import os

#Declaration des ports physiques et des bridges
port = ['enp1s0', 'enp2s0']
bridge = ['WAN', 'LAN', 'DMZ', 'LABO1', 'LABO2']

#Fonction : Creation d'un bridge OVS
def new_bridge(bridge):
    cmd = 'ovs-vsctl add-br {}'.format(bridge)
    os.system(cmd)

#Fonction : Ajout d'un port sur un bridge
def add_port(bridge, port):
    cmd = 'ovs-vsctl add-port {} {}'.format(bridge, port)
    os.system(cmd)
    print('Ajout du port <{}> au bridge <{}>'.format(port, bridge))

#Creation des bridges
for index in range(len(bridge)):
    new_bridge(bridge[index])
    print('Creation du bridge <{}>'.format(bridge[index]))

#Ajout des ports sur les bridges
add_port(bridge[0], port[0])
add_port(bridge[1], port[1])

print('Configuration OK')