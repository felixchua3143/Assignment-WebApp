from flask import Flask, render_template, request, redirect, url_for
from Forms import CarbonCalForm
import shelve, User, carbon_cal

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carbon_cal.html')
def carbon_cal():
    carbon_cal_form = CarbonCalForm(request.form)
    if request.method == 'POST' and carbon_cal_form.validate():
        carbon_dict = {}
        db = shelve.open('carbon_cal.db', 'c')

        try:
            carbon_dict = db['carbon_cal']
        except:
            print("Error in retrieving data from carbon_cal.db")

        carbon_cal = CarbonCalForm(carbon_cal_form.get_user_id,carbon_cal_form.electricity, carbon_cal_form.gas, carbon_cal_form.water, carbon_cal_form.num_household)
        carbon_dict[CarbonCalForm.get_user_id()] = carbon_cal
        db['carbon_cal'] = carbon_dict

        # Test codes
        carbon_dict = db['carbon_cal']
        CarbonCalForm = carbon_dict[CarbonCalForm.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==",
              user.get_user_id())

        db.close()

        return redirect(url_for('home'))
    return render_template('carbon_cal.html', form=carbon_cal_form)
    return render_template('carbon_cal.html')

if __name__ == '__main__':
    app.run(debug=True)
