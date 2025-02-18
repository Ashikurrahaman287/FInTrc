# FinTrackBot 🤖💰

A Telegram bot to track personal finances, debts, credits, and expenses with intuitive categorization and summary features.

## Features ✨

- Track debts (money owed to you) and credits (money you owe)
- Daily transaction overview
- Balance summary with net worth calculation
- Expense categorization system
- Easy-to-use Telegram interface
- Docker container support 🐳

## Commands 📜
/start - Initialize the bot
/debt - Log new debt
/credit - Log new credit
/today - Show today's transactions
/summary - Financial summary
/categories - Spending by category
/help - List all commands

Copy

## Setup 🛠️

### Prerequisites
- Python 3.9+
- Docker (optional)
- Telegram account

### Configuration
1. Get your Telegram Bot Token from [@BotFather](https://t.me/BotFather)
2. Create `.env` file:
```env
TELEGRAM_TOKEN=your_bot_token_here
Docker Installation 🐳
bash
Copy
# Build the image
docker build -t fintrackbot .

# Run the container
docker run -d --name FinTrackBot --env-file .env fintrackbot
Manual Installation
bash
Copy
# Clone repository
git clone https://github.com/yourusername/FinTrackBot.git

# Install dependencies
pip install -r requirements.txt

# Run the bot
python Bot1.py
Categories 🏷️
Default spending categories:

Food 🍔

Transport 🚕

Bills 🧾

Entertainment 🎮

Friend 👫

Business 💼

Other 🤷

Contributing 🤝
Contributions welcome! Please open an issue first to discuss proposed changes.

License
MIT License - See LICENSE for details

Happy financial tracking! 💰📈

Copy

This README includes:
1. Project description and features
2. Command list matching your HELP_MESSAGE
3. Docker-specific instructions
4. Setup guide for both Docker and manual installation
5. Category list from your DEFAULT_CATEGORIES
6. Contribution guidelines
7. License information

You might want to:
1. Add actual screenshots
2. Update repository URLs
3. Add your requirements.txt if you have dependencies
4. Customize the license file
5. Add proper error handling documentation
6. Include deployment badges if needed
