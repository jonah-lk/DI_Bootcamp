import requests, time

def measure_load_time(url):
    start = time.time()
    response = requests.get(url)
    end = time.time()

    load_time = end - start
    return load_time, response.status_code

websites = [
    "https://www.google.com",
    "https://www.ynet.co.il",
    "https://www.imdb.com",
    "https://www.wikipedia.org",
    "https://www.github.com"
]

for site in websites:
    t, status = measure_load_time(site)
    print(f"{site} loaded in {t:.3f} seconds (status {status})")