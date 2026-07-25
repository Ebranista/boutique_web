"""
Create Database Tables
"""
import os
from dotenv import load_dotenv

# Load environment variables explicitly
load_dotenv()

# Debug: Print environment variables
print(f"DATABASE_USER: {os.getenv('DATABASE_USER')}")
print(f"DATABASE_PASSWORD: {os.getenv('DATABASE_PASSWORD')}")
print(f"DATABASE_HOST: {os.getenv('DATABASE_HOST')}")
print(f"DATABASE_PORT: {os.getenv('DATABASE_PORT')}")
print(f"DATABASE_NAME: {os.getenv('DATABASE_NAME')}")

from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    print('Tables created successfully')
