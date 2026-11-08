# Used to call Durnam API to get some transliterations. It's far from accurate
# import os
# import json
# import time
# import requests

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# INPUT_FILE = os.path.join(SCRIPT_DIR, "lexicon.json")
# # New isolated output destination file
# OUTPUT_FILE = os.path.join(SCRIPT_DIR, "lexicon_updated.json")

# DURNAM_API_URL = "https://app.durnam.com/api/transliterate"

# def transliterate_word(word: str) -> str:
#     """
#     Sends a single word query using your verified session credentials.
#     """
#     payload = {
#         "text": word
#     }
    
#     headers = {
#         "Host": "app.durnam.com",
#         "Accept": "application/json, text/plain, */*",
#         "Content-Type": "application/json",
#         "Authorization": "Bearer 3|lJkRUuFGs1bfsAa1HX68oT7mMBhY8ZDLkd3ZtEAw5ec1a3ec",
#         "Origin": "https://durnam.com",
#         "Referer": "https://durnam.com/",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
#     }
    
#     try:
#         response = requests.post(DURNAM_API_URL, json=payload, headers=headers, timeout=10)
#         if response.status_code == 200:
#             data = response.json()
#             print(f" -> Raw API response payload: {data}")
#             return data.get("output", "")
#         else:
#             print(f" -> Error {response.status_code} for word '{word}': {response.text}")
#             return ""
#     except Exception as e:
#         print(f" -> Exception raised while hitting API for '{word}': {e}")
#         return ""

# def main():
#     with open(INPUT_FILE, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     if isinstance(data, list):
#         data = {word: "" for word in data}

#     updated_count = 0
#     for word, current_translation in data.items():
#         if not current_translation:
#             print(f"\nTransliterating: {word}")
#             arabic_script = transliterate_word(word)
            
#             if arabic_script:
#                 data[word] = arabic_script
#                 updated_count += 1
#                 print(f" -> Successfully mapped: '{word}' -> '{arabic_script}'")
#                 time.sleep(0.5)

#     # Write out to the new distinct destination file pathway
#     with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
        
#     print(f"\nProcessing complete. Wrote {updated_count} updated terms to {OUTPUT_FILE}.")

# if __name__ == "__main__":
#     main()
