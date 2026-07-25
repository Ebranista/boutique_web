"""
Flask Application Entry Point
"""
import os
from app import create_app

# Load environment variables
os.environ.setdefault('FLASK_ENV', 'development')

# Create Flask application
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
