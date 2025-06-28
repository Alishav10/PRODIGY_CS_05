# PRODIGY_CS_05
A simple Python-based packet sniffer that captures live network traffic and logs protocol, source, and destination IPs

This project is part of the **Prodigy InfoTech Cybersecurity Internship**.

## Objective

To build a simple **Python-based packet sniffer** that captures live network traffic and prints basic details like **protocol, source IP, and destination IP**.

This tool helps you understand how data flows across networks and is commonly used in **network analysis** and **ethical hacking** for monitoring or debugging purposes.

##  What It Does

- Captures **live data packets** from your system's network interface
- Identifies whether it's an **IP-based packet**
- Extracts:
  - Protocol summary
  - Source IP address
  - Destination IP address
- Prints this information to the terminal
- Stops after capturing **10 packets**

> This project uses **Scapy**, a powerful Python library for network packet analysis and manipulation.


##  How It Shows Output

Once you run the script, the terminal displays output like:
-Protocol:
-Source IP:
-Destination IP: 
