import requests

q = 'hilarious'
rating = 'g'
api_key = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My'
limit = 10

url = f'https://api.giphy.com/v1/gifs/search?q={q}&rating={rating}&api_key={api_key}&limit={limit}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("Error fetching data:", response.status_code)

data = list(filter(lambda gif: int(gif['images']['original']['height']) > 100, data['data']))

print(data[0])

q = input("Enter a search term or phrase: ").strip()

if q:
    url = f'https://api.giphy.com/v1/gifs/search?q={q}&rating=g&api_key={api_key}&limit={limit}'
else:
    if not q:
        print("No search term provided. Showing trending GIFs instead.")

    url = f'https://api.giphy.com/v1/gifs/trending?api_key={api_key}&limit={limit}&rating={rating}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("Error fetching data:", response.status_code)

for gif in list(data['data']):
    print(gif['url'])