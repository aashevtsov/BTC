import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    crypto_price = data[crypto_id]['usd']
    return crypto_price

# Example usage:
btc_price = get_crypto_price('bitcoin')
print(f"The current price of Bitcoin is ${btc_price}")

eth_price = get_crypto_price('ethereum')
print(f"The current price of Ethereum is ${eth_price}")
