#!/usr/bin/env python3
"""
Movie Provider Bot Setup Script
This script helps you set up the bot with all necessary configurations.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def print_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🎬 MOVIE PROVIDER BOT                    ║
    ║                        Setup Script                         ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required. Current version:", sys.version)
        sys.exit(1)
    print("✅ Python version:", sys.version.split()[0])

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def create_env_file():
    """Create .env file with template"""
    env_content = """# Movie Provider Bot Configuration
# Copy this file and fill in your actual values

# Bot Configuration
BOT_TOKEN=your_bot_token_here
API_ID=your_api_id_here
API_HASH=your_api_hash_here

# Database Configuration
DATABASE_URI=your_mongodb_uri_here
DATABASE_NAME=filmadda

# Admin Configuration
ADMINS=your_admin_id_here
CHANNELS=your_channel_id_here

# Index Channel Configuration
INDEX_REQ_CHANNEL=your_index_channel_id_here
FILE_STORE_CHANNEL=your_file_store_channel_id_here
LOG_CHANNEL=your_log_channel_id_here

# Optional Configuration
SHORTLINK_URL=arlinks.in
SHORTLINK_API=your_shortlink_api_here
STREAM_SITE=papajiurl.com
STREAM_API=your_stream_api_here

# Images
PICS=https://telegra.ph/file/2e14c61c67f0ab9951b89.jpg
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Created .env template file")
    else:
        print("ℹ️  .env file already exists")

def create_config_template():
    """Create info.py template"""
    if not os.path.exists('info.py.example'):
        print("✅ Creating info.py.example template...")
        # Copy current info.py as template
        with open('info.py', 'r') as f:
            content = f.read()
        
        # Replace actual values with placeholders
        content = content.replace('"8342816692:AAE9hsbZ7DU3tcCko08rXJWior0m9ruWlF4"', '"your_bot_token_here"')
        content = content.replace('27507157', 'your_api_id_here')
        content = content.replace('"8c1121dfa9159420a3c9276a1dc00c53"', '"your_api_hash_here"')
        
        with open('info.py.example', 'w') as f:
            f.write(content)
        print("✅ Created info.py.example template")

def setup_git():
    """Initialize git repository"""
    if not os.path.exists('.git'):
        print("\n🔧 Setting up Git repository...")
        try:
            subprocess.check_call(['git', 'init'])
            subprocess.check_call(['git', 'add', '.'])
            subprocess.check_call(['git', 'commit', '-m', 'Initial commit: Movie Provider Bot'])
            print("✅ Git repository initialized")
        except subprocess.CalledProcessError:
            print("⚠️  Git not found. Please install Git to use version control")
    else:
        print("ℹ️  Git repository already exists")

def create_directories():
    """Create necessary directories"""
    directories = ['logs', 'temp', 'backup']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✅ Created necessary directories")

def check_requirements():
    """Check if all requirements are met"""
    print("\n🔍 Checking requirements...")
    
    # Check if info.py exists
    if not os.path.exists('info.py'):
        print("❌ info.py not found. Please create it from info.py.example")
        return False
    
    # Check if bot.py exists
    if not os.path.exists('bot.py'):
        print("❌ bot.py not found")
        return False
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        return False
    
    print("✅ All requirements met")
    return True

def show_next_steps():
    """Show next steps to the user"""
    print("""
    🎉 Setup completed successfully!
    
    📋 Next Steps:
    
    1. 📝 Configure your bot:
       - Edit info.py with your actual credentials
       - Or use .env file for environment variables
    
    2. 🚀 Run the bot:
       python bot.py
    
    3. 🌐 Deploy to cloud:
       - Heroku: Follow DEPLOYMENT.md
       - Railway: Connect GitHub repository
       - VPS: Use setup script on server
    
    4. 📚 Documentation:
       - README.md: Complete documentation
       - DEPLOYMENT.md: Deployment guide
    
    5. 🔧 Development:
       - Add features in plugins/ directory
       - Test thoroughly before deploying
    
    🆘 Need help?
    - Check logs in logs/ directory
    - Read documentation
    - Open GitHub issues
    
    Happy coding! 🚀
    """)

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    check_python_version()
    
    # Check requirements
    if not check_requirements():
        print("❌ Setup failed. Please fix the issues above.")
        sys.exit(1)
    
    # Install dependencies
    install_dependencies()
    
    # Create environment file
    create_env_file()
    
    # Create config template
    create_config_template()
    
    # Setup git
    setup_git()
    
    # Create directories
    create_directories()
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main()
