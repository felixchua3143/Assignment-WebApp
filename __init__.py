from flask import Flask, render_template, request, redirect, url_for
# from Forms import CreateUserForm
# import shelve, User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/')
def carbon_cal():
    return render_template('carbon_cal.html')


if __name__ == '__main__':
    app.run()

