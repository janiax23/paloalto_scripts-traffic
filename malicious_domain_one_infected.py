import socket
import time

print("Simulating Traffic Flow to a Malicious Domain from Content Update 4825-5343")

# Domain to simulate communication with a C2 server
c2_domain = "super-traffic.vip"

def simulate_infected_host(domain):
    while True:
        try:
            ip_address = socket.gethostbyname(domain)
            print(f"Domain: {domain}, IP Address: {ip_address}")
        except socket.gaierror as e:
            print(f"Domain: {domain}, Error: {e}")
        time.sleep(5)  # Delay between requests to simulate ongoing communication

# Simulate infected host communication
simulate_infected_host(c2_domain)
