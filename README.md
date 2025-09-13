# Telegram Username Search Web Application

## Quick Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python run.py
```
Or for production:
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### 3. Access the App
Open your browser and go to: `http://localhost:5000`

## Demo Access Codes
- **Code 1**: `C93B8E7A2F4D6E1B9A5C3D7F8E2A4B6C9D1E3F7A9B5C` (₹8660 balance)
- **Code 2**: `A1B2C3D4E5F6789012345678901234567890ABCDEF12` (₹0 balance)

## Demo Search Data
- **Username**: `riyakhanna1` or `sr_cheat_hack`
- **Phone Numbers**: `7091729147` or `7970421286`
- **Valid UTR**: `453983442711`

## Deployment
- **Heroku**: Use Procfile (included)
- **Railway**: Use runtime.txt (included)
- **PythonAnywhere**: Upload files and run app.py
- **Vercel**: Use run.py as entry point

## Features
- Secure access portal with hex-based authentication
- Username search with phone number extraction
- SIM owner details lookup (free after username search)
- QR code payment integration
- UTR verification system
- Professional dark theme UI
- Mobile responsive design

## Developer Contact
For access codes and support: `t.me/@hackingteamx`