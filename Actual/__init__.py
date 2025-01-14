from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',  methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/calculator.html')
def cal_load():
    return render_template("calculator.html")

@app.route('/graph.html')
def graph_load():
    return render_template("graph.html")


if __name__ == '__main__':
    app.run(debug=True)