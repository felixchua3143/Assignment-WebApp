from flask import Flask, render_template,request, redirect, url_for
from Forms import CreateGraphForm
import shelve

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/calculator.html')
def cal_load():
    return render_template("calculator.html")


@app.route('/graph.html', methods=["GET", "POST"])
def create_graph():
    create_graph_form = CreateGraphForm(request.form)
    if request.method == "POST" and create_graph_form.validate():
        graph_dict = {}
        db = shelve.open("graph.db", "c")

        try:
            graph_dict = db["Graphs"]
        except:
            print("Error in retrieving Graph from graph.db")

        graph = (create_graph_form.date, create_graph_form.value)
        graph_dict[graph.get_graph_id()] = graph
        db["Graphs"] = graph_dict

    return render_template("graph.html", form = create_graph_form)


if __name__ == '__main__':
    app.run(debug=True)
