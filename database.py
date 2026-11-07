import sqlite3
def save_url(short_code,original_url):
    connection = sqlite3.connect("urls.db")
    cursor =connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            short_code TEXT PRIMARY KEY,
            original_url TEXT NOT NULL
        )
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO urls (short_code, original_url)
    VALUES (?, ?)
    """,(short_code,original_url))
    connection.commit()
    connection.close()
def get_url(short_code):
    connection = sqlite3.connect("urls.db")
    cursor =connection.cursor()
    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()

    if result is None:
        return None
    else:
        return result[0]
def code_exists(short_code):
    return get_url(short_code) is not None

def get_all_urls():
    connection = sqlite3.connect("urls.db")
    cursor =connection.cursor()
    cursor.execute(
        "SELECT short_code, original_url FROM urls ORDER BY rowid DESC"
    )
    results = cursor.fetchall()
    connection.close()
    return results