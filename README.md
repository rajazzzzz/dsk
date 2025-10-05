# 🎬 Movie Provider Bot

A powerful Telegram bot for providing movies and files with advanced features like index channel support, auto filtering, and premium membership management.

## ✨ Features

- 🎯 **Index Channel Support** - Connect multiple channels for content
- 🔍 **Auto File Filtering** - Automatic content filtering and organization
- 💎 **Premium Membership** - Premium user management system
- 🔗 **Custom Shortlinks** - Integrated shortlink support
- 📱 **Multi-language Support** - Support for multiple languages
- 🛡️ **Content Protection** - File protection and forward restrictions
- 📊 **Admin Panel** - Complete admin management system
- 🎬 **IMDB Integration** - Movie information and ratings
- 🔄 **Auto Delete** - Automatic file cleanup
- 📈 **Analytics** - User and chat statistics

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MongoDB Database
- Telegram Bot Token
- Telegram API Credentials

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/movie-provider-bot.git
cd movie-provider-bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
# Copy and edit the configuration
cp info.py.example info.py
# Edit info.py with your credentials
```

4. **Run the bot**
```bash
python bot.py
```

## ⚙️ Configuration

### Required Environment Variables

```python
BOT_TOKEN = "your_bot_token_here"
API_ID = "your_api_id"
API_HASH = "your_api_hash"
DATABASE_URI = "your_mongodb_uri"
ADMINS = "admin_user_ids"
CHANNELS = "channel_ids"
INDEX_REQ_CHANNEL = "index_channel_id"
FILE_STORE_CHANNEL = "file_store_channel_id"
```

### Optional Variables

```python
SHORTLINK_URL = "your_shortlink_domain"
SHORTLINK_API = "your_shortlink_api"
STREAM_SITE = "your_streaming_site"
STREAM_API = "your_stream_api"
LOG_CHANNEL = "log_channel_id"
```

## 🎯 Features Overview

### 📱 Bot Commands
- `/start` - Start the bot
- `/connect` - Connect your group
- `/settings` - Bot settings
- `/stats` - Bot statistics
- `/broadcast` - Broadcast messages
- `/ban`/`/unban` - User management

### 🔧 Admin Features
- User management (ban/unban)
- Channel management
- File management
- Premium user management
- Broadcast system
- Analytics and statistics

### 🎬 Content Management
- Auto file filtering
- Content protection
- File storage
- Index channel support
- Multi-language support

## 🚀 Deployment

### Heroku Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/YOUR_USERNAME/movie-provider-bot)

### Railway Deployment
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/YOUR_TEMPLATE_ID)

### VPS Deployment
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/movie-provider-bot.git
cd movie-provider-bot

# Install dependencies
pip install -r requirements.txt

# Run bot
python bot.py
```

## 📊 Database Schema

The bot uses MongoDB with the following collections:
- `users` - User information
- `chats` - Chat information
- `files` - File metadata
- `filters` - Auto filters
- `premium_users` - Premium members

## 🔧 Development

### Project Structure
```
movie-provider-bot/
├── bot.py                 # Main bot file
├── info.py               # Configuration
├── Script.py             # Bot scripts
├── requirements.txt      # Dependencies
├── plugins/              # Bot plugins
│   ├── commands.py
│   ├── filters.py
│   ├── broadcast.py
│   └── ...
├── database/             # Database files
│   ├── users_chats_db.py
│   ├── ia_filterdb.py
│   └── ...
└── util/                 # Utilities
    ├── config_parser.py
    ├── file_properties.py
    └── ...
```

### Adding New Features
1. Create plugin in `plugins/` directory
2. Import in `bot.py`
3. Add configuration if needed
4. Test thoroughly

## 📝 License

This project is licensed under the GNU AGPL 3.0 License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

- **Telegram**: [@YourSupportBot](https://t.me/YourSupportBot)
- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/movie-provider-bot/issues)
- **Documentation**: [Wiki](https://github.com/YOUR_USERNAME/movie-provider-bot/wiki)

## 🙏 Acknowledgments

- [Pyrogram](https://github.com/pyrogram/pyrogram) - Telegram MTProto API client
- [MongoDB](https://www.mongodb.com/) - Database
- [Heroku](https://www.heroku.com/) - Deployment platform

## ⚠️ Disclaimer

This bot is for educational purposes only. Please ensure you comply with all applicable laws and regulations when using this bot.

---

**Made with ❤️ by [Your Name]**