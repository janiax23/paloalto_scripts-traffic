import requests
import time

# Lists of URLs to test
non_malicious_urls = [
    "http://urlfiltering.paloaltonetworks.com/test-abortion",
    "http://urlfiltering.paloaltonetworks.com/test-abused-drugs",
    "http://urlfiltering.paloaltonetworks.com/test-adult",
    "http://urlfiltering.paloaltonetworks.com/test-alcohol-and-tobacco",
    "http://urlfiltering.paloaltonetworks.com/test-auctions",
    "http://urlfiltering.paloaltonetworks.com/test-web-based-email",
    "http://urlfiltering.paloaltonetworks.com/test-cryptocurrency",
    "http://urlfiltering.paloaltonetworks.com/test-grayware",
    "http://urlfiltering.paloaltonetworks.com/test-business-and-economy",
    "http://urlfiltering.paloaltonetworks.com/test-computer-and-internet-info",
    "http://urlfiltering.paloaltonetworks.com/test-content-delivery-networks",
    "http://urlfiltering.paloaltonetworks.com/test-copyright-infringement",
    "http://urlfiltering.paloaltonetworks.com/test-dating",
    "http://urlfiltering.paloaltonetworks.com/test-dynamic-dns",
    "http://urlfiltering.paloaltonetworks.com/test-educational-institutions",
    "http://urlfiltering.paloaltonetworks.com/test-entertainment-and-arts",
    "http://urlfiltering.paloaltonetworks.com/test-extremism",
    "http://urlfiltering.paloaltonetworks.com/test-financial-services",
    "http://urlfiltering.paloaltonetworks.com/test-gambling",
    "http://urlfiltering.paloaltonetworks.com/test-games",
    "http://urlfiltering.paloaltonetworks.com/test-government",
    "http://urlfiltering.paloaltonetworks.com/test-hacking",
    "http://urlfiltering.paloaltonetworks.com/test-health-and-medicine",
    "http://urlfiltering.paloaltonetworks.com/test-home-and-garden",
    "http://urlfiltering.paloaltonetworks.com/test-hunting-and-fishing",
    "http://urlfiltering.paloaltonetworks.com/test-insufficient-content",
    "http://urlfiltering.paloaltonetworks.com/test-internet-communications-and-telephony",
    "http://urlfiltering.paloaltonetworks.com/test-internet-portals",
    "http://urlfiltering.paloaltonetworks.com/test-job-search",
    "http://urlfiltering.paloaltonetworks.com/test-legal",
    "http://urlfiltering.paloaltonetworks.com/test-military",
    "http://urlfiltering.paloaltonetworks.com/test-motor-vehicles",
    "http://urlfiltering.paloaltonetworks.com/test-music",
    "http://urlfiltering.paloaltonetworks.com/test-news",
    "http://urlfiltering.paloaltonetworks.com/test-nudity",
    "http://urlfiltering.paloaltonetworks.com/test-online-storage-and-backup",
    "http://urlfiltering.paloaltonetworks.com/test-parked",
    "http://urlfiltering.paloaltonetworks.com/test-peer-to-peer",
    "http://urlfiltering.paloaltonetworks.com/test-personal-sites-and-blogs",
    "http://urlfiltering.paloaltonetworks.com/test-philosophy-and-political-advocacy",
    "http://urlfiltering.paloaltonetworks.com/test-private-ip-addresses",
    "http://urlfiltering.paloaltonetworks.com/test-proxy-avoidance-and-anonymizers",
    "http://urlfiltering.paloaltonetworks.com/test-questionable",
    "http://urlfiltering.paloaltonetworks.com/test-real-estate",
    "http://urlfiltering.paloaltonetworks.com/test-recreation-and-hobbies",
    "http://urlfiltering.paloaltonetworks.com/test-reference-and-research",
    "http://urlfiltering.paloaltonetworks.com/test-religion",
    "http://urlfiltering.paloaltonetworks.com/test-search-engines",
    "http://urlfiltering.paloaltonetworks.com/test-sex-education",
    "http://urlfiltering.paloaltonetworks.com/test-shareware-and-freeware",
    "http://urlfiltering.paloaltonetworks.com/test-shopping",
    "http://urlfiltering.paloaltonetworks.com/test-social-networking",
    "http://urlfiltering.paloaltonetworks.com/test-society",
    "http://urlfiltering.paloaltonetworks.com/test-sports",
    "http://urlfiltering.paloaltonetworks.com/test-stock-advice-and-tools",
    "http://urlfiltering.paloaltonetworks.com/test-streaming-media",
    "http://urlfiltering.paloaltonetworks.com/test-swimsuits-and-intimate-apparel",
    "http://urlfiltering.paloaltonetworks.com/test-training-and-tools",
    "http://urlfiltering.paloaltonetworks.com/test-translation",
    "http://urlfiltering.paloaltonetworks.com/test-travel",
    "http://urlfiltering.paloaltonetworks.com/test-unknown",
    "http://urlfiltering.paloaltonetworks.com/test-weapons",
    "http://urlfiltering.paloaltonetworks.com/test-web-advertisements",
    "http://urlfiltering.paloaltonetworks.com/test-web-hosting"
]
risk_url_categories = [
    "http://urlfiltering.paloaltonetworks.com/test-low-risk",
    "http://urlfiltering.paloaltonetworks.com/test-medium-risk",
    "http://urlfiltering.paloaltonetworks.com/test-high-risk"
]

malicious_url_categories = [
"http://urlfiltering.paloaltonetworks.com/test-malware",
"http://urlfiltering.paloaltonetworks.com/test-phishing",
"http://urlfiltering.paloaltonetworks.com/test-command-and-control",
"http://urlfiltering.paloaltonetworks.com/test-ransomware" 
]


def test_urls(category, urls):
    print(f"----------------------------------")
    print(f"Testing {category}")
    print(f"----------------------------------")
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            print(f"URL: {url}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"URL: {url}, Error: {e}")
        time.sleep(1)
    print("\n")


# Testing Non-Malicious URLs
test_urls("Non-Malicious URLs", non_malicious_urls)

# Testing Risk URL Categories
test_urls("Risk URL Categories", risk_url_categories)

# Testing Malicious URL Categories
test_urls("Malicious URL Categories", malicious_url_categories)

# Keep the prompt open
input ("Press Enter to exit ...")


