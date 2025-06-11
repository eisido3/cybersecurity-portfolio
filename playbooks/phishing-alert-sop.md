# Standard Operating Procedure (SOP)
## Phishing Email Alert - Incident Response

**Purpose:**  
To provide a standardized response procedure for suspected phishing emails detected by email security tools or reported by users.

**Scope:**  
SOC Analysts, Tier 1–2 Incident Responders

---

## Step-by-Step Response Workflow

### 1. **Triage**
- Review the initial alert from email gateway, SIEM, or user report.
- Gather details: sender address, subject, delivery timestamp, email headers.

### 2. **Analyze**
- Open the email in a secure sandboxed environment.
- Look for:
  - Suspicious links (hover to preview URL)
  - Malicious attachments (macro-enabled, .scr, .exe, etc.)
  - Spoofed domains or lookalike URLs

### 3. **Check Indicators of Compromise (IOCs)**
- Run:
  - URLs and hashes through [VirusTotal](https://www.virustotal.com/)
  - Sender IPs through WHOIS or abuse databases
  - Domain via passive DNS or reputation tools

### 4. **Contain**
- If confirmed malicious:
  - Quarantine the email across all recipients (via email gateway tool)
  - Block associated domains/IPs via firewall or proxy
  - Disable affected user accounts if compromise suspected

### 5. **Notify**
- Inform IT and Security leadership
- Provide guidance to users who received the email (without clicking)

### 6. **Document**
- Log the event in ticketing system (e.g., Jira, ServiceNow)
- Record:
  - Summary of the phishing attempt
  - IOCs and tool output
  - Steps taken and timeline
  - Any affected users or systems

### 7. **Post-Incident**
- Update internal phishing detection rules if needed
- Share IOCs with threat intel feeds (if part of your org process)
- Run phishing awareness training refresh if applicable

---

## Thoughts

- Never click links or download attachments in suspected phishing emails on a regular workstation.
- Keep evidence (original .eml file, screenshots, logs).
- Always follow the least-privilege principle when responding.

---

*Author: Evan Isidoro*  
*Last Updated: June 2025*

