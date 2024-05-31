from flask import render_template, request, redirect, url_for, current_app as app
from .email import send_contact_message


templates = {
    'template1': 'template1.html',
}

@app.route('/')
def landing_page():
    return render_template(templates['template1'])


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    send_contact_message(name, email, message)
    print(f"Received message from {name} ({email}): {message}")
    return redirect(url_for('landing_page'))
