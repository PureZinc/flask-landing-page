# Config for your landing page

config = {
    'SECRET_KEY': '<your secret key>',

    # Database Settings
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///contacts.db',

    # Email Settings
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': 'your_email@example.com',
    'MAIL_PASSWORD': 'your_password'
}
