import typer
from rich import print

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

app = typer.Typer()


@app.command()
def order():

    print("[bold blue]Binance Futures Trading Bot[/bold blue]\n")

    symbol = typer.prompt("Enter Symbol").upper()

    side = typer.prompt(
        "BUY or SELL"
    ).upper()

    order_type = typer.prompt(
        "MARKET / LIMIT"
    ).upper()

    quantity = typer.prompt(
        "Quantity",
        type=float
    )

    price = None

    if order_type == "LIMIT":
        price = typer.prompt(
            "Price",
            type=float
        )

    try:

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        print("\n[yellow]Submitting Order...[/yellow]")

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n[green]===== ORDER SUCCESS =====[/green]")

        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice')}")

    except Exception as e:

        print(f"\n[red]ERROR:[/red] {e}")


if __name__ == "__main__":
    app()