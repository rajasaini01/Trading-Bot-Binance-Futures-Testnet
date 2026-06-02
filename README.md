# Binance Futures Testnet Trading Bot

## Overview

A Python-based trading bot for Binance Futures Testnet (USDT-M) supporting Market and Limit orders with logging, validation, CLI interaction, and Streamlit UI.

## Features

* Market Orders
* Limit Orders
* BUY / SELL Support
* Binance Futures Testnet Integration
* Logging
* Error Handling
* Input Validation
* Enhanced CLI (Typer)
* Lightweight UI (Streamlit)

## Setup

1. Clone repository
2. Create virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create `.env`

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run CLI

```bash
python cli.py
```

## Run Web UI

```bash
streamlit run app.py
```

## Example Orders

### Market Order

Symbol: BTCUSDT

Side: BUY

Quantity: 0.001

### Limit Order

Symbol: BTCUSDT

Side: SELL

Quantity: 0.001

Price: 120000

## Assumptions

* Binance Futures Testnet account is active.
* Valid API credentials are configured.
* Orders are executed on Binance Futures Testnet.
