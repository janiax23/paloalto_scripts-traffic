import requests
import random
import urllib3
from requests.adapters import HTTPAdapter
import time

# You can enable SSL warnings since we're now using trusted certificates
# If you still want to disable warnings, uncomment the following line:
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List of unique URLs
urls = [
    "https://www.salesforce.com",
    "https://www.google.com/drive/",
    "https://www.microsoft.com/en-us/microsoft-365",
    "https://www.zoho.com",
    "https://www.dropbox.com",
    "https://www.box.com",
    "https://www.adobe.com",
    "https://www.sap.com",
    "https://www.slack.com",
    "https://www.webex.com",
    "https://www.zoom.us",
    "https://www.atlassian.com",
    "https://www.gitlab.com",
    "https://www.github.com",
    "https://www.trello.com",
    "https://www.workday.com",
    "https://www.shopify.com",
    "https://www.servicenow.com",
    "https://www.snowflake.com",
    "https://www.okta.com",
    "https://www.cloudflare.com",
    "https://www.twilio.com",
    "https://www.hubspot.com",
    "https://www.docusign.com",
    "https://www.figma.com",
    "https://www.airtable.com",
    "https://www.clickup.com",
    "https://www.monday.com",
    "https://www.netsuite.com",
    "https://www.squarespace.com",
    "https://www.wix.com",
    "https://www.freshbooks.com",
    "https://www.quickbooks.intuit.com",
    "https://www.intuit.com",
    "https://www.asana.com",
    "https://www.bitbucket.org",
    "https://www.oracle.com",
    "https://aws.amazon.com",
    "https://azure.microsoft.com",
    "https://www.heroku.com",
    "https://www.digitalocean.com",
    "https://www.typeform.com",
    "https://www.intercom.com",
    "https://www.miro.com",
    "https://www.crowdstrike.com",
    "https://www.datadoghq.com",
    "https://www.loom.com",
    "https://www.hellosign.com",
    "https://www.freshdesk.com",
    "https://www.zendesk.com",
    "https://www.segment.com",
    "https://www.splunk.com",
    "https://www.mixpanel.com",
    "https://www.concur.com",
    "https://www.toggl.com",
    "https://www.smartsheet.com",
    "https://www.pipedrive.com",
    "https://www.xero.com",
    "https://www.dynatrace.com",
    "https://www.appdynamics.com",
    "https://www.jira.com",
    "https://www.notion.so",
    "https://www.expensify.com",
    "https://www.surveymonkey.com",
    "https://www.qualtrics.com",
    "https://www.ustream.tv",
    "https://www.citrix.com",
    "https://www.boxcryptor.com",
    "https://www.rightsignature.com",
    "https://www.sage.com",
    "https://www.hightail.com",
    "https://www.bitdefender.com",
    "https://www.pingidentity.com",
    "https://www.adroll.com",
    "https://www.knime.com",
    "https://www.pagerduty.com",
    "https://www.kaltura.com",
    "https://www.logmein.com",
    "https://www.newrelic.com",
    "https://www.citrixonline.com",
    "https://www.teamviewer.com",
    "https://www.webroot.com",
    "https://www.jamf.com",
    "https://www.anaplan.com",
    "https://www.spiceworks.com",
    "https://www.talentlms.com",
    "https://www.gainsight.com",
    "https://www.blackbaud.com",
    "https://www.callrail.com",
    "https://www.databricks.com",
    "https://www.zscaler.com",
    "https://www.crunchbase.com",
    "https://www.bamboohr.com",
    "https://www.chargify.com",
    "https://www.mailchimp.com",
    "https://www.autodesk.com",
    "https://www.knowbe4.com",
    "https://www.vendasta.com",
    "https://www.zoho.com/desk/",
    "https://www.microsoft.com/powerbi/",
    "https://www.salesforce.com/marketing-cloud",
    "https://www.tableau.com/",
    "https://www.servicenow.com/workflows",
    "https://www.workday.com/en-us/solutions.html",
    "https://www.simplercloud.com/",
    "https://www.google.com/analytics/",
    "https://www.dropbox.com/business",
    "https://aws.amazon.com/marketplace",
    "https://www.vmware.com/products/horizon.html",
    "https://azure.microsoft.com/en-us/services/active-directory/",
    "https://www.cisco.com/c/en/us/products/security/cloudlock/",
    "https://www.atlassian.com/software/jira",
    "https://www.sap.com/products/s4hana-cloud.html",
    "https://www.ibm.com/cloud-computing/",
    "https://www.oracle.com/cloud/"
    "https://www.microsoft.com/teams/",
    "https://slack.com/intl/en-in/",
    "https://www.zoom.us/",
    "https://www.webex.com/",
    "https://www.dropbox.com/",
    "https://www.box.com/",
    "https://www.cisco.com/c/en/us/products/unified-communications/",
    "https://www.google.com/chat/",
    "https://www.icloud.com/",
    "https://www.onedrive.live.com/",
    "https://drive.google.com/",
    "https://www.sync.com/",
    "https://www.egnyte.com/",
    "https://www.mediafire.com/",
    "https://www.megaupload.com/",
    "https://www.wetransfer.com/",
    "https://www.facebook.com/",
    "https://www.twitter.com/",
    "https://www.instagram.com/",
    "https://www.linkedin.com/",
    "https://www.snapchat.com/",
    "https://www.tiktok.com/",
    "https://www.pinterest.com/",
    "https://www.paypal.com/",
    "https://www.stripe.com/",
    "https://www.squareup.com/",
    "https://www.payoneer.com/",
    "https://www.venmo.com/",
    "https://www.wellsfargo.com/",
    "https://www.chase.com/",
    "https://www.bankofamerica.com/",
    "https://aws.amazon.com/",
    "https://cloud.google.com/",
    "https://azure.microsoft.com/",
    "https://www.ibm.com/cloud/",
    "https://cloud.oracle.com/",
    "https://www.digitalocean.com/",
    "https://www.linode.com/",
    "https://www.gitlab.com/",
    "https://github.com/",
    "https://bitbucket.org/",
    "https://www.jenkins.io/",
    "https://www.circleci.com/",
    "https://travis-ci.org/",
    "https://www.puppet.com/",
    "https://www.ansible.com/",
    "https://www.salesforce.com/",
    "https://www.hubspot.com/",
    "https://www.zoho.com/",
    "https://www.pipedrive.com/",
    "https://www.marketo.com/",
    "https://www.mailchimp.com/",
    "https://www.activecampaign.com/",
    "https://www.infusionsoft.com/",
    "https://www.youtube.com/",
    "https://www.netflix.com/",
    "https://www.hulu.com/",
    "https://www.spotify.com/",
    "https://www.vimeo.com/",
    "https://www.soundcloud.com/",
    "https://www.twitch.tv/",
    "https://www.dailymotion.com/"
    "https://www.office.com",
    "https://www.barracuda.com",
    "https://www.bluecoat.com",
    "https://www.meraki.cisco.com",
    "https://www.webroot.com",
    "https://www.netskope.com",
    "https://www.citrix.com/solutions/workspace",
    "https://www.ibm.com/watson",
    "https://www.dropbox.com/transfer",
    "https://www.symantec.com",
    "https://www.proofpoint.com",
    "https://www.vmware.com/products/appdefense.html",
    "https://www.carbonblack.com",
    "https://www.checkpoint.com",
    "https://www.crowdstrike.com",
    "https://www.forcepoint.com",
    "https://www.mcafee.com",
    "https://www.paloaltonetworks.com",
    "https://www.qualys.com",
    "https://www.sonicwall.com",
    "https://www.sophos.com",
    "https://www.tenable.com",
    "https://www.trendmicro.com",
    "https://www.verizon.com/business/solutions/security",
    "https://www.kaspersky.com",
    "https://www.avast.com",
    "https://www.bitdefender.com",
    "https://www.malwarebytes.com",
    "https://www.cybereason.com",
    "https://www.darktrace.com",
    "https://www.guardicore.com",
    "https://www.rsa.com",
    "https://www.deepinstinct.com",
    "https://www.secureworks.com",
    "https://www.menlosecurity.com",
    "https://www.cylance.com",
    "https://www.fireeye.com",
    "https://www.rapid7.com",
    "https://www.threatstack.com",
    "https://www.vmware.com/products/workspace-one.html",
    "https://www.citrix.com/products/citrix-endpoint-management.html",
    "https://www.manageengine.com/products/desktop-central/",
    "https://www.splunk.com/en_us/software/splunk-enterprise-security.html",
    "https://www.alienvault.com",
    "https://www.blackberry.com/us/en/products/spark",
    "https://www.ibm.com/security",
    "https://www.trendmicro.com/en_us/business/solutions/cloud.html",
    "https://www.sophos.com/en-us/products/cloud-optix.aspx",
    "https://www.skyboxsecurity.com",
    "https://www.mcafee.com/enterprise/en-us/products/cloud-security.html",
    "https://www.tanium.com"
]

# User-Agent list to simulate different browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 "
    "(KHTML, like Gecko) Version/10.1.2 Safari/602.3.12",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) "
    "AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.85 Mobile Safari/537.36"
]

# Function to simulate traffic generation with real data retrieval
def simulate_real_traffic():
    for url in urls:
        try:
            # Create a new session for each URL (ensures separate TCP connections)
            with requests.Session() as session:
                session.mount("https://", HTTPAdapter(max_retries=0))

                # Randomized headers to simulate browser behavior
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept": (
                        "text/html,application/xhtml+xml,application/xml;q=0.9,"
                        "image/webp,image/apng,*/*;q=0.8"
                    ),
                }

                # Perform GET request using the system's trusted certificates
                response = session.get(url, headers=headers, timeout=(5, 10))

                # Print the URL, Status Code, and Content Length in one line
                print(
                    f"{url}, Status Code: {response.status_code}, "
                    f"Content Length: {len(response.content)} bytes"
                )

        except requests.exceptions.RequestException as e:
            print(f"Error: {e} for {url}")

# Run the traffic simulation in an infinite loop
while True:
    simulate_real_traffic()
    time.sleep(5)  # Pause for 5 seconds between loops to avoid overwhelming the server
