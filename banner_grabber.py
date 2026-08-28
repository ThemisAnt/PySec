import socket

from utils import classify_banner


def grab_banner(ip, port, host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        result = sock.connect_ex((ip, port))

        if result != 0:
            return

        banner = sock.recv(1024).decode(errors="replace").strip()
        label = classify_banner(banner)
        print(f"    Banner: {label}")
        
        

    except TimeoutError:
        print("    Banner: No automatic response")

    except OSError as error:
        print(f"    Banner error: {error}")

    finally:
        sock.close()