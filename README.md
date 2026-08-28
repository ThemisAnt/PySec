# PySec

A lightweight Python network reconnaissance tool. PySec scans a target domain for open ports, grabs service banners, analyzes HTTP responses, and saves a structured JSON report of the results — built as a hands-on project to learn Python and core networking/security concepts.

## Features

- **DNS resolution** — resolves a domain name to its IP address before scanning
- **Port scanning** — checks a user-specified list of ports to see which are open
- **Service identification** — maps common ports to known services (SSH, HTTP, FTP, DNS, etc.)
- **Banner grabbing** — connects to open ports and reads the service banner, cleanly labeling empty or non-text (binary) responses
- **HTTP analysis** — for open port 80, sends a raw HTTP request and parses the status code, server header, and content type
- **Graceful error handling** — invalid or unresolvable domains produce a clean error message instead of a crash
- **JSON reporting** — saves scan results to a `<domain>_scan_report.json` file for later review or use by other tools

## Requirements

- Python 3.x
- No external dependencies — uses only Python's built-in `socket` and `json` modules

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
   PySec v1.5
Network Security Tool
======================
Enter a Domain: scanme.nmap.org
Enter ports to scan: 22,80

======================
Port Scan
======================
[OPEN] 22 (SSH)
    Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
[OPEN] 80 (HTTP)

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

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — handles user input and ties everything together |
| `banner.py` | Displays the tool's startup banner |
| `dns_lookup.py` | Resolves a domain name to an IP address |
| `scanner.py` | Core port scanning logic and service identification |
| `banner_grabber.py` | Connects to open ports and reads service banners |
| `http_client.py` | Sends a raw HTTP request and parses the response |
| `report.py` | Saves scan results to a JSON report file |
| `utils.py` | Shared helper functions (e.g. banner classification) |

## Disclaimer

This tool is intended for educational purposes and for scanning systems you own or have explicit permission to test — such as [scanme.nmap.org](https://scanme.nmap.org), which the Nmap project provides for exactly this purpose. Scanning systems without authorization may be illegal.

## About

Built as a learning project to practice Python fundamentals (functions, error handling, file I/O) alongside core networking and cybersecurity concepts (sockets, ports, protocols, banner grabbing).
