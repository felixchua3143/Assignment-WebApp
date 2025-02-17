import carbon_cal
import os
import shelve

from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField, IntegerField, FileField, FloatField, validators
from Forms import CarbonCalForm

DATABASE_FILE = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
DB_PATH = 'user_data.db'
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


def get_db():
    return shelve.open(DB_PATH, writeback=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with get_db() as db:
            # Check if it's the admin login
            if username == 'admin@gmail.com' and password == 'admin':
                session['user'] = username
                return redirect(url_for('database'))  # Redirect to database page for admin

            # Check for regular user login
            elif username in db and db[username]['password'] == password:
                session['user'] = username
                return redirect(url_for('profile'))

            else:
                flash('Invalid credentials')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(password) < 8:
            flash('Password must be at least 8 characters long')
            return redirect(url_for('signup'))

        with get_db() as db:
            if username in db:
                flash('Username already exists')
                return redirect(url_for('signup'))
            db[username] = {'password': password}
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))

    username = session['user']

    if request.method == 'POST':
        new_password = request.form['new_password']
        if len(new_password) < 8:
            flash('Password must be at least 8 characters long')
            return redirect(url_for('profile'))

        with get_db() as db:
            db[username]['password'] = new_password
        flash('Password updated successfully')

    return render_template('profile.html', username=username)


@app.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user' not in session:
        return redirect(url_for('login'))

    username = session['user']

    with get_db() as db:
        del db[username]

    session.pop('user', None)
    flash('Account deleted successfully')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/database')
def database_page():
    if 'user' not in session or session['user'] != 'admin@gmail.com':
        return redirect(url_for('login'))

    db = get_db()  # Open the shelf database
    users = db.items()  # Get users from the opened database

    return render_template('database.html', users=users)


@app.route('/update_password/<username>', methods=['GET','POST'])
def update_password(username):
    if 'user' not in session or session['user'] != 'admin@gmail.com':
        return redirect(url_for('login'))

    new_password = request.form['new_password']
    if len(new_password) < 8:
        flash('Password must be at least 8 characters long')
        return redirect(url_for('database_page'))

    with get_db() as db:
        db[username]['password'] = new_password

    flash(f'Password for {username} updated successfully')
    return redirect(url_for('database_page'))


@app.route('/delete_user/<username>', methods=['GET','POST'])
def delete_user(username):
    if 'user' not in session or session['user'] != 'admin@gmail.com':
        return redirect(url_for('login'))

    with get_db() as db:
        del db[username]

    flash(f'User {username} deleted successfully')
    return redirect(url_for('database_page'))


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

@app.route('/feedback.html', methods=['GET', 'POST'])
def feedback_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']

        feedback_dict = get_shelve_data('feedback.db', 'Feedback')
        feedback_id = len(feedback_dict) + 1
        feedback_dict[feedback_id] = Forms.Feedback(name, email, feedback).to_dict()
        save_shelve_data('feedback.db', 'Feedback', feedback_dict)

        return render_template('success.html', message="Feedback submitted successfully!")
    return render_template('feedback.html')

@app.route('/retrieveFeedback')
def retrieve_feedback():
    feedback_dict = get_shelve_data('feedback.db', 'Feedback')
    feedback_list = [{"id": key, **feedback_dict[key]} for key in feedback_dict]
    return render_template('retrieveFeedback.html', feedback_list=feedback_list)

@app.route('/updateFeedback/<int:id>', methods=['GET', 'POST'])
def update_feedback(id):
    feedback_dict = get_shelve_data('feedback.db', 'Feedback')
    feedback = feedback_dict.get(id)

    if request.method == 'POST':
        feedback['name'] = request.form['name']
        feedback['email'] = request.form['email']
        feedback['feedback'] = request.form['feedback']
        feedback_dict[id] = feedback
        save_shelve_data('feedback.db', 'Feedback', feedback_dict)
        return redirect(url_for('retrieve_feedback'))

    return render_template('updateFeedback.html', feedback=feedback, id=id)

@app.route('/deleteFeedback/<int:id>', methods=['POST'])
def delete_feedback(id):
    feedback_dict = get_shelve_data('feedback.db', 'Feedback')
    feedback_dict.pop(id, None)
    save_shelve_data('feedback.db', 'Feedback', feedback_dict)
    return redirect(url_for('retrieve_feedback'))

# Review CRUD
@app.route('/review', methods=['GET', 'POST'])
def review_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        product_name = request.form['product_name']
        review = request.form['review']
        rating = request.form['rating']

        review_dict = get_shelve_data('review.db', 'Review')
        review_id = len(review_dict) + 1
        review_dict[review_id] = Forms.Review(name, email, product_name, review, rating).to_dict()
        save_shelve_data('review.db', 'Review', review_dict)

        return render_template('success.html', message="Review submitted successfully!")
    return render_template('review.html')

@app.route('/retrieveReview')
def retrieve_review():
    review_dict = get_shelve_data('review.db', 'Review')
    if not review_dict:
        review_dict = {}
    review_list = [{"id": key, **review_dict[key]} for key in review_dict]
    return render_template('retrieveReviews.html', review_list=review_list)
def get_shelve_data(db_name, key):
    with shelve.open(db_name, 'c') as db:
        if key not in db:
            db[key] = {}
        return db[key]

def save_shelve_data(db_name, key, data):
    with shelve.open(db_name, 'c')as db:
        db[key] = data



    @app.route('/updateReview/<int:id>', methods=['GET', 'POST'])
    def update_review(id):
        review_dict = get_shelve_data('review.db', 'Review')
        review = review_dict.get(id)

        if request.method == 'POST':
            review['name'] = request.form['name']
            review['email'] = request.form['email']
            review['product_name'] = request.form['product_name']
            review['review'] = request.form['review']
            review['rating'] = request.form['rating']
            review_dict[id] = review
            save_shelve_data('review.db', 'Review', review_dict)
            return redirect(url_for('retrieve_review'))

        return render_template('updateReview.html', review=review, id=id)

    @app.route('/deleteReview/<int:id>', methods=['POST'])
    def delete_review(id):
        review_dict = get_shelve_data('review.db', 'Review')
        review_dict.pop(id, None)
        save_shelve_data('review.db', 'Review', review_dict)
        return redirect(url_for('retrieve_review'))

        # Support CRUD
    @app.route('/support', methods=['GET', 'POST'])
    def support_form():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            issue = request.form['issue']

            support_dict = get_shelve_data('support.db', 'Support')
            support_id = len(support_dict) + 1
            support_dict[support_id] = Forms.Support(name, email, issue).to_dict()
            save_shelve_data('support.db', 'Support', support_dict)

            return render_template('success.html', message="Support request submitted successfully!")
        return render_template('support.html')

    @app.route('/retrieveSupport')
    def retrieve_support():
        support_dict = get_shelve_data('support.db', 'Support')
        support_list = [{"id": key, **support_dict[key]} for key in support_dict]
        return render_template('retrieveSupport.html', support_list=support_list)

    @app.route('/updateSupport/<int:id>', methods=['GET', 'POST'])
    def update_support(id):
        support_dict = get_shelve_data('support.db', 'Support')
        support = support_dict.get(id)

        if request.method == 'POST':
            support['name'] = request.form['name']
            support['email'] = request.form['email']
            support['issue'] = request.form['issue']
            support_dict[id] = support
            save_shelve_data('support.db', 'Support', support_dict)
            return redirect(url_for('retrieve_support'))

        return render_template('updateSupport.html', support=support, id=id)

    @app.route('/deleteSupport/<int:id>', methods=['POST'])
    def delete_support(id):
        support_dict = get_shelve_data('support.db', 'Support')
        support_dict.pop(id, None)
        save_shelve_data('support.db', 'Support', support_dict)
        return redirect(url_for('retrieve_support'))

    def get_shelve_data( db_name, key):
        db = shelve.open(db_name, 'c')
        if key not in db:
            db[key] = {}
        data = db[key]
        db.close()
        return data

    def save_shelve_data(db_name, key, data):
        db = shelve.open(db_name, 'c')
        db[key] = data
        db.close()



if __name__ == '__main__':
    app.run()
