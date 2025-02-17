import carbon_cal
import os
import shelve

from flask import Flask, Blueprint, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField, IntegerField, FileField, FloatField, validators
from User import User
from Forms import CarbonCalForm

views = Blueprint('views', __name__)

DATABASE_FILE = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

users = [
    {'email': 'admin@gmail.com', 'password': 'admin', 'is_admin': True},
    {'email': 'user@example.com', 'password': 'user123', 'is_admin': False}
]

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

with shelve.open('products_shelve.db', writeback=True) as products_db:
    if 'products' not in products_db:
        products_db['products'] = {}


class CreateProductForm(FlaskForm):
    product_name = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    product_description = StringField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    product_img = FileField('Product Image', [validators.DataRequired()])
    stock_amt = IntegerField('Amount of Stock', [validators.DataRequired()])
    product_price = FloatField('Price', [validators.DataRequired()])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'user' in session and not session['user']['is_admin']:
        return render_template('home.html')
    return redirect(url_for('index'))  # Admins cannot access home page


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Add new user (In real apps, you should store in a database)
        users.append({'email': email, 'password': password, 'is_admin': False})
        return redirect(url_for('index'))
    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = next((u for u in users if u['email'] == email and u['password'] == password), None)

    if user:
        session['user'] = user
        if user['is_admin']:
            return redirect(url_for('database'))  # Admin (employee) goes to database page
        else:
            return redirect(url_for('home'))  # Regular user goes to home page
    else:
        return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'user' in session and not session['user']['is_admin']:
        return render_template('profile.html', user=session['user'])
    return redirect(url_for('index'))  # Admins cannot access profile pag



@app.route('/logout')
def logout():
    session.pop('user', None)  # Clear the user session
    return redirect(url_for('index'))  # Redirect to login page


@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user' in session:
        users.remove(session['user'])
        session.pop('user', None)
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user' in session and not session['user']['is_admin']:
        session['user']['email'] = request.form['email']
        session['user']['password'] = request.form['password']
        return redirect(url_for('profile'))
    return redirect(url_for('index'))  # Admins cannot update profile

@app.route('/database')
def database():
    if 'user' in session and session['user']['is_admin']:
        return render_template('database.html', users=users)
    return redirect(url_for('index'))  # Non-admins cannot access the database page

@app.route('/create', methods=['GET', 'POST'])
def create_product():
    form = CreateProductForm()
    if form.validate_on_submit():
        file = request.files['product_img']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            with shelve.open('products_shelve.db', writeback=True) as products_db:
                if 'products' not in products_db:
                    products_db['products'] = {}
                new_product_id = max(products_db['products'].keys(), default=0) + 1
                products_db['products'][new_product_id] = {
                    'id': new_product_id,
                    'name': form.product_name.data,
                    'description': form.product_description.data,
                    'image': filename,
                    'stock': form.stock_amt.data,
                    'price': form.product_price.data
                }
                products_db.sync()
            return redirect(url_for('list_products'))
    return render_template('create_product.html', form=form)


class EditDescriptionForm(FlaskForm):
    product_description = StringField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])


@app.route('/products', methods=['GET', 'POST'])
def list_products():
    form = EditDescriptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        product_id = int(request.form['product_id'])
        new_description = form.product_description.data
        with shelve.open('products_shelve.db', writeback=True) as products_db:
            if product_id in products_db['products']:
                products_db['products'][product_id]['description'] = new_description
                products_db.sync()
        return redirect(url_for('list_products'))

    with shelve.open('products_shelve.db') as products_db:
        products = [product for product in products_db.get('products', {}).values() if product['stock'] > 0]
    return render_template('product_list.html', products=products, form=form)


@app.route('/product/<int:product_id>')
def product(product_id):
    try:
        with shelve.open('products_shelve.db') as products_db:
            product = products_db['products'].get(product_id)
        return render_template('product.html', product=product)
    except EOFError:
        return "Stock is empty"


@app.route('/purchase')
def purchase_page():
    try:
        with shelve.open('products_shelve.db') as products_db:
            products = [product for product in products_db.get('products', {}).values() if product['stock'] > 0]
        return render_template('purchase_page.html', products=products)
    except EOFError:
        return "Stock is empty"


@app.route('/purchase/<int:product_id>', methods=['GET', 'POST'])
def purchase_product(product_id):
    error = None
    try:
        with shelve.open('products_shelve.db', writeback=True) as products_db:
            product = products_db['products'].get(product_id)
            if request.method == 'POST':
                quantity = int(request.form['quantity'])
                if quantity <= product['stock']:
                    product['stock'] -= quantity
                    if product['stock'] <= 0:
                        del products_db['products'][product_id]
                    products_db.sync()
                    return redirect(url_for('purchase_page'))
                else:
                    error = "Not enough stock available."
        return render_template('product.html', product=product, error=error)
    except EOFError:
        return "Stock is empty"


@app.route('/delete_stock/<int:product_id>', methods=['POST'])
def delete_stock(product_id):
    try:
        with shelve.open('products_shelve.db', writeback=True) as products_db:
            product = products_db['products'].get(product_id)
            quantity = int(request.form['quantity'])
            if quantity <= product['stock']:
                product['stock'] -= quantity
                if product['stock'] <= 0:
                    del products_db['products'][product_id]
                products_db.sync()
                return redirect(url_for('list_products'))
            else:
                error = "Not enough stock available."
                return redirect(url_for('list_products', error=error))
    except EOFError:
        return "Error: Shelve database is empty or corrupted."


@app.route('/delete_all_stock/<int:product_id>', methods=['POST'])
def delete_all_stock(product_id):
    try:
        with shelve.open('products_shelve.db', writeback=True) as products_db:
            del products_db['products'][product_id]
        return redirect(url_for('list_products'))
    except EOFError:
        return "Error: Shelve database is empty or corrupted."


@app.route('/carbon_cal.html', methods=["GET", "POST"])
def create_cal():
    create_cal_form = CarbonCalForm(request.form)
    if request.method == "POST":
        carbon_dict = {}
        db = shelve.open('carbon.db', 'c')

        try:
            carbon_dict = db['Carbon']
        except:
            print("Error in retrieving data from carbon.db.")

        carbon = carbon_cal.Carbon_Cal(create_cal_form.get_username().data, create_cal_form.electricity.data,
                                       create_cal_form.gas.data,
                                       create_cal_form.water.data, create_cal_form.num_household.data)
        carbon_dict[carbon.get_id()] = carbon
        db["Carbon"] = carbon_dict

        db.close()
        return redirect(url_for("create_cal"))
    return render_template("carbon_cal.html", form=create_cal_form)


@app.route('/carbon_cal_food.html', methods=["GET", "POST"])
def create_cal_food():
    create_cal_form = CarbonCalForm(request.form)
    if request.method == "POST" and create_cal_form.validate():
        return redirect(url_for("create_cal"))
    return render_template('carbon_cal_food.html', form=create_cal_form)


@app.route('/carbon_cal_spendings.html', methods=["GET", "POST"])
def create_cal_spendings():
    create_cal_form = CarbonCalForm(request.form)
    if request.method == "POST" and create_cal_form.validate():
        return redirect(url_for("create_cal"))
    return render_template('carbon_cal_spendings.html', form=create_cal_form)


if __name__ == '__main__':
    app.run(debug=True)
