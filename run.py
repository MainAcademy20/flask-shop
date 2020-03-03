from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from controllers import get_all_products, insert_item
from models import User

app = Flask('shop-app')


def app_init(a):
    a.config['SECRET_KEY'] = 'asdgasdfasdfasdfasdfSDGDGADSFGAFDG'
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_or_none(user_id)

    return a


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    u = current_user
    if request.method == 'POST':
        user, passw = request.form.get('username'), request.form.get('password')
        if u.is_anonymous:
            new_u = User.get_or_none(username=user)
            if new_u:
                if check_password_hash(new_u.password, passw):
                    login_user(new_u)
                    return redirect(url_for('index'))
                else:
                    return render_template('login.html', msg='Invalid password')
            new_u = User.create(username=user, password=generate_password_hash(passw))
            login_user(new_u)

        return redirect(url_for('index'))
    if u.is_authenticated:
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    items = get_all_products()
    return render_template('index.html', products=items)


@app.route('/create-item')
def create_item():
    name = request.args['item_name']
    price = request.args['item_price']
    insert_item(name, price)
    return redirect('/')


if __name__ == '__main__':
    a = app_init(app)
    a.run(debug=True, port=8888)