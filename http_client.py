import socket


def http_request(ip, port, host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    try:
        result = sock.connect_ex((ip, port))

        if result != 0:
            print("HTTP connection failed")
            return

        sock.sendall(request.encode())

        response = b""

        while True:
            chunk = sock.recv(1024)

            if not chunk:
                break

            response += chunk

        text_response = response.decode(errors="replace")

        headers, separator, body = text_response.partition("\r\n\r\n")

        lines = headers.split("\r\n")


        print("\nHTTP Information")
        print("----------------")

        status_line = "Unknown"
        location = "Not provided"


        for line in lines:

            if line.startswith("HTTP/"):
                status_line = line
                print(f"Status: {line}")

            elif line.startswith("Server:"):
                print(line)

            elif line.startswith("Content-Type:"):
                print(line)
            elif line.startswith("Location:"):
                location = line



        if "200" in status_line:
            print("Meaning: Request successful")

        
        elif "301" in status_line or "302" in status_line:
            print("Meaning: Redirected to another location")
            print(location)


        elif "403" in status_line:
            print ("Meaning: Access forbidden")

        elif "404" in status_line:
            print("Meaning: Page not found")

        else:
            print("Meaning: Unknown status")    
        



    except TimeoutError:
        print("HTTP request timed out")

    except OSError as error:
        print(f"HTTP error: {error}")

    finally:
        sock.close()