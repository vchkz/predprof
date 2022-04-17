from flask import Flask, render_template, request, redirect, make_response
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg
from dataBase import *
import cv2 as cv

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








@app.route('/plot')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

if __name__ == '__main__':
    app.run(debug=True)