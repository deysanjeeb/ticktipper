# ticktipper
This project is a web scraper that automatically retrieves equity technical intraday tips and calls from the Nirmal Bang website and sends them via a Telegram bot.

## Requirements

- Python 3
- Selenium
- BeautifulSoup
- python-telegram-bot
- requests

## Setup

1. Install the required Python packages:

```bash
pip install selenium beautifulsoup4 python-telegram-bot requests
```
2. Download the appropriate ChromeDriver for your system and put it in your system's PATH, or specify its location in the executable_path argument when creating the Service object.

3. Create a config.py file with the following variables:

```bash
token = 'YOUR_TELEGRAM_BOT_TOKEN'
phno = 'YOUR_PHONE_NUMBER'
```
Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your Telegram bot's API token and 'YOUR_PHONE_NUMBER' with your phone number.

## Usage
Run the main.py script:

```bash
python main.py
```
