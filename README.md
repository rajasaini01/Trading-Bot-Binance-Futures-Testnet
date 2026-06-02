# Binance Futures Testnet Trading Bot

A Python-based trading bot for Binance Futures Testnet (USDT-M) that supports Market and Limit Orders through both an interactive CLI and a lightweight Streamlit web interface.

## Features

- Place MARKET orders

- Place LIMIT orders

- BUY and SELL support

- Binance Futures Testnet integration

- Input validation

- Error handling

- API request/response logging

- Interactive CLI using Typer

- Lightweight Web UI using Streamlit

- Structured and reusable codebase

---

## Project Structure

```text
Trading-Bot-Binance-Futures-Testnet/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── app.py
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd Trading-Bot-Binance-Futures-Testnet
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Credentials

Create a `.env` file in the project root:

```env
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_api_secret
```

---

## Running the Application

### Interactive CLI

```bash
python cli.py
```

Example:

```text
Enter Symbol: BTCUSDT
BUY or SELL: BUY
MARKET / LIMIT: MARKET
Quantity: 0.001
```

---

### Streamlit Web UI

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## Example Orders

### Market Order

```text
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.001
```

### Limit Order

```text
Symbol: BTCUSDT
Side: SELL
Order Type: LIMIT
Quantity: 0.001
Price: 120000
```

---

## Logging

All API requests, responses, and errors are recorded in:

```text
logs/bot.log
```

The repository includes logs demonstrating:

* MARKET Order execution
* LIMIT Order execution
* Request details
* Response details
* Error tracking

---

## Assumptions

* Binance Futures Testnet account is active.
* Valid Testnet API credentials are configured.
* User has sufficient testnet balance available.
* Internet connection is available during execution.
* Orders are executed only on Binance Futures Testnet.

---

## Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* Typer
* Rich
* Streamlit

---

## Author

Developed as part of the Python Developer Technical Assessment for Binance Futures Testnet Trading Bot.
