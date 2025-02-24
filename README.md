# Repository Overview

The public repository contains several Python scripts that may help with:

- **Testing DNS Security:**  
  Verify that DNS security works correctly by blocking malicious categories (DNS tunneling, DGA, ransomware, etc.).

- **Validating Malicious Domains:**  
  Test a list of malicious domains published in content update 4825-5343 (note: these domains might need to be replaced with more up-to-date ones from newer content updates).

- **Simulating Infected Hosts:**  
  Continuously generate traffic to a single C2 domain to simulate an infected host.

- **Testing WildFire Configuration:**  
  Download testing Palo Alto files that trigger WildFire submissions.

- **Generating App-ID Traffic:**  
  Generate traffic for more than 200 App-IDs.

- **Evaluating URL Filtering:**  
  Test URL filtering configuration (shows allowed and blocked websites for both decrypted and encrypted traffic).

## Individual Scripts

- **app_id_traffic.py**  
  > Generates traffic to approximately 200 web applications to test whether App-ID functions correctly or simply to generate traffic.

- **dns_security_category_testing.py**  
  > Tests if the firewall blocks malicious DNS security categories.

- **domain_malicious.py**  
  > Generates traffic to malicious domains from content update 4825-5343 (these domains may need to be updated based on newer content).

- **http_url_filtering-category_test.py**  
  > Tests against Palo Alto Networks HTTP testing pages to ensure URL filtering works as expected.

- **https_url_filtering-category_test.py**  
  > Tests against Palo Alto Networks HTTPS testing pages to verify URL filtering functionality.

- **malicious_domain_one_infected.py**  
  > Continuously generates traffic to a single domain to imitate an infected host communicating with a C2 domain.

- **wildfire_submission.py**  
  > Tests WildFire profiles by downloading testing files from Palo Alto Networks.
