
# Configuración de producción para CallTech
import os

class ProductionConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'calltech-production-key-2024'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///calltech_production.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    
    # Configuración para servidor web
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 8080))
