import streamlit as st
from bot.orders import place_order

st.title("Binance Futures Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox("Side", ["BUY", "SELL"])

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001
)

price = None

if order_type == "LIMIT":
    price = st.number_input(
        "Price",
        min_value=1.0,
        value=100000.0
    )

if st.button("Place Order"):
    try:
        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        st.success("Order Submitted Successfully")

        st.write(f"Order ID: {response.get('orderId')}")
        st.write(f"Status: {response.get('status')}")
        st.write(f"Executed Qty: {response.get('executedQty')}")
        st.write(f"Average Price: {response.get('avgPrice')}")

    except Exception as e:
        st.error(str(e))