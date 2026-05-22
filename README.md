# 🚀 Telegram On-Chain Trading Bot

Bot Telegram untuk trading otomatis on-chain dengan sistem skill dinamis dari GitHub (mirip Bankr Bot).

## ✨ Fitur Utama

### 💰 Trading Features
- ✅ **Swap Tokens** - Tukar token langsung on-chain
- ✅ **Limit Orders** - Buat order dengan harga target
- ✅ **Stop Loss & Take Profit** - Manajemen risiko otomatis
- ✅ **DCA (Dollar Cost Averaging)** - Investasi berkala
- ✅ **TWAP (Time-Weighted Avg Price)** - Eksekusi volume besar
- ✅ **Perpetuals** - Trading dengan leverage
- ✅ **Yield Farming** - Deposit ke protokol DeFi
- ✅ **Multi-Chain Support** - Base, Ethereum, Polygon, Solana
- ✅ **Portfolio Management** - Track balance & P&L

### 🧠 Smart Features
- ✅ **Natural Language Commands** - Perintah dalam bahasa natural
- ✅ **AI Trading Strategies** - Rekomendasi otomatis
- ✅ **Copy Trading** - Ikuti trader lain
- ✅ **Smart Wallets** - Non-custodial, aman

### 📦 Skill System
- ✅ **Dynamic Skill Loading** - Pull kode dari GitHub
- ✅ **Skill Marketplace** - Share & discover skills
- ✅ **Skill Verification** - Validasi keamanan
- ✅ **Custom Strategies** - Buat skill sendiri

### 📊 Data & Security
- ✅ **Portfolio Tracking** - Track semua aset
- ✅ **Trade History** - Riwayat transaksi
- ✅ **Wallet Security** - Enkripsi private key
- ✅ **2FA Support** - Authenticator

## 📦 Instalasi

```bash
# Clone repository
git clone https://github.com/herviana/telegram-trading-bot.git
cd telegram-trading-bot

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env dengan config Anda

# Run bot
python main.py
```

## ⚙️ Konfigurasi (.env)

```
# Telegram
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_ADMIN_ID=your_id

# Blockchain
WEB3_PROVIDER_URL=https://mainnet.base.org
PRIVATE_KEY=your_private_key_encrypted

# GitHub (untuk skill loading)
GITHUB_TOKEN=your_github_token
GITHUB_REPO=username/skills-repo

# Database
DATABASE_URL=sqlite:///bot.db

# Trading
DEFAULT_SLIPPAGE=0.5
MAX_GAS_PRICE=100
```

## 🎯 Cara Penggunaan

### 1. Start Bot
```
/start - Inisialisasi wallet
/wallet - Lihat balance
/help - Bantuan lengkap
```

### 2. Trading Commands
```
/swap - Tukar token
/limit - Buat limit order
/stoploss - Set stop loss
/profit - Set take profit
/dca - Dollar cost averaging
```

### 3. Skill Management
```
/skills - Lihat semua skill
/install_skill - Install dari GitHub
/my_skills - Skill yang sudah diinstall
/create_skill - Buat skill baru
```

### 4. Portfolio
```
/portfolio - Lihat semua aset
/pnl - P&L summary
/history - Riwayat trade
/orders - Order aktif
```

## 🏗️ Struktur Project

```
telegram-trading-bot/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── .env.example           # Config template
│
├── bot/
│   ├── __init__.py
│   ├── handlers/          # Command handlers
│   │   ├── trading.py     # Trading commands
│   │   ├── portfolio.py   # Portfolio commands
│   │   ├── skills.py      # Skill commands
│   │   └── wallet.py      # Wallet commands
│   ├── strategies/        # Trading strategies
│   │   ├── dca.py
│   │   ├── limit_order.py
│   │   ├── stop_loss.py
│   │   └── twap.py
│   ├── skills/            # Skill management
│   │   ├── loader.py      # Load dari GitHub
│   │   ├── validator.py   # Validasi skill
│   │   └── marketplace.py # Skill marketplace
│   └── middleware/        # Middleware & utils
│       ├── auth.py        # Authentication
│       ├── logging.py
│       └── error_handler.py
│
├── blockchain/
│   ├── __init__.py
│   ├── web3_client.py     # Web3 interactions
│   ├── dex/
│   │   ├── uniswap.py
│   │   └── curve.py
│   ├── wallet/
│   │   ├── manager.py
│   │   └── encryption.py
│   └── chains/            # Multi-chain support
│       ├── base.py
│       ├── ethereum.py
│       └── polygon.py
│
├── db/
│   ├── __init__.py
│   ├── models.py          # Database models
│   ├── migrations/        # Database migrations
│   └── repositories/      # Data access layer
│       ├── user_repo.py
│       ├── trade_repo.py
│       └── skill_repo.py
│
├── services/
│   ├── trading_service.py
│   ├── portfolio_service.py
│   ├── skill_service.py
│   └── notification_service.py
│
└── tests/
    ├── test_trading.py
    ├── test_wallet.py
    └── test_skills.py
```

## 🔐 Security Features

1. **Encrypted Private Keys** - Private key tersimpan terenkripsi
2. **Rate Limiting** - Cegah spam & brute force
3. **2FA Authentication** - Double factor security
4. **Skill Verification** - Scan kode sebelum eksekusi
5. **Gas Limit Protection** - Lindungi dari gas-griefing
6. **Whitelist Support** - Whitelist wallet penerima

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Docker
```bash
docker build -t trading-bot .
docker run --env-file .env trading-bot
```

## 📚 Documentation

Lihat folder `docs/` untuk dokumentasi lengkap:
- `docs/setup.md` - Panduan setup
- `docs/api.md` - API reference
- `docs/skills.md` - Membuat custom skill
- `docs/deployment.md` - Deployment guide

## 🤝 Contributing

Kontribusi welcome! Baca CONTRIBUTING.md untuk guidelines.

## 📝 License

MIT License - Bebas digunakan untuk keperluan apapun

## 💬 Support & Updates

- 📧 Email: support@example.com
- 💬 Telegram Community: Coming soon
- 📖 Full Docs: Coming soon

## ⚠️ Disclaimer

**RISK WARNING**: Bot ini adalah tools trading otomatis. Gunakan dengan hati-hati:
- ⚠️ Test di testnet terlebih dahulu
- ⚠️ Mulai dengan jumlah kecil
- ⚠️ Monitor aktivitas bot secara berkala
- ⚠️ Developer tidak bertanggung jawab atas kerugian finansial

---

**Versi**: 1.0.0  
**Last Updated**: May 2026  
**Author**: @herviana
