import os
from apify_client import ApifyClient

# Replace with your Apify API token
APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")

client = ApifyClient(APIFY_TOKEN)

# Example: Run All Video Scraper on YouTube
run_input = {
    "startUrls": [
        {"url": "https://www.youtube.com/@GoogleDevelopers"}
    ],
    "maxResults": 10
}

run = client.actor("agentx/all-video-scraper").call(run_input=run_input)

# Fetch results
for item in client.dataset(run["defaultDatasetId"]).list_items().items:
    print(item)