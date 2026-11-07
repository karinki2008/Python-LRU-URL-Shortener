import random
import string
from database import save_url,get_url,code_exists
from cache import access_cache,add_to_cache
def get_original_url(code):
    original_url = access_cache(code)

    if original_url is not None:
        print ("cache hit ! ")
        return original_url
    print("cache miss!,searching database......")
    original_url = get_url(code)
    if original_url is not None:
        add_to_cache(code,original_url)
    return original_url
characters = string.ascii_uppercase + string.digits

while True:
    original_url = input("Enter the original URL: ")

    if original_url.lower()=="exit":
        break
    original_url = original_url.strip()

    code = ""

    for i in range(4):
        code = code + random.choice(characters)

    while code_exists(code):
        code = ""
        for i in range(4):
            code = code + random.choice(characters)
    save_url(code,original_url)
    print("Generated short code:", code)
while True:
    print("\nRetrieve original URL:")

    search_code = input("Enter short code: ")

    result = get_original_url(search_code)

    if result is None:
        print("Short code not found!")
    else:
        print("Original URL:", result)