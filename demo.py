import asyncio
import aiohttp
import requests
import time
import sys

# List of URLs to request data from
URLS = [
    'https://github.com',
    'https://pypi.org',
    'https://nasa.gov',
    'https://espn.com',
    'https://cnn.com',
    'https://nfl.com'
]

# Synchronous function for fetching URLs
# This function uses the requests library to perform an HTTP GET request.
# It blocks the execution until the response is returned, hence it is synchronous.
def fetch_sync(url):
    return requests.get(url).text

# This function demonstrates synchronous requests to URLs.
# It iterates over a list of URLs and fetches their content one by one.
# The program will wait for each request to complete before moving to the next one.
def synchronous_demo():
    for url in URLS:
        content = fetch_sync(url)
        print(f"Fetched {len(content)} characters from {url}")

# Asynchronous coroutine for fetching URLs
# This coroutine uses aiohttp to perform an HTTP GET request.
# The 'await' keyword suspends execution of fetch_async until the response is ready, without blocking.
# Other tasks can run during this wait time, making the function non-blocking.
async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.text()

# This coroutine demonstrates asynchronous requests to URLs.
# It uses aiohttp.ClientSession to create a context manager that manages sessions.
# It then creates a list of task objects (not yet executed) for each URL.
# asyncio.gather() is used to run all the tasks concurrently.
# Each call to fetch_async will be awaited, but they will run concurrently, not sequentially.
async def asynchronous_demo():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in URLS]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(f"Fetched {len(response)} characters")

# Main function to run both synchronous and asynchronous demos.
def main():
    print("Running synchronous demo...")
    # Time measurement for synchronous execution starts.
    start_time = time.time()
    synchronous_demo()
    # Calculate duration of synchronous execution.
    sync_duration = time.time() - start_time
    print(f"Synchronous demo took {sync_duration:.2f} seconds\n")

    print("Running asynchronous demo...")
    # Time measurement for asynchronous execution starts.
    start_time = time.time()
    # asyncio.run is a high-level API to run the event loop, used here to run the asynchronous demo.
    # If running on Windows, an event loop policy is set to ensure compatibility.
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(asynchronous_demo())
    # Calculate duration of asynchronous execution.
    async_duration = time.time() - start_time
    print(f"Asynchronous demo took {async_duration:.2f} seconds")

# The if __name__ == '__main__': check ensures this code runs only when this script is executed directly,
# and not when it is imported as a module in another script.
if __name__ == '__main__':
    main()
