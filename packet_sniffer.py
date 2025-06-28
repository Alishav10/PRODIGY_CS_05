from scapy.all import sniff

# Callback function to process each packet
def process_packet(packet):
    print(f"\n Packet Captured:")
    print(f" - Protocol: {packet.summary()}")
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f" - Source IP: {ip_layer.src}")
        print(f" - Destination IP: {ip_layer.dst}")
    else:
        print(" - Non-IP packet")

# Start sniffing packets (requires sudo/admin on some systems)
print(" Starting packet sniffer... Press CTRL+C to stop.")
sniff(prn=process_packet, count=10)  # capture 10 packets
