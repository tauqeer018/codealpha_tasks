from scapy.all import sniff, IP, TCP, UDP, Raw
import sys

# File ka naam jahan data save hoga
LOG_FILE = "captured_packets.log"
def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        protocol_name = "Other"
        if proto == 6: protocol_name = "TCP"
        elif proto == 17: protocol_name = "UDP"
        elif proto == 1: protocol_name = "ICMP"
        # Formatting for the file 
        output = (
            f"\n" + "="*50 +
            f"\n[+] SOURCE IP      : {src_ip}"
            f"\n[+] DESTINATION IP : {dst_ip}"
            f"\n[+] PROTOCOL       : {protocol_name}"
        )
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            output += f"\n[*] PAYLOAD        : {payload}"
        output += f"\n" + "="*50 + "\n"
        # Terminal par display nahi hoga, sirf file mein save hoga [cite: 51]
        with open(LOG_FILE, "a") as f:
            f.write(output)
def main():
    print("--- CodeAlpha Basic Network Sniffer ---")
    print(f"[*] Saving captured info in: {LOG_FILE}")
    print("[*] Terminal output is HIDDEN. Monitoring traffic... [cite: 24, 42]")
    print("[*] Press Ctrl+C to stop and save the tool session.")
    try:
        # Packet capturing start [cite: 23, 25]
        sniff(iface="lo", prn=process_packet, store=0, lfilter=lambda pkt: pkt.haslayer(Raw))
    except KeyboardInterrupt:
        print(f"\n[!] Sniffer stopped. All packets have been saved to {LOG_FILE}")
        sys.exit()
if __name__ == "__main__":
    main()
