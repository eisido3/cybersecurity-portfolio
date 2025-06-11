#  Threat Assessment Report
**Incident Title:** Outbound Beaconing to Suspicious External IP  
**Date:** June 1, 2025  
**Analyst:** Evan Isidoro

---

## Summary

On June 1, 2025, the SOC detected multiple outbound connections from internal host `HR-LAPTOP-12` to the external IP address `185.220.101.25`. This IP is known to be associated with the Tor network and previously observed in command-and-control (C2) infrastructure.

The pattern of connection attempts — occurring every 5 minutes over port 443 — indicates potential beaconing behavior, commonly used in malware post-compromise communication.

---

## Observations

- **Host Involved:** `SUSPICIOUS-LAPTOP-12`
- **User Account:** `jsmith`
- **External IP:** `185.220.101.25` (listed in abuse.ch and AlienVault OTX)
- **Protocol/Port:** HTTPS (TCP/443)
- **Frequency:** Regular intervals (5-minute gaps)
- **Timeline:** Initial alert at 08:12 CST, recurring until isolation at 10:17 CST

---

##  Risk Analysis

| Factor              | Notes                                           |
|---------------------|------------------------------------------------|
| **Impact**          | High — system has access to HR systems and PII |
| **Likelihood**      | Medium to High — persistent connection attempts |
| **TTPs**            | MITRE ATT&CK T1071.001 – Application Layer Protocol: Web Protocols |

This pattern of traffic suggests an active C2 channel or beaconing from a compromised system.

---

## Recommendations

1. **Isolate the host** from the network for forensic investigation.
2. **Collect volatile memory and disk images** for deep analysis.
3. **Reset credentials** for user `jsmith` and any related admin accounts.
4. **Search for lateral movement** or similar behavior from other endpoints.
5. **Update detection rules** to flag repetitive outbound connections to suspicious IPs.

---

##  Notes

- No phishing emails or credential harvesting activity was detected leading up to the alert — the vector is currently unknown.
- Endpoint antivirus did not trigger during the observed activity — further investigation needed.

---

## References

- [MITRE ATT&CK: T1071.001](https://attack.mitre.org/techniques/T1071/001/)
- [Abuse.ch Threat Intelligence](https://abuse.ch/)
- [AlienVault OTX Lookup](https://otx.alienvault.com/)

---

*This assessment demonstrates my ability to identify, analyze, and document real-world attack patterns using structured threat intelligence methodology.*
