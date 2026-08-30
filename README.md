# PySec
 
A lightweight Python network reconnaissance tool. PySec scans a target domain for open ports **concurrently**, grabs service banners, checks them against a local vulnerability database, analyzes HTTP responses, and saves a structured JSON report of the results — built as a hands-on project to learn Python, core networking/security concepts, and concurrency.
 
## Features
 
- **DNS resolution** — resolves a domain name to its IP address before scanning
- **Multithreaded port scanning** — checks all user-specified ports concurrently (one thread per port) instead of one at a time, significantly speeding up scans
- **Thread-safe result collection** — uses a lock to safely combine results from multiple threads without data corruption
- **Service identification** — maps common ports to known services (SSH, HTTP, FTP, DNS, etc.)
- **Banner grabbing** — connects to open ports and reads the service banner, cleanly labeling empty or non-text (binary) responses, tagged by port number so results stay traceable even with concurrent output
- **Vulnerability detection** — checks grabbed banners against a local database of known CVEs (e.g. flags outdated OpenSSH, Apache, and vsftpd versions) and includes any matches directly in the report
- **HTTP analysis** — for open port 80, sends a raw HTTP request and parses the status code, server header, and content type
- **Graceful error handling** — invalid or unresolvable domains produce a clean error message instead of a crash
- **JSON reporting** — saves scan results, including any flagged vulnerabilities, to a `<domain>_scan_report.json` file for later review or use by other tools
## Requirements
 
- Python 3.x
- No external dependencies — uses only Python's built-in `socket`, `threading`, and `json` modules
## How to Run
 
```bash
python main.py
```
 
You'll be prompted for:
1. **A domain** to scan (e.g. `scanme.nmap.org`)
2. **A comma-separated list of ports** to scan (e.g. `22,80,443`)
## Example Output
 
```
======================
   PySec v2.0
Network Security Tool
======================
Enter a Domain: scanme.nmap.org
Enter ports to scan: 22,80
 
======================
Port Scan
======================
[OPEN] 22 (SSH)
[OPEN] 80 (HTTP)
    [22] Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
    [22] ⚠ VULNERABLE: CVE-2015-5600 (Medium) - Keyboard-interactive authentication flaw allows attackers to bypass MaxAuthTries via multiple ChallengeResponseAuthentication devices, enabling brute-force attacks.
 
Port scan complete.
 
======================
HTTP Analysis
======================
HTTP Information
----------------
Status: HTTP/1.1 200 OK
Server: Apache/2.4.7 (Ubuntu)
Content-Type: text/html
Meaning: Request successful
 
Report saved to scanme.nmap.org_scan_report.json
```
 
Note: because ports are scanned concurrently, output for different ports may appear interleaved rather than in the order they were entered — this is expected and is a sign the threads are running in parallel. Each banner and vulnerability line is tagged with its port number so results remain traceable.
 
The saved JSON report includes both port status and any flagged vulnerabilities:
```json
[
    {
        "port": 22,
        "status": "open",
        "service": "SSH"
    },
    {
        "port": 22,
        "type": "vulnerability",
        "cve": "CVE-2015-5600",
        "severity": "Medium",
        "description": "Keyboard-interactive authentication flaw allows attackers to bypass MaxAuthTries via multiple ChallengeResponseAuthentication devices, enabling brute-force attacks."
    }
]
```
 
## Project Structure
 
| File | Purpose |
|---|---|
| `main.py` | Entry point — handles user input and ties everything together |
| `banner.py` | Displays the tool's startup banner |
| `dns_lookup.py` | Resolves a domain name to an IP address |
| `scanner.py` | Core multithreaded port scanning logic and service identification |
| `banner_grabber.py` | Connects to open ports, reads service banners, and checks them for known vulnerabilities |
| `vuln_db.py` | Local database of known CVEs matched against banner version strings |
| `http_client.py` | Sends a raw HTTP request and parses the response |
| `report.py` | Saves scan results, including vulnerabilities, to a JSON report file |
| `utils.py` | Shared helper functions (e.g. banner classification) |
 
## Vulnerability Detection
 
This tool uses a small, local, hardcoded database of known CVEs (in `vuln_db.py`) matched against banner version strings — it does **not** query any live CVE database or external API. It's intended as a learning exercise in basic vulnerability matching, not a comprehensive or up-to-date vulnerability scanner. For real-world vulnerability assessment, use established tools and live CVE feeds.
 
## Disclaimer
 
This tool is intended for educational purposes and for scanning systems you own or have explicit permission to test — such as [scanme.nmap.org](https://scanme.nmap.org), which the Nmap project provides for exactly this purpose. Scanning systems without authorization may be illegal.
 
## About
 
Built as a learning project to practice Python fundamentals (functions, error handling, file I/O) alongside core networking, cybersecurity, and concurrency concepts (sockets, ports, protocols, banner grabbing, multithreading, thread safety, basic vulnerability matching).