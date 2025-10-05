# 🚀 Deployment Guide

This guide will help you deploy your Movie Provider Bot to various platforms.

## 📋 Prerequisites

Before deploying, make sure you have:

1. **Telegram Bot Token** - Get from [@BotFather](https://t.me/BotFather)
2. **Telegram API Credentials** - Get from [my.telegram.org](https://my.telegram.org/apps)
3. **MongoDB Database** - Get from [MongoDB Atlas](https://www.mongodb.com/atlas)
4. **GitHub Account** - For repository hosting

## 🔧 Environment Variables

Set these environment variables in your deployment platform:

### Required Variables
```bash
BOT_TOKEN=8342816692:AAE9hsbZ7DU3tcCko08rXJWior0m9ruWlF4
API_ID=27507157
API_HASH=8c1121dfa9159420a3c9276a1dc00c53
DATABASE_URI=mongodb+srv://filmadda:AhqzPphdF6e7AwEK@cluster0.bggihn4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
ADMINS=5547390021
CHANNELS=-1002558927719
INDEX_REQ_CHANNEL=-1002558927719
FILE_STORE_CHANNEL=-1002558927719
LOG_CHANNEL=-1002558927719
```

### Optional Variables
```bash
SHORTLINK_URL=arlinks.in
SHORTLINK_API=b0a9ac72d3e476a2fe0a3c166376f4b71ade1644
STREAM_SITE=papajiurl.com
STREAM_API=77960489f7791283414e359c32475f1f07e0fdd3
PICS=https://telegra.ph/file/2e14c61c67f0ab9951b89.jpg
```

## 🌐 Deployment Options

### 1. Heroku Deployment

#### Step 1: Prepare for Heroku
```bash
# Create Procfile
echo "worker: python bot.py" > Procfile

# Create runtime.txt
echo "python-3.11.0" > runtime.txt
```

#### Step 2: Deploy to Heroku
1. Go to [Heroku](https://heroku.com)
2. Create new app
3. Connect GitHub repository
4. Set environment variables
5. Enable worker dyno
6. Deploy

#### Step 3: Heroku Commands
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-bot-name

# Set environment variables
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set API_ID=your_api_id
heroku config:set API_HASH=your_api_hash
heroku config:set DATABASE_URI=your_mongodb_uri

# Deploy
git push heroku main

# Scale worker
heroku ps:scale worker=1
```

### 2. Railway Deployment

#### Step 1: Prepare for Railway
```bash
# Create railway.json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python bot.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

#### Step 2: Deploy to Railway
1. Go to [Railway](https://railway.app)
2. Connect GitHub
3. Select repository
4. Set environment variables
5. Deploy

### 3. VPS Deployment

#### Step 1: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3 python3-pip -y

# Install Git
sudo apt install git -y

# Install screen (for background running)
sudo apt install screen -y
```

#### Step 2: Deploy Bot
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/movie-provider-bot.git
cd movie-provider-bot

# Install dependencies
pip3 install -r requirements.txt

# Create environment file
nano .env
# Add your environment variables

# Run bot in screen
screen -S bot
python3 bot.py
# Press Ctrl+A then D to detach
```

#### Step 3: Auto-start on Boot
```bash
# Create systemd service
sudo nano /etc/systemd/system/movie-bot.service
```

Add this content:
```ini
[Unit]
Description=Movie Provider Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/movie-provider-bot
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl enable movie-bot.service
sudo systemctl start movie-bot.service
sudo systemctl status movie-bot.service
```

### 4. Docker Deployment

#### Step 1: Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

#### Step 2: Create docker-compose.yml
```yaml
version: '3.8'

services:
  movie-bot:
    build: .
    environment:
      - BOT_TOKEN=${BOT_TOKEN}
      - API_ID=${API_ID}
      - API_HASH=${API_HASH}
      - DATABASE_URI=${DATABASE_URI}
      - ADMINS=${ADMINS}
      - CHANNELS=${CHANNELS}
    restart: unless-stopped
```

#### Step 3: Deploy with Docker
```bash
# Build and run
docker-compose up -d

# Check logs
docker-compose logs -f
```

## 🔍 Monitoring & Maintenance

### Health Checks
```bash
# Check bot status
curl -f http://localhost:8080/health || exit 1

# Check logs
tail -f bot.log
```

### Backup Strategy
```bash
# Backup database
mongodump --uri="your_mongodb_uri" --out=backup/

# Backup files
tar -czf backup-$(date +%Y%m%d).tar.gz /path/to/bot/
```

### Updates
```bash
# Pull latest changes
git pull origin main

# Restart bot
sudo systemctl restart movie-bot.service
```

## 🛠️ Troubleshooting

### Common Issues

1. **Bot not starting**
   - Check environment variables
   - Verify database connection
   - Check logs for errors

2. **Database connection failed**
   - Verify MongoDB URI
   - Check network connectivity
   - Verify database credentials

3. **Memory issues**
   - Increase server RAM
   - Optimize database queries
   - Use connection pooling

### Logs Location
- **Heroku**: `heroku logs --tail`
- **Railway**: Dashboard logs
- **VPS**: `/var/log/movie-bot.log`
- **Docker**: `docker logs container_name`

## 📞 Support

If you encounter any issues:

1. Check the logs
2. Verify environment variables
3. Test database connection
4. Check bot permissions
5. Contact support

---

**Happy Deploying! 🚀**
