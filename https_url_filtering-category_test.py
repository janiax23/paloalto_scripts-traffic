import requests
import time

# Path to the CA certificate on Windows
ca_cert = r'C:\Users\deisenhower\Desktop\python_scripts\ridpharm_ca.cer'  # Using a raw string

# Lists of HTTPS URLs to test
non_malicious_urls = [
    "https://urlfiltering.paloaltonetworks.com/test-abortion",
    "https://urlfiltering.paloaltonetworks.com/test-abused-drugs",
    "https://urlfiltering.paloaltonetworks.com/test-adult",
    "https://urlfiltering.paloaltonetworks.com/test-alcohol-and-tobacco",
    "https://urlfiltering.paloaltonetworks.com/test-auctions",
    "https://urlfiltering.paloaltonetworks.com/test-web-based-email",
    "https://urlfiltering.paloaltonetworks.com/test-cryptocurrency",
    "https://urlfiltering.paloaltonetworks.com/test-grayware",
    "https://urlfiltering.paloaltonetworks.com/test-business-and-economy",
    "https://urlfiltering.paloaltonetworks.com/test-computer-and-internet-info",
    "https://urlfiltering.paloaltonetworks.com/test-content-delivery-networks",
    "https://urlfiltering.paloaltonetworks.com/test-copyright-infringement",
    "https://urlfiltering.paloaltonetworks.com/test-dating",
    "https://urlfiltering.paloaltonetworks.com/test-dynamic-dns",
    "https://urlfiltering.paloaltonetworks.com/test-educational-institutions",
    "https://urlfiltering.paloaltonetworks.com/test-entertainment-and-arts",
    "https://urlfiltering.paloaltonetworks.com/test-extremism",
    "https://urlfiltering.paloaltonetworks.com/test-financial-services",
    "https://urlfiltering.paloaltonetworks.com/test-gambling",
    "https://urlfiltering.paloaltonetworks.com/test-games",
    "https://urlfiltering.paloaltonetworks.com/test-government",
    "https://urlfiltering.paloaltonetworks.com/test-hacking",
    "https://urlfiltering.paloaltonetworks.com/test-health-and-medicine",
    "https://urlfiltering.paloaltonetworks.com/test-home-and-garden",
    "https://urlfiltering.paloaltonetworks.com/test-hunting-and-fishing",
    "https://urlfiltering.paloaltonetworks.com/test-insufficient-content",
    "https://urlfiltering.paloaltonetworks.com/test-internet-communications-and-telephony",
    "https://urlfiltering.paloaltonetworks.com/test-internet-portals",
    "https://urlfiltering.paloaltonetworks.com/test-job-search",
    "https://urlfiltering.paloaltonetworks.com/test-legal",
    "https://urlfiltering.paloaltonetworks.com/test-military",
    "https://urlfiltering.paloaltonetworks.com/test-motor-vehicles",
    "https://urlfiltering.paloaltonetworks.com/test-music",
    "https://urlfiltering.paloaltonetworks.com/test-news",
    "https://urlfiltering.paloaltonetworks.com/test-nudity",
    "https://urlfiltering.paloaltonetworks.com/test-online-storage-and-backup",
    "https://urlfiltering.paloaltonetworks.com/test-parked",
    "https://urlfiltering.paloaltonetworks.com/test-peer-to-peer",
    "https://urlfiltering.paloaltonetworks.com/test-personal-sites-and-blogs",
    "https://urlfiltering.paloaltonetworks.com/test-philosophy-and-political-advocacy",
    "https://urlfiltering.paloaltonetworks.com/test-private-ip-addresses",
    "https://urlfiltering.paloaltonetworks.com/test-proxy-avoidance-and-anonymizers",
    "https://urlfiltering.paloaltonetworks.com/test-questionable",
    "https://urlfiltering.paloaltonetworks.com/test-real-estate",
    "https://urlfiltering.paloaltonetworks.com/test-recreation-and-hobbies",
    "https://urlfiltering.paloaltonetworks.com/test-reference-and-research",
    "https://urlfiltering.paloaltonetworks.com/test-religion",
    "https://urlfiltering.paloaltonetworks.com/test-search-engines",
    "https://urlfiltering.paloaltonetworks.com/test-sex-education",
    "https://urlfiltering.paloaltonetworks.com/test-shareware-and-freeware",
    "https://urlfiltering.paloaltonetworks.com/test-shopping",
    "https://urlfiltering.paloaltonetworks.com/test-social-networking",
    "https://urlfiltering.paloaltonetworks.com/test-society",
    "https://urlfiltering.paloaltonetworks.com/test-sports",
    "https://urlfiltering.paloaltonetworks.com/test-stock-advice-and-tools",
    "https://urlfiltering.paloaltonetworks.com/test-streaming-media",
    "https://urlfiltering.paloaltonetworks.com/test-swimsuits-and-intimate-apparel",
    "https://urlfiltering.paloaltonetworks.com/test-training-and-tools",
    "https://urlfiltering.paloaltonetworks.com/test-translation",
    "https://urlfiltering.paloaltonetworks.com/test-travel",
    "https://urlfiltering.paloaltonetworks.com/test-unknown",
    "https://urlfiltering.paloaltonetworks.com/test-weapons",
    "https://urlfiltering.paloaltonetworks.com/test-web-advertisements",
    "https://urlfiltering.paloaltonetworks.com/test-web-hosting"
]
risk_url_categories = [
    "https://urlfiltering.paloaltonetworks.com/test-low-risk",
    "https://urlfiltering.paloaltonetworks.com/test-medium-risk",
    "https://urlfiltering.paloaltonetworks.com/test-high-risk"
]

malicious_url_categories = [
    "https://urlfiltering.paloaltonetworks.com/test-malware",
    "https://urlfiltering.paloaltonetworks.com/test-phishing",
    "https://urlfiltering.paloaltonetworks.com/test-command-and-control",
    "https://urlfiltering.paloaltonetworks.com/test-ransomware"
]


def test_urls(category, urls, ca_cert):
    print(f"----------------------------------")
    print(f"Testing {category}")
    print(f"----------------------------------")
    for url in urls:
        try:
            # Send HTTPS request with CA certificate
            response = requests.get(url, timeout=10, verify=ca_cert)
            print(f"URL: {url}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"URL: {url}, Error: {e}")
        time.sleep(1)
    print("\n")


# Testing Non-Malicious URLs
test_urls("Non-Malicious URLs", non_malicious_urls, ca_cert)

# Testing Risk URL Categories
test_urls("Risk URL Categories", risk_url_categories, ca_cert)

# Testing Malicious URL Categories
test_urls("Malicious URL Categories", malicious_url_categories, ca_cert)

# Keep the prompt open
input("Press Enter to exit ...")
