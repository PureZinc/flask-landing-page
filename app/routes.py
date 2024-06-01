from flask import render_template, request, redirect, url_for, current_app as app
from .email import send_contact_message


templates = {
    '1': 'template1.html',
}

landing_pages = [
    {
        'name': 'the_SuperMarket',
        'template': '1'
    },
]


@app.route('/')
def pages():
    return render_template('lists.html', pages=landing_pages)


@app.route('/<template>')
def landing_page(template):
    if template in templates:
        return render_template(templates[template])
    else:
        return "Template not found", 404


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    send_contact_message(name, email, message)
    print(f"Received message from {name} ({email}): {message}")
    return redirect(url_for('landing_page'))
