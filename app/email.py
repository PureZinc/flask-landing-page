from flask_mail import Mail, Message
from .models import Contact, Subscriber, db
from config import config


mail = Mail()
username = config['MAIL_USERNAME']


def send_contact_message(name, email, message):
    new_contact = Contact(name=name, email=email, message=message)
    db.session.add(new_contact)
    new_sub = Subscriber(name=name, email=email)
    db.session.add(new_sub)
    db.session.commit()


    msg = Message(
        f'New Contact From {email}',
        sender=username,
        recipients=[username]
    )
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    