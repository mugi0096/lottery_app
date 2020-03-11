import sys
sys.path.append("/usr/local/lib/python3.7/site-packages")

from flask import Flask, escape, request, render_template
import make_random
from make_random import make_random_n3
from make_random import make_random_n4

app = Flask(__name__)
prob_1000_n4 = make_random.counts_100_probs_n4
prob_100_n4 = make_random.counts_100_probs_n4
prob_10_n4 = make_random.counts_10_probs_n4
prob_1_n4 = make_random.counts_1_probs_n4

prob_100_n3 = make_random.counts_100_probs_n3
prob_10_n3 = make_random.counts_10_probs_n3
prob_1_n3 = make_random.counts_1_probs_n3

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/n3')
def display_number_n3():
    img_100 = 'static/src/0.png'
    img_10 = 'static/src/0.png'
    img_1 = 'static/src/0.png'
    res = render_template("numbers3.html", img_100=img_100, img_10=img_10, img_1=img_1)

    return res

@app.route('/make_n3', methods=['GET'])
def make_number_n3():
    if request.method == 'GET':
        numbers3 = make_random_n3(prob_100_n3, prob_10_n3, prob_1_n3)

        img_100 = 'static/src/' + str(numbers3[0]) + '.png'
        img_10 = 'static/src/' + str(numbers3[1]) + '.png'
        img_1 = 'static/src/' + str(numbers3[2]) + '.png'
        res = render_template("numbers3.html", img_100=img_100, img_10=img_10, img_1=img_1)

        return res

@app.route('/n4')
def display_number_n4():
    img_1000 = 'static/src/0.png'
    img_100 = 'static/src/0.png'
    img_10 = 'static/src/0.png'
    img_1 = 'static/src/0.png'
    res = render_template("numbers4.html", img_1000=img_1000, img_100=img_100, img_10=img_10, img_1=img_1)

    return res

@app.route('/make_n4', methods=['GET'])
def make_number_n4():
    if request.method == 'GET':
        numbers4 = make_random_n4(prob_1000_n4, prob_100_n4, prob_10_n4, prob_1_n4)

        img_1000 = 'static/src/' + str(numbers4[0]) + '.png'
        img_100 = 'static/src/' + str(numbers4[1]) + '.png'
        img_10 = 'static/src/' + str(numbers4[2]) + '.png'
        img_1 = 'static/src/' + str(numbers4[3]) + '.png'
        res = render_template("numbers4.html", img_1000=img_1000, img_100=img_100, img_10=img_10, img_1=img_1)

        return res
        

    

if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=80)