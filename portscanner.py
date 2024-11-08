import socket, termcolor, threading

def scan_port(ip, port):
  try:
    sock = socket.socket()
    sock.settimeout(0.5)
    sock.connect((ip, port))
    print(termcolor.colored(f"[+] Port {port} is open", 'green'))
    sock.close()
  except:
    pass
    # print(termcolor.colored(f"[-] port {port} is closed", 'red'))
        
targets = input("Insert the targets you want to scan (comma-separated):   ")
ports = int(input("How many ports do you want to scan:   "))

for ip in targets.split(','):
  print(termcolor.colored(f'[*] Scanning {ip}...  ', 'blue'))
  for port in range(1, ports+1):
    thread = threading.Thread(target=scan_port, args=(ip, port))
    thread.start()