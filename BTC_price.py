import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd,rub"
    response = requests.get(url)
    data = response.json()
    crypto_price_usd = data[crypto_id]['usd']
    crypto_price_rub = data[crypto_id]['rub']
    return crypto_price_usd, crypto_price_rub

# Example usage:
btc_price_usd, btc_price_rub = get_crypto_price('bitcoin')
print(f"The current price of Bitcoin is ${btc_price_usd} = {btc_price_rub} RUB")

eth_price_usd, eth_price_rub = get_crypto_price('ethereum')
print(f"The current price of Ethereum is ${eth_price_usd} = {eth_price_rub} RUB")

#eth_price = get_crypto_price('ethereum')
#print(f"The current price of Ethereum is ${eth_price}")
