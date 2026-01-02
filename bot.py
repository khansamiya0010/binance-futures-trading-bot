import logging
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from config import API_KEY, API_SECRET

# Logging setup
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logging.info("Trading bot initialized")

    # Market order
    def place_market_order(self, symbol, side, quantity):
        try:
            self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info(
                f"Market order placed successfully | Symbol: {symbol}, Side: {side}, Quantity: {quantity}"
            )
            return True
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error(f"Market order failed: {e}")
            return False

    # Limit order
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logging.info(
                f"Limit order placed successfully | Symbol: {symbol}, Side: {side}, Quantity: {quantity}, Price: {price}"
            )
            return True
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error(f"Limit order failed: {e}")
            return False

    # Stop-Limit order (bonus)
    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                quantity=quantity,
                stopPrice=stop_price
            )
            logging.info(
                f"Stop-Limit order placed successfully | Symbol: {symbol}, Side: {side}, "
                f"Quantity: {quantity}, Stop Price: {stop_price}, Limit Price: {limit_price}"
            )
            return True
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error(f"Stop-Limit order failed: {e}")
            return False

# Menu-based CLI
def main_menu():
    print("=== Welcome to Junior Python Trading Bot ===")
    print("1. Place Market Order")
    print("2. Place Limit Order")
    print("3. Place Stop-Limit Order")
    choice = input("Enter choice (1/2/3): ")

    return choice

def get_order_inputs(order_type):
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Buy or Sell: ").upper()
    quantity = float(input("Quantity: "))

    price = None
    stop_price = None
    if order_type == "limit":
        price = float(input("Limit Price: "))
    elif order_type == "stop-limit":
        stop_price = float(input("Stop Price: "))
        price = float(input("Limit Price: "))

    return symbol, side, quantity, price, stop_price

if __name__ == "__main__":
    bot = BasicBot(API_KEY, API_SECRET)

    choice = main_menu()

    if choice == "1":
        symbol, side, quantity, _, _ = get_order_inputs("market")
        success = bot.place_market_order(symbol, side, quantity)
    elif choice == "2":
        symbol, side, quantity, price, _ = get_order_inputs("limit")
        success = bot.place_limit_order(symbol, side, quantity, price)
    elif choice == "3":
        symbol, side, quantity, price, stop_price = get_order_inputs("stop-limit")
        success = bot.place_stop_limit_order(symbol, side, quantity, stop_price, price)
    else:
        print("Invalid choice")
        exit()

    if success:
        print("\nOrder placed successfully!")
        print("Check bot.log for execution details.")
    else:
        print("\nOrder failed. Check bot.log for error details.")
