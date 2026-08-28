from banner import show_banner
from dns_lookup import resolve_target
from scanner import scan_ports
from http_client import http_request
from report import save_report

show_banner()


target = input("Enter a Domain: ").strip()
ports = input("Enter ports to scan: ").strip()
port_list = [int(p) for p in ports.split(",")]

ip = resolve_target(target)

if ip is None:
    exit()



scan_results = scan_ports(ip, target, port_list)
save_report(target, scan_results)
