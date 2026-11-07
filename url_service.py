import random
import string
from urllib.parse import urlparse
from database import save_url, code_exists,get_url
from cache import access_cache,add_to_cache
def is_valid_url(url):
    parsed_url = urlparse(url)
    return(
        parsed_url.scheme in ["http", "https"]
        and parsed_url.netloc != ""
        and "." in parsed_url.netloc
    )
def check_suspicious_url(url):

    suspicious_words = [
        "login-verify",
        "free-prize",
        "account-suspended",
        "claim-reward",
        "verify-account"
    ]

    url = url.lower()

    for word in suspicious_words:
        if word in url:
            return True

    return False
def generate_short_code():
    characters = string.ascii_uppercase + string.digits

    code = ""

    for i in range(4):
        code = code + random.choice(characters)

    while code_exists(code):
        code = ""

        for i in range(4):
            code = code + random.choice(characters)

    return code

def shorten_url(original_url):
    if not is_valid_url(original_url):
        return None,False
    suspicious_url = check_suspicious_url(original_url)
    code = generate_short_code()
    save_url(code,original_url)
    return code, suspicious_url
def get_original_url(code):
    original_url = access_cache(code)

    if original_url is not None:
        print("Cache hit!")
        return original_url

    print("Cache miss! Searching database...")

    original_url = get_url(code)

    if original_url is not None:
        add_to_cache(code, original_url)

    return original_url