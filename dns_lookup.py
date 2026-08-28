import socket

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"Error: Could not resolve '{target}'. Check the domain name and try again.")
        return None

    

