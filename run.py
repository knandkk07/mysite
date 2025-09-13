#!/usr/bin/env python3
"""
Telegram Username Search Web Application
Production-ready launcher script
"""

import os
from app import app

if __name__ == '__main__':
    # Get port from environment or default to 5000
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    # Run the Flask application
    app.run(
        host=host,
        port=port,
        debug=False  # Set to False for production
    )