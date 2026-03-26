# CodeAlpha Cybersecurity Internship - Task 1

## Project: Basic Network Sniffer
This is a Python-based network analysis tool developed during my internship at CodeAlpha. The sniffer captures live network traffic and extracts key details like Source/Destination IP addresses, Protocols (TCP, UDP, ICMP), and raw payloads.

### Features:
- Real-time packet sniffing.
- Automatic logging to `captured_packets.log`.
- Clear formatting for protocol analysis.
- Cross-platform support (Kali Linux & Windows).

### Repository Contents:
- **sniffer.py**: The main Python script for sniffing.
- **OS-Requirement.txt**: Detailed guide for setting up the environment on Windows and Kali.
- **captured_packets.log**: A sample output file.
- **screenshots/**: Visual proof of the tool working on the terminal.

### How to Run:
1. Clone the repository.
2. Refer to `OS-Requirement.txt` to install necessary drivers (like Npcap for Windows).
3. Run the script with administrative privileges:
   - **Kali:** `sudo python3 sniffer.py`
   - **Windows:** `python sniffer.py` (Run as Admin)

---
**Developed by:** Muhammad Tauqeer Ul Hassan
**Student ID:** BCS241100
**University:** Capital University of Science and Technology (CUST)
