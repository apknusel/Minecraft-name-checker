from requests_html import HTML, HTMLSession

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d71f0ce9c4992b23bac6e05750d2f410b1602358429; __cmpcc=1; _pubcid=2c482c4d-dc04-4aff-8c3c-83a09963cf0e',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

def main():
    get_time("tough")

def get_time(username):
    url = "https://namemc.com/search?q="+username
    session = HTMLSession()
    req = session.get(url)
    print(req.html.find('#availability-time', first=True))

if __name__ == "__main__":
    main()
