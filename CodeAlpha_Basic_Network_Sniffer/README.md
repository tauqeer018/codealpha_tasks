# 🔍 Basic Network Sniffer
### CodeAlpha Cybersecurity Internship - Task 1

![Python](https://img.shields.io/badge/Language-Python-yellow)
![Tool](https://img.shields.io/badge/Tool-Scapy-green)
![OS](https://img.shields.io/badge/OS-Kali%20%7C%20Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

This is a **Python-based network analysis tool** developed during my internship at **CodeAlpha**. The sniffer captures live network traffic and extracts key details such as Source/Destination IP addresses, Protocols (TCP, UDP, ICMP), and raw payloads.

---

## 🚀 Key Features

* **⏱️ Real-time Packet Sniffing:** Monitors and captures network data as it moves across the interface.
* **📂 Automatic Logging:** All captured packets are formatted and saved to `captured_packets.log` for offline analysis.
* **🧠 Protocol Analysis:** Provides clear formatting to identify TCP, UDP, and ICMP protocols instantly.
* **💻 Cross-Platform Support:** Fully compatible and tested on both **Kali Linux** (VirtualBox) and **Windows 11**.

---

## 📁 Repository Contents

| File | Description |
| :--- | :--- |
| 🐍 **sniffer.py** | The main Python script used for capturing and analyzing packets. |
| 📋 **OS-Requirement.txt** | Detailed guide for setting up environments (Npcap for Windows, etc.). |
| 📝 **captured_packets.log** | A sample output file containing captured network data. |
| 📸 **screenshots/** | Visual proof of the tool executing in the terminal. |

---

## 🛠️ How to Run

1.  **Clone:** Clone this repository to your local machine.
2.  **Setup:** Refer to `OS-Requirement.txt` to install necessary drivers (like **Npcap** for Windows).
3.  **Execute:** Run the script with administrative privileges:
    * **Kali Linux:** `sudo python3 sniffer.py`
    * **Windows:** `python sniffer.py` (Run as Administrator)

---

## 👤 About the Author

**Muhammad Tauqeer Ul Hassan**  
**Student ID:** `BCS241100`  
**University:** Capital University of Science and Technology (CUST)  
**Role:** Cybersecurity Intern at CodeAlpha

---
*Disclaimer: This tool is intended for educational purposes and ethical use only.*
