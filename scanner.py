import socket

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



def scan_ports(ip, host, ports):

    
    http_found = False
    results= []
    


    print("\n======================")
    print("Port Scan")
    print("======================")



    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((ip, port))

        if result == 0:
            service = KNOWN_SERVICES.get(port, "Unknown")
            print(f"[OPEN] {port} ({service})")

            
            results.append({"port": port, "status": "open", "service": service})




            service_result = analyze_service(ip, port, host)
            

            if service_result == "http":
                http_found = True

        
        else:
            print(f"[CLOSED/FILTERED] {port}")
            results.append({"port": port, "status": "closed/filtered", "service": None})

        sock.close()

        

    print("\nPort scan complete.")

    if http_found:
        print("\n======================")
        print("HTTP Analysis")
        print("======================")

        http_request(ip, 80, host)
    return results