from flask import Flask, render_template, request, redirect, url_for
from Forms import CarbonCalForm
import shelve, User, carbon_cal

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carbon_cal.html', methods=["GET", "POST"])
def create_cal():
    create_cal_form = CarbonCalForm(request.form)
    if request.method == "POST" and create_cal_form.validate():
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
