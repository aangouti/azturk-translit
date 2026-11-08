import requests

# Use the cleaner REST API data tunnel to bypass portal redirection blocks
url = "https://wiktionary.org" 
# Let's hit the dedicated page content REST endpoint directly instead
url_page = "https://wiktionary.org"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

response = requests.get(url_page, headers=headers)

if response.status_code == 200:
    try:
        data = response.json()
        print("Success! JSON payload parsed perfectly.\n")
        # Print the first revision's text safely
        wikitext = data["revisions"][0]["slots"]["main"]["content"]
        print("--- RAW WIKITEXT SAMPLE ---")
        print(wikitext[:1000])
    except Exception as e:
        print(f"Parsing error: {e}")
else:
    print(f"Server rejected request with status code: {response.status_code}")
