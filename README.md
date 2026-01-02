# Junior Python Crypto Trading Bot (Binance Futures Testnet)

This project is a Python-based trading bot that I built as part of the **Junior Python Developer internship application task**.  
The bot works on the **Binance Futures Testnet (USDT-M)** and allows users to place trades using the official Binance API.

---

## Project Description

The goal of this assignment was to build a simplified trading bot that can interact with the Binance Futures Testnet using API credentials, accept user input from the command line, and log all trading activity.

In this project, the bot:

- Connects to **Binance Futures Testnet** using API keys  
- Places **Market and Limit orders** for both Buy and Sell  
- Uses **Python** with the `python-binance` library (REST API)  
- Accepts user input through a **command-line interface (CLI)**  
- Displays order execution status in the terminal  
- Logs all API requests, order activity, and errors  

### Bonus Features Implemented
- Added **Stop-Limit order** as a third order type  
- Implemented a **menu-based CLI** for easier interaction  

---

## Features

- Market Orders (Buy / Sell)  
- Limit Orders (Buy / Sell)  
- Stop-Limit Orders (Buy / Sell)  
- Menu-based CLI for order selection  
- Logging of all orders and errors in `bot.log`  
- Clean and reusable Python class structure  
- Proper error handling using exceptions  

---

## Setup and Installation

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd trading-bot

