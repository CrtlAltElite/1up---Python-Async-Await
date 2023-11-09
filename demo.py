import asyncio
import aiohttp
import requests
import time
import sys

# List of URLs for To Request from
URLS = [
    'https://github.com',
    'https://pypi.org',
    'https://nasa.gov',
    'https://espn.com',
    'https://cnn.com',
    'https://nfl.com'
]

# Synchronous (normal) version of fetching URLs
def fetch_sync(url):
    return requests.get(url).text

def synchronous_demo():
    for url in URLS:
        content = fetch_sync(url)
        print(f"Fetched {len(content)} characters from {url}")

# Asynchronous version of fetching URLs
async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.text()

async def asynchronous_demo():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in URLS]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(f"Fetched {len(response)} characters")

# Main function to run the demos
def main():
    print("Running synchronous demo...")
    if sys.platform == 'win32':
        # Windows-specific event-loop policy & selector
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    start_time = time.time()
    synchronous_demo()
    sync_duration = time.time() - start_time
    print(f"Synchronous demo took {sync_duration:.2f} seconds\n")

    print("Running asynchronous demo...")
    start_time = time.time()
    asyncio.run(asynchronous_demo())
    async_duration = time.time() - start_time
    print(f"Asynchronous demo took {async_duration:.2f} seconds")

if __name__ == '__main__':
    main()
