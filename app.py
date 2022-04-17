from flask import Flask, render_template, request, redirect, make_response
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg
from dataBase import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        id_a = request.form['id_a']
        id_d = request.form['id_d']
        intens = request.form['intens']
        k_x = request.form['k_x']
        k_y = request.form['k_y']
        add_anomaly(id_d, id_a, intens, k_x, k_y)
        return redirect('/')

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
