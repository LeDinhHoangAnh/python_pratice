import threading
import requests
import time

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.stackoverflow.com",
]

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"{url}  Status: {response.status_code}")
    except Exception as e:
        print(f"[{url}]  Error: {e}")

print(">>> Check list website by sequence")
start_sequence = time.time()
for url in urls:
    check_website(url)
print(f"Time to execute by sequence: {round(time.time() - start_sequence, 2)} s\n")

print(">>> Check list website by multithreading")
threads = []
start_multithread = time.time()

for url in urls:
    t = threading.Thread(target=check_website, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print(f"Time to execute by multithreading: {round(time.time() - start_multithread, 2)} s")
