import json
import requests

def get_azerbaijani_arabic_loanwords():
    """Fetch Azerbaijani terms derived from Arabic from Wiktionary."""

    url = "https://en.wiktionary.org/w/api.php"

    headers = {
        "User-Agent": (
            "AzTurkTranslit/1.0 "
            "(personal lexicon research)"
        )
    }

    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": "Category:Azerbaijani terms derived from Arabic",
        "cmlimit": "max",
        "format": "json",
    }

    loanwords = []

    with requests.Session() as session:
        session.headers.update(headers)

        while True:
            try:
                response = session.get(
                    url,
                    params=params,
                    timeout=30,
                )

                if response.status_code != 200:
                    print(
                        f"HTTP Error: {response.status_code}"
                    )
                    print(
                        "Response details:",
                        response.text[:1000],
                    )
                    response.raise_for_status()

                data = response.json()

            except requests.exceptions.RequestException as error:
                print(f"Request failed: {error}")
                return []

            except ValueError as error:
                print(f"Invalid JSON response: {error}")
                return []

            # Extract category members.
            members = (
                data.get("query", {})
                .get("categorymembers", [])
            )

            for member in members:
                # Namespace 14 represents category pages.
                if member.get("ns") != 14:
                    loanwords.append(member["title"])

            # Continue fetching if more results are available.
            continuation = data.get("continue")

            if not continuation:
                break

            params.update(continuation)

    # Remove duplicates and sort alphabetically.
    return sorted(set(loanwords), key=str.casefold)


if __name__ == "__main__":
    word_list = get_azerbaijani_arabic_loanwords()

    if word_list:
        print(
            f"Found {len(word_list)} candidate Arabic "
            "loanwords in Azerbaijani.\n"
        )
        
        # Save output directly to lexicon.json file
        with open("lexicon.json", "w", encoding="utf-8") as file:
            json.dump(word_list, file, ensure_ascii=False, indent=4)
            
        print("Successfully saved data to lexicon.json.")
    else:
        print(
            "No words retrieved. Check the error messages "
            "above for details."
        )
