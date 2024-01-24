#Se um computador tiver a placa de rede com a função WakeOnLan habilitada, conseguimos ligar o computador remotamente através da rede se ele estiver hibernado ou suspenso.

import socket
import binascii

def send_wol(mac_address):
    # Cria um pacote WoL
    wol_packet = b'FF' * 6 + (binascii.unhexlify(mac_address.replace(':', ''))) * 16

    # Envia o pacote para o endereço de broadcast na porta 9
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(wol_packet, ('<broadcast>', 9))

# Use a função com o endereço MAC do computador de destino
send_wol('00:11:22:33:44:55')

