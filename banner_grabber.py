import socket

from utils import classify_banner
from vuln_db import check_vulnerabilities


def grab_banner(ip, port, host, results, lock):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        result = sock.connect_ex((ip, port))

        if result != 0:
            return

        banner = sock.recv(1024).decode(errors="replace").strip()
        label = classify_banner(banner)
        print(f"    [{port}] Banner: {label}")

        vulns = check_vulnerabilities(banner)

        for v in vulns:
            print(f"    [{port}] ⚠ VULNERABLE: {v['cve']} ({v['severity']}) - {v['description']}")

            if vulns:
                with lock:
                    for v in vulns:
                        results.append({
                            "port": port,
                            "type": "vulnerability",
                            "cve": v["cve"],
                            "severity":  v["severity"],
                            "description": v["description"]
                        })

    except TimeoutError:
        print(f"    [{port}] Banner: No automatic response")

    except OSError as error:
        print(f"    [{port}] Banner error: {error}")

    finally:
        sock.close()