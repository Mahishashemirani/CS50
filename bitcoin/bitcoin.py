import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return float(data['bpi']['USD']['rate_float'])
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        btc_amount = float(sys.argv[1])
    except ValueError:
        print("Error: <number_of_bitcoins> must be a valid number.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost_usd = btc_amount * bitcoin_price

    print(f"Cost of {btc_amount:,.4f} Bitcoins: ${total_cost_usd:,.4f}")


if __name__ == "__main__":
    main()
