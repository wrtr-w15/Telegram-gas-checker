# ⛽️ Telegram Gas Checker

Real-time **Ethereum gas tracker** in Telegram.  
Users choose how often to receive gas price updates and set a custom low-gas alert.

---

## 🌟 Features
- `/start` – choose update interval: **30 sec / 1 min / 10 min**
- `/gas` – get current gas price instantly
- `/threshold` – set custom low-gas alert (in Gwei)
- `/alert` – enable or disable alerts  
- Clean inline buttons and fully async logic (aiogram v3)

---

## 📂 Project structure
```bash
Telegram-gas-checker/
│
├── .env.example        # example environment variables
├── requirements.txt    # dependencies
├── main.py             # entry point
│
├── bot/
│   ├── init.py     # setup & scheduler start
│   ├── handlers.py     # commands and inline buttons
│   ├── scheduler.py    # periodic gas checks
│   └── utils.py        # RPC call to Ethereum
│
└── config/
└── settings.py     # load env & global settings
```

---

## ⚡️ Quick start
1. **Clone and enter project**
   ```bash
   git clone https://github.com/yourname/Telegram-gas-checker.git
   cd Telegram-gas-checker
    ```
2.	**Install dependencies**
    ```bash
    python3 -m pip install -r requirements.txt
     ```
3.	**Configure environment**
    ```bash
    cp .env.example .env
    nano .env
    ```

    **Fill in:**

    ```bash
    BOT_TOKEN=your_telegram_bot_token
    RPC_URL=https://mainnet.infura.io/v3/your_project_id
    ALERT_THRESHOLD=20
    CHECK_INTERVAL=60
    ```

4.	**Run bot**

    ```bash
    python3 main.py
    ```