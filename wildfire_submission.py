import os
import requests
import random
import time
from http.client import IncompleteRead
from requests.adapters import HTTPAdapter

# Path to the CA certificate (replace with your actual CA certificate path)
ca_cert = r'C:\Users\deisenhower\Desktop\python_scripts\ridpharm_ca.cer'

# List of file URLs to trigger WildFire submission (Palo Alto Networks & other services)
file_urls = [
    "https://wildfire.paloaltonetworks.com/publicapi/test/pe",      # PE Test File
    "https://wildfire.paloaltonetworks.com/publicapi/test/apk",     # APK Test File
    "https://wildfire.paloaltonetworks.com/publicapi/test/macos",   # macOS Test File
    "https://wildfire.paloaltonetworks.com/publicapi/test/elf",     # ELF Test File
]

# User-Agent list to simulate different browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.1.2 Safari/602.3.12",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.85 Mobile Safari/537.36"
]

# Function to create a directory on the user's desktop
def create_directory_on_desktop():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    download_directory = os.path.join(desktop_path, "wildfire_downloads")

    # Check if directory exists, if not, create it
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    return download_directory

# Function to download files and save to the specified directory
def download_files():
    download_directory = create_directory_on_desktop()  # Create the directory on the desktop

    while True:  # Infinite loop for continuous downloads
        for url in file_urls:
            try:
                print(f"\nAttempting to download from {url}")
                
                # Create a new session for every download (new TCP session)
                with requests.Session() as session:
                    adapter = HTTPAdapter(max_retries=0)  # No retries
                    session.mount("https://", adapter)

                    # Randomized headers to simulate browser behavior
                    headers = {
                        "User-Agent": random.choice(user_agents),
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                    }

                    # Shorter timeout (3s for connection and 5s for read)
                    response = session.get(url, headers=headers, verify=ca_cert, timeout=(3, 5))
                    response.raise_for_status()  # Raise an error for bad status codes

                    # Save the downloaded file to the specified directory
                    file_name = os.path.join(download_directory, url.split("/")[-1])
                    with open(file_name, "wb") as file:
                        file.write(response.content)

                    print(f"Downloaded {file_name} from {url}, Status Code: {response.status_code}, Content Length: {len(response.content)}\n")

            except IncompleteRead as e:
                print(f"Incomplete read for {url}: {e}. Skipping this file and moving to the next.\n")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err}. Skipping this file and moving to the next.\n")
            except requests.exceptions.HTTPError as http_err:
                # Handle HTTP errors like 403, 503, etc. (expected with blocking)
                print(f"HTTP error occurred (blocked or unavailable): {http_err} for {url}. Skipping this file.\n")
            except requests.exceptions.RequestException as req_err:
                print(f"Error downloading {url}: {req_err}. Skipping this file.\n")
            except Exception as e:
                print(f"Unexpected error: {e}. Skipping this file.\n")

            # Add a very short backoff to prevent hammering the server (0.5 seconds)
            time.sleep(0.5)

# Run the script continuously
download_files()
