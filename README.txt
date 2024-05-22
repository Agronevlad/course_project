App Monitoring Telegram Bot

This Python script creates a Telegram bot that monitors the running time of selected applications on your system.

Prerequisites
- Python 3
- `psutil` library
- `telebot` library

Setup
1. Install the required Python libraries using pip:
```
pip install psutil telebot
```

2. Replace `'YOUR_BOT_TOKEN'` with your actual Telegram bot token.

Usage
1. Start the bot by running the script.
2. Open Telegram and start a chat with your bot.
3. Use the `/start` or `/restart` command to initialize the bot.
4. Choose the "Track" option to monitor the running time of specific applications.
5. Select an application from the provided list.
6. The bot will respond with the running time of the selected application.

Features
- Tracks the running time of specified applications.
- Provides running time information in minutes and seconds.
- Supports tracking multiple applications simultaneously.

Limitations
- Only supports Windows executable applications.
- Requires the application process names to be known in advance.

Example Applications
- `Valorant.exe`
- `Telegram.exe`
- `Discord.exe`
- `BIGFOOT.exe`

Author
This Telegram bot script was developed by Gareev and Frants