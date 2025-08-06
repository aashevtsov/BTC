import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    btc_price = data['bitcoin']['usd']
    return btc_price

# Example usage:
btc_price = get_btc_price()
print(f"The current price of Bitcoin is ${btc_price}")