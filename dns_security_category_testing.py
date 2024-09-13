import requests
import time

# Path to the CA certificate on Windows
ca_cert = r'C:\Users\deisenhower\Desktop\python_scripts\ridpharm_ca.cer'  # Using a raw string

# Lists of DNS security testing URLs
c2_urls = ["https://test-c2.testpanw.com"]
dns_tunneling_urls = ["https://test-dnstun.testpanw.com"]
dga_urls = ["https://test-dga.testpanw.com"]
dynamic_dns_urls = ["https://test-ddns.testpanw.com"]
malware_urls = ["https://test-malware.testpanw.com"]
newly_registered_domains_urls = ["https://test-nrd.testpanw.com"]
phishing_urls = ["https://test-phishing.testpanw.com"]
grayware_urls = ["https://test-grayware.testpanw.com"]
parked_urls = ["https://test-parked.testpanw.com"]
proxy_avoidance_urls = ["https://test-proxy.testpanw.com"]
fast_flux_urls = ["https://test-fastflux.testpanw.com"]
malicious_nrd_urls = ["https://test-malicious-nrd.testpanw.com"]
nxns_attack_urls = ["https://test-nxns.testpanw.com"]
dangling_urls = ["https://test-dangling-domain.testpanw.com"]
dns_rebinding_urls = ["https://test-dns-rebinding.testpanw.com"]
dns_infiltration_urls = ["https://test-dns-infiltration.testpanw.com"]
wildcard_abuse_urls = ["https://test-wildcard-abuse.testpanw.com"]
strategically_aged_urls = ["https://test-strategically-aged.testpanw.com"]
compromised_dns_urls = ["https://test-compromised-dns.testpanw.com"]
ad_tracking_urls = ["https://test-adtracking.testpanw.com"]
cname_cloaking_urls = ["https://test-cname-cloaking.testpanw.com"]
ransomware_urls = ["https://test-ransomware.testpanw.com"]
stockpile_urls = ["https://test-stockpile-domain.testpanw.com"]
cybersquatting_urls = ["https://test-squatting.testpanw.com"]
subdomain_reputation_urls = ["https://test-subdomain-reputation.testpanw.com"]

def test_urls(category, urls):
    print(f"----------------------------------")
    print(f"Testing {category}")
    print(f"----------------------------------")
    for url in urls:
        try:
            response = requests.get(url, verify=ca_cert, timeout=10)  # Use the CA certificate for verification
            print(f"URL: {url}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"URL: {url}, Error: {e}")
        time.sleep(1)
    print("\n")

# Testing individual DNS security categories
test_urls("C2", c2_urls)
test_urls("DNS Tunneling", dns_tunneling_urls)
test_urls("DGA", dga_urls)
test_urls("Dynamic DNS", dynamic_dns_urls)
test_urls("Malware", malware_urls)
test_urls("Newly Registered Domains", newly_registered_domains_urls)
test_urls("Phishing", phishing_urls)
test_urls("Grayware", grayware_urls)
test_urls("Parked", parked_urls)
test_urls("Proxy Avoidance and Anonymizers", proxy_avoidance_urls)
test_urls("Fast Flux", fast_flux_urls)
test_urls("Malicious NRD", malicious_nrd_urls)
test_urls("NXNS Attack", nxns_attack_urls)
test_urls("Dangling", dangling_urls)
test_urls("DNS Rebinding", dns_rebinding_urls)
test_urls("DNS Infiltration", dns_infiltration_urls)
test_urls("Wildcard Abuse", wildcard_abuse_urls)
test_urls("Strategically-Aged", strategically_aged_urls)
test_urls("Compromised DNS", compromised_dns_urls)
test_urls("Ad Tracking", ad_tracking_urls)
test_urls("CNAME Cloaking", cname_cloaking_urls)
test_urls("Ransomware", ransomware_urls)
test_urls("Stockpile", stockpile_urls)
test_urls("Cybersquatting", cybersquatting_urls)
test_urls("Subdomain Reputation", subdomain_reputation_urls)

# Keep the prompt open
input("Press Enter to exit...")
