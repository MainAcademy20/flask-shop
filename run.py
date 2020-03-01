from flask import Flask, render_template, request, redirect, url_for, Response
from flask_login import LoginManager, AnonymousUserMixin, current_user, login_user

from controllers import get_all_products, insert_item, exists_user
from models import User

app = Flask('shop-app')


def app_init(a):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_or_none(user_id)

    return a

#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         user, password = request.form['user'], request.form['password']
#         if exists_user(user):
#             return render_template('register.html', msg='Username already taken')
#
#         register_user(user, password)
#         return Response(status=302, headers={
#             'Location': url_for('index'),
#             'Set-Cookie': 'username={}'.format(user)
#         })
#         return redirect(url_for('index'))

    # return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    u = current_user
    if request.method == 'POST':
        user, passw = request.form.get('username'), request.form.get('password')
        if u.is_anonymous:
            new_u = User.create(username=user, password=passw)
            login_user(new_u)
        return redirect(url_for('index'))
    if u.is_authenticated:
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/')
def index():
    # if exists_user(username):/
    items = get_all_products()
    return render_template('index.html', products=items)
    # return render_template('unauthorized.html')


@app.route('/create-item')
def create_item():
    name = request.args['item_name']
    price = request.args['item_price']
    insert_item(name, price)
    return redirect('/')


if __name__ == '__main__':
    a = app_init(app)
    a.run(debug=True, port=8888)