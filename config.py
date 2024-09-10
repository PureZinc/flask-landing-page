# Config for your landing page
import os

config = {
    'SECRET_KEY': os.urandom(24),

    # Database Settings
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///contacts.db',

    # Email Settings
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': 'your_email@example.com',
    'MAIL_PASSWORD': 'your_password'
}

prod_config = {
    'SECRET_KEY': os.environ.get('SECRET_KEY'),

    # Database Settings
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///contacts.db',

    # Cookies Settings
    'SESSION_COOKIE_HTTPONLY': True,  # Prevent JS access to cookies
    'SESSION_COOKIE_SECURE': True,    # Ensure cookies are sent only over HTTPS
    'SESSION_COOKIE_SAMESITE': 'Lax',

    # Email Settings
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': os.environ.get('EMAIL_USERNAME'),
    'MAIL_PASSWORD': os.environ.get('EMAIL_PASSWORD')
}