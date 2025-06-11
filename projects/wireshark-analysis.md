# Wireshark Network Traffic Analysis
**Project:** Network Forensics and Intrusion Detection  
**Tool Used:** Wireshark  
**Date:** January 2023 – Present  
**Author:** Evan Isidoro

---

## Objective

To analyze captured network traffic for signs of suspicious or malicious behavior, gain deeper insight into TCP/IP communication, and practice manual packet inspection as part of SOC and blue team skill development.

---

## Lab Setup

- Captured traffic using Wireshark from a test machine simulating normal and abnormal user behavior.
- Network activity included DNS queries, HTTP/HTTPS browsing, ICMP pings, and simulated C2 traffic using a test payload.
- Examined `.pcap` files from TryHackMe and self-generated lab environments.

---

## 🔍 Key Analysis Focus

### TCP Three-Way Handshake
- Verified proper initiation and termination of TCP connections.
- Identified unusual SYN flood behavior in one session, suggesting scanning activity.

### DNS Query Inspection
- Spotted repeated DNS queries to misspelled domains (e.g., `micros0ft-update.com`) suggesting a phishing C2 callback attempt.
- Cross-referenced domain reputation via VirusTotal and RiskIQ.

### HTTP Traffic Review
- Observed data exfiltration via HTTP POST request to an IP in a suspicious ASN (Autonomous System Number).
- Flagged base64-encoded data in HTTP payload, indicative of covert data transmission.

### ICMP Abuse
- Detected large and irregular ICMP Echo Requests, possibly being used for exfiltration or host discovery in a lateral movement scenario.

---

## Takeaways

- Learned to differentiate between normal vs. suspicious packet patterns.
- Practiced interpreting packet payloads and metadata without relying on automated alerts.
- Gained a deeper appreciation for how subtle and stealthy some attacks can appear when viewed at the packet level.

---

## References

- MITRE ATT&CK: [T1040 - Network Sniffing](https://attack.mitre.org/techniques/T1040/)
- Wireshark Filter Cheatsheet
- [TryHackMe: Wireshark Room](https://tryhackme.com/room/wireshark)

---

*This analysis exercise helped reinforce my ability to think like an attacker and respond like a defender, focusing on critical thinking and pattern recognition within network traffic.*
