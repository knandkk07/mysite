#!/usr/bin/env python3
"""
Telegram Username Search Web App
Web-based interface for Telegram username search with deployment support
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'hackingteamx_secure_session_key_2025'

# Enable CORS for mobile compatibility
CORS(app)

# Mobile-friendly configurations
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Valid access codes - secure hex codes
VALID_ACCESS_CODES = {
    '0x34A2C6BCe8c5c4F36955D1cfaDC80909871ac58C': 8660,    # Demo code with balance 8660
    '0x34A2C6BCe8c5c4F36955D1cfaDC80909851ac58C': 0       # Demo code with balance 0
}

class TelegramUserSearch:
    def __init__(self, bot_token=None):
        """
        Demo search functionality
        """
        self.bot_token = bot_token or os.getenv('TELEGRAM_BOT_TOKEN')

    def search_public_info(self, username):
        """
        Demo database se search karta hai
        """
        if username.startswith('@'):
            username = username[1:]

        # User database
        user_database = {
            "riyakhanna1": {
                "username": "👤 @Riyakhanna1",
                "phone": "📱 +917091729147",
                "status": "🟢 Active User",
                "account_type": "👨‍💼 Personal Account",
                "last_seen": "⏰ Recently Active",
                "verification": "✅ Verified Profile",
                "privacy_level": "🔓 Public Profile",
                "search_cost": "💰 ₹30 per search",
                "cost_note": "✅ Search completed successfully",
                "success": True
            },
            "sr_cheat_hack": {
                "username": "👤 @SR_CHEAT_HACK",
                "phone": "📱 +917970421286",
                "status": "🟢 Active User",
                "account_type": "👨‍💼 Personal Account",
                "last_seen": "⏰ Recently Active",
                "verification": "✅ Verified Profile",
                "privacy_level": "🔓 Public Profile",
                "search_cost": "💰 ₹30 per search",
                "cost_note": "✅ Search completed successfully",
                "success": True
            }
        }

        # Check if username exists in database (case insensitive)
        username_lower = username.lower().replace('@', '')
        if username_lower in user_database:
            result = user_database[username_lower].copy()
            return result

        # Default response for other usernames
        return {
            "username": f"👤 @{username}",
            "status": "❌ User not found in database",
            "note": "📵 Phone number information not available",
            "suggestion": "🔍 Please verify username or try another account",
            "privacy_info": "🔒 User may have privacy settings enabled",
            "recommendation": "💡 Try searching for verified public accounts",
            "search_cost": "💰 ₹30 per search",
            "cost_note": "✅ Search completed - Balance deducted",
            "success": True
        }

# Initialize searcher
searcher = TelegramUserSearch()

@app.route('/')
def home():
    """
    Main page - check authentication and redirect appropriately
    """
    if not session.get('authenticated'):
        return redirect(url_for('login_page'))
    return redirect(url_for('dashboard'))

@app.route('/login')
def login_page():
    """
    Login page for authentication
    """
    if session.get('authenticated'):
        return redirect(url_for('home'))
    
    response = app.make_response(render_template('login.html'))
    # Add mobile-friendly headers
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route('/login', methods=['POST'])
def login():
    """
    Handle login authentication
    """
    try:
        data = request.get_json()
        access_code = data.get('access_code', '').strip()

        if access_code in VALID_ACCESS_CODES:
            session['authenticated'] = True
            session['default_balance'] = VALID_ACCESS_CODES[access_code]
            return jsonify({
                'success': True,
                'message': 'Access granted'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Invalid access code. Contact @hackingteamx for assistance.'
            })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Authentication error occurred'
        })

@app.route('/dashboard')
def dashboard():
    """
    Main search dashboard - only accessible after login
    """
    if not session.get('authenticated'):
        session.clear()
        return redirect(url_for('login_page'))
    
    balance = session.get('default_balance', 0)
    response = app.make_response(render_template('index.html', balance=balance))
    # Add mobile-friendly headers
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route('/logout')
def logout():
    """
    Logout and clear session
    """
    session.clear()
    return redirect(url_for('login_page'))

@app.route('/search', methods=['POST'])
def search():
    # Check authentication
    if not session.get('authenticated'):
        return jsonify({
            'error': 'Authentication required',
            'success': False
        }), 401
    """
    Username search API endpoint with professional delay - Cost: ₹30 per search
    """
    import time
    try:
        data = request.get_json()
        username = data.get('username', '').strip()

        if not username:
            return jsonify({
                "error": "Username enter kariye",
                "success": False
            })
        
        # Check balance for search cost (₹30)
        current_balance = session.get('default_balance', 0)
        if current_balance < 30:
            return jsonify({
                "error": "Insufficient balance. You need ₹30 for this search. Please deposit money to continue.",
                "success": False
            })

        # Professional 10-second delay
        time.sleep(10)

        # Search perform karte hain
        searcher = TelegramUserSearch()
        result = searcher.search_public_info(username)
        
        if result and result.get('success'):
            # Deduct ₹30 from balance for successful search
            new_balance = current_balance - 30
            session['default_balance'] = new_balance
            result['new_balance'] = new_balance  # Include new balance in response

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": f"Server error: {str(e)}",
            "success": False
        })

@app.route('/sim-details', methods=['POST'])
def sim_details():
    # Check authentication
    if not session.get('authenticated'):
        return jsonify({
            'error': 'Authentication required',
            'success': False
        }), 401
    """
    SIM owner details API endpoint
    """
    import time
    try:
        data = request.get_json()
        phone_number = data.get('phone_number', '').strip()

        if not phone_number:
            return jsonify({
                "error": "Phone number required",
                "success": False
            })
        
        # SIM search is free - no balance check needed

        # Professional delay
        time.sleep(8)

        # Clean phone number format
        phone_clean = phone_number.replace('+91', '').replace('+', '').replace(' ', '')
        
        # SIM owner details for demo numbers
        if phone_clean == "7091729147":
            return jsonify({
                "phone_numbers": [
                    "📞 918207426355",
                    "📞 917903028438", 
                    "📞 918864033507",
                    "📞 919065717472",
                    "📞 917091729147"
                ],
                "addresses": [
                    "🏘️ S/O Sattar Shah,-,CHHOTI KABRISTAN Bettiah,INDRA CHOWK,Bettiah Bettiah,West Champaran,Bihar,845438",
                    "🏘️ choti,CHHOTI KABRISTAN INDRA CHOWK,BETTIAH BETTIAH ward no 14,ward no 14,BETTIAH BETTIAH WEST CHAMPARAN,BETTIAH,WEST CHAMPARAN,BIHAR,845438"
                ],
                "document_number": "🃏 275339966355",
                "full_name": "👤 Sattar shah",
                "father_name": "👨 Ramtula Shah", 
                "region": "🗺️ VODA BHR&JHR;BIHAR JIO;AIRTEL BHR&JHR;BIHAR VODAFONE",
                "success": True
            })
            
        elif phone_clean == "7970421286":
            return jsonify({
                "phone_numbers": [
                    "📞 918607096821",
                    "📞 919113198403",
                    "📞 919693442577", 
                    "📞 917497099699",
                    "📞 917970421286"
                ],
                "addresses": [
                    "🏘️ 22 village bisi kalan dinara district rohtas,Nawanagar PO,buxar,post office-bisi kalan Nawanagar,Nawanagar,Bhojpur,Buxar,Bihar,802129",
                    "🏘️ S/O Hari Prasan Ram,village-bisi kalan village-bisi kalandinara district-rohtas Nawanagar,NA,post office-bisi kalan,Nawanagar Nawanagar Buxar,NA,Bihar,802129"
                ],
                "document_number": "🃏 661024605582",
                "full_name": "👤 Hari Prasan Ram",
                "father_name": "👨 Shiv Kumar Ram",
                "region": "🗺️ BIHAR JIO;AIRTEL BHR&JHR;JIO BHR&JHR",
                "success": True
            })
            
        else:
            return jsonify({
                "error": "SIM details not found for this number",
                "success": False
            })

    except Exception as e:
        return jsonify({
            "error": f"Server error: {str(e)}",
            "success": False
        })

@app.route('/deposit', methods=['POST'])
def deposit():
    """
    Handle deposit requests with UTR verification
    """
    # Check authentication
    if not session.get('authenticated'):
        return jsonify({
            'error': 'Authentication required',
            'success': False
        }), 401
        
    try:
        data = request.get_json()
        utr = data.get('utr', '').strip()
        amount = data.get('amount', 0)
        
        if not utr:
            return jsonify({
                'error': 'UTR number is required',
                'success': False
            })
        
        if amount not in [60, 90, 120, 900, 1800]:
            return jsonify({
                'error': 'Invalid amount selected',
                'success': False
            })
        
        # Check if UTR is valid (default UTR: 453983442711)
        if utr == '453983442711':
            # Add amount to balance
            current_balance = session.get('default_balance', 0)
            new_balance = current_balance + amount
            session['default_balance'] = new_balance
            
            return jsonify({
                'success': True,
                'message': 'Balance successfully added',
                'new_balance': new_balance,
                'amount_added': amount
            })
        else:
            return jsonify({
                'error': 'Wrong UTR number. Please check your payment and enter the correct UTR.',
                'success': False
            })
            
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}',
            'success': False
        })

@app.route('/health')
def health():
    """
    Health check endpoint for deployment
    """
    return jsonify({
        "status": "healthy",
        "app": "Telegram Username Search Demo",
        "version": "1.0"
    })

def create_app():
    return app

if __name__ == '__main__':
    # Check if running in production
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    
    if os.environ.get('PRODUCTION') == 'true':
        # Production mode with mobile-friendly configuration
        from werkzeug.serving import run_simple
        run_simple('0.0.0.0', port, app, 
                  use_reloader=False, 
                  use_debugger=False, 
                  threaded=True,
                  processes=1)
    else:
        # Development mode with mobile-friendly settings
        app.run(host='0.0.0.0', port=port, debug=debug_mode, threaded=True)