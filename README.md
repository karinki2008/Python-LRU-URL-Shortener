# Python LRU Cache-Based URL Shortener
## Project Description
This project is a URL Shortener application developed using Python and Flask

It converts long URL's into short easy to share links.

The application uses SQLite to stpre URL's permenantly and LRU(Least Recently Used) Cache to improve retrieval speed.

before redirecting the users to the original website,the application provides a destination preview and basic and suspicious URL warnings.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- LRU Cache (Data Structure)

## Key Features

- Converts long URLs into short links
- Generates unique 4-characters short codes.
- Stores URLs permanently using SQLite.
- Uses an LRU Cache for faster URL retrival.
- Implements cache hit ,cache miss, and LRU eviction.
- Provides Destination preview before redirection
- Display basic warnings for suspicious URLs.
- Maintain URL history.
- Allows users to copy shortened links.
- Compares cache and database retrival performance.


## How It Works

1. The user enters a long URL.
2. The application validates the URL.
3. A unique 4-character short code is generated.
4. The original URL and short code are stored in the SQLite database.
5. When someone accesses a short link, the application first checks the LRU Cache.
6. If the URL is found in the cache (Cache Hit), it is retrieved directly from memory.
7. If the URL is not found (Cache Miss), it is retrieved from SQLite and added to the cache.
8. The application displays a destination preview before redirecting the user to the original website.
9. The LRU Cache removes the least recently used entry when its capacity is full.


## Performance Testing

The application compares URL retrieval time using SQLite and the LRU Cache.

Test Configuration:
- Number of iterations: 5,000
- Database: SQLite
- Cache: LRU Cache

Test Results:

| Method | Execution Time |
|---|---:|
| SQLite Database | 1.6171 seconds |
| LRU Cache | 0.00121 seconds |

The LRU Cache achieved approximately 1,340 times faster retrieval in this local test compared with SQLite.

This demonstrates how caching can improve retrieval performance by reducing repeated database access.

## Installation and Setup
1.Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_LINK

2.Navigate to the project directory:

cd url-shortener-project

3.Install Flask:

pip install flask

4.Run the Application

Python app.py

5.Open the following url in your browser

http://127.0.0.1:5000


## Project Structure

url-shortener-project/

│

├── app.py

├── url_service.py

├── database.py

├── cache.py

├── performance_test.py

├── urls.db

│

├── templates/

│   ├── index.html

│   ├── preview.html

│   └── history.html

│

└── static/

    └── style.css
