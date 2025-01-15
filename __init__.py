from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm
import shelve, User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.electricity.data, create_user_form.num_household.data, create_user_form.water.data, create_user_form.gas.data, create_user_form.food.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_electricity(), user.get_num_household(), "was stored in user.db successfully with user_id ==", user.get_user_id())

        db.close()

        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)


if __name__ == '__main__':
    app.run()

