import socket
import threading

KNOWN_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    554: "RTSP",
    1723: "PPTP",
    5060: "SIP",
}

from banner_grabber import grab_banner
from http_client import http_request


def analyze_service(ip, port, host):

    if port == 22:
        grab_banner(ip, port, host)

    elif port == 80:
        return "http"
    
    else:
        grab_banner(ip, port, host)



def scan_one_port(ip, port, host, results, lock):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    result = sock.connect_ex((ip, port))

    if result == 0:
        service = KNOWN_SERVICES.get(port, "Unknown")
        print(f"[OPEN] {port} ({service})")

        with lock:
            results.append({"port": port, "status": "open", "service": service})
        analyze_service(ip, port, host)

    else:
        print(f"[CLOSED/FILTERED] {port}")
        with lock:
            results.append({"port": port, "status": "closed/filtered", "service": None})

    sock.close()



def scan_ports(ip, host, ports):
    results = []
    lock = threading.Lock()

    print("\n======================")
    print("Port Scan")
    print("======================")

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_one_port, args=(ip, port, host, results, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("\nPort scan complete.")

    http_found = any(r["port"] == 80 and r["status"] == "open" for r in results)

    if http_found:
        print("\n======================")
        print("HTTP Analysis")
        print("======================")
        http_request(ip, 80, host)

    

    return results



    


  


