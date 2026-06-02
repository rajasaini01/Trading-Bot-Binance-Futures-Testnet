from bot.client import get_client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logger.info(f"Order Request: {params}")

    response = client.futures_create_order(**params)

    logger.info(f"Order Response: {response}")

    return response