cache = {}
capacity    = 3
recently_used = []
def add_to_cache(key,value):
    if key in cache:
        recently_used.remove(key)
    elif len(recently_used)>=capacity:
        oldest_key =recently_used.pop(0)
        cache.pop(oldest_key)
    cache[key] = value
    recently_used.append(key)
    print(cache)
    print(recently_used)
def access_cache(key):
    if key in cache:
        recently_used.remove(key)
        recently_used.append(key)
        return cache[key]
    else:
        return None
