from flask import Flask, render_template, request, jsonify
import evaluate_faces
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/select/')
def select():
    return render_template("select.html")

@app.route('/play/')
def play():
    num = request.args.get("num")
    img = num + ".jpg"
    print (img)
    return render_template("play.html", img_name=img)

@app.route('/compute/', methods=['GET','POST'])
def compute():
    if request.method == 'POST':
        image = request.files.get('file', '')
        stockimg = "static/" + request.form.get("img_name")
        image.save("./snapshot.jpg")
        score, escore, fscore = evaluate_faces.evaluate_faces(stockimg, "snapshot.jpg")
    data = {"total" : score,
            "escore" : escore,
            "fscore" : fscore}
    return jsonify(data)

@app.route('/end/')
def end():
    score = request.args.get('score')

    escore = request.args.get('escore')
    fscore = request.args.get('fscore')
    print (score)
    print (type(score))
    return render_template("end.html", emotional_score=score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
