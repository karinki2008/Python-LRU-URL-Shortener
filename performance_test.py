from time import perf_counter
from database import get_url
from cache import add_to_cache,access_cache

short_code = "MQ3M"
#get the original url from sqlite
original_url = get_url(short_code)

if original_url is None:
    print("short code not found in database")

else:
    add_to_cache(short_code, original_url)

    iterations = 5000
    start = perf_counter()
    for i in range(iterations):
        get_url(short_code)

    database_time = perf_counter() - start
    start = perf_counter()
    for i in range(iterations):
        access_cache(short_code)
    cache_time = perf_counter() - start
    print("\n-----Performance Comparision---")
    print("Iterations: ", iterations)
    print("Database time:", database_time,"seconds")
    print("Cache time:", cache_time,"seconds")

    if cache_time > 0:
        print("Speed improvement:",database_time/cache_time,"times")