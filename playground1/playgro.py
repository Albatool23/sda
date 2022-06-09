


from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home '


@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<num>')
def playx(num):
    return render_template('playx.html',_num=int(num))


@app.route('/play/<num>/<color>')
def playColor(num,color):
    return render_template('playcolor.html',_num=int(num),_color=color)





if __name__=="__main__":
    app.run(debug=True)