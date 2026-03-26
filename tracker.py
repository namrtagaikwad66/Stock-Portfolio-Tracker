# tracker.py (offline version - works instantly)

STOCK_PRICES = {
    "AAPL": 150,
    "TSLA": 700,
    "GOOG": 2800,
    "MSFT": 300,
    "AMZN": 3300
}

def calculate_portfolio(portfolio):
    total = 0
    result = {}

    for symbol, qty in portfolio.items():
        if symbol in STOCK_PRICES:
            price = STOCK_PRICES[symbol]
            value = price * qty
            result[symbol] = {
                "price": price,
                "quantity": qty,
                "value": value
            }
            total += value
        else:
            result[symbol] = "Not Found"

    return total, result