from flask import render_template, request, redirect, url_for, current_app as app
from .email import send_contact_message


landing_pages = {
    'the-supermarket' : {
        'name': 'The Supermarket',
        'template': 'template1.html'
    },
    'digital-agents' : {
        'name': 'Digital Agents',
        'template': 'template2.html'
    },
    'front-saas' : {
        'name': 'Front SaaS',
        'template': 'template3.html'
    },
}


@app.route('/')
def pages():
    return render_template('lists.html', landing_pages=landing_pages.items())


@app.route('/<slug>')
def landing_page(slug):
    if slug in landing_pages.keys():
        return render_template('spas/' + landing_pages[slug]['template'])
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
