The public repository contains several Python scripts, which may help with:
    - testing whether DNS security works correctly and blocks malicious categories (DNS tunneling, DGA, ransomware, etc.)
    - testing a list of malicious domains that were published in content update 4825-5343 (the domains might need to be replaced with more up to date domains from newer content update)
    - continuously generating traffic to a single C2 domain to simulate an infected host
    - downloading testing Palo Alto files that trigger WildFire submission and test WildFire configuration
    - generating traffic for more than 200 App-IDs
    - testing URL filtering configuration (shows allowed and blocked websites, exists for both decrypted and encrypted traffic)

The individual scripts are: 
    - app_id_traffic.py
        > generates traffic to ~200 web applications to test whether App-ID functions correctly or just to generate some traffic  
    - dns_security_category_testing.py
        > tests whether firewall blocks DNS security malicious categories 
    - domain_malicious.py
        > generates traffic to malicious domains that were published in content update 4825-5343 (the domains might need to be replaced with more up to date domains from newer content update)
    - http_url_filtering-category_test.py
        > tests against Palo Alto Network HTTP testing pages whether URL filtering works as expected 
    - https_url_filtering-category_test.py
        > tests against Palo Alto Network HTTPS testing pages whether URL filtering works as expected 
    - malicious_domain_one_infected.py
        > continously generates traffic to a single domain to imitate an infected host communicating with a C2 domain   
    - wildfire_submission.py
        > tests whether WildFire profiles work as expected by downloading testing Palo Alto Networks files 
