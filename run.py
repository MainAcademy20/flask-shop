from flask import Flask, render_template, request, redirect, url_for

from controllers import get_all_products, insert_item, register_user, exists_user

app = Flask('shop-app')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user, password = request.form['user'], request.form['password']
        if exists_user(user):
            return render_template('register.html', msg='Username already taken')

        register_user(user, password)
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/')
def index():
    items = get_all_products()
    return render_template('index.html', products=items)


@app.route('/create-item')
def create_item():
    name = request.args['item_name']
    price = request.args['item_price']
    insert_item(name, price)
    return redirect('/')


app.run(debug=True, port=8888)