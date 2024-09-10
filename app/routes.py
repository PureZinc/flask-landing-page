from flask import render_template, request, redirect, url_for, current_app as app, session
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

# Data Tracking
def create_data_tracking_route(route_name, key_name, key_info: dict={}, redirect_link='/'):    
    @app.route(route_name)
    def tracker():
        session_info = {
            'utm_source': request.args.get('utm_source'),
            'utm_medium': request.args.get('utm_medium'),
            'utm_campaign': request.args.get('utm_campaign'),
            'referrer': request.referrer,
            'user_agent': request.headers.get('User-Agent'),
            'user_ip': request.remote_addr,
        }
        session_info.update(key_info)
        session[key_name] = session_info
        print(session_info)      
        return redirect(redirect_link)

    return tracker

create_data_tracking_route('/testing', 'test')