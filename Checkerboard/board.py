

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4')
def four():
    return render_template('four.html')


@app.route('/<x>/<y>')
def lastxy(x,y):
    return render_template('lastxy.html',_x=int(x),_y=int (y))


if __name__=="__main__":
    app.run(debug=True)