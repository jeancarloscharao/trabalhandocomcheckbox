from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    alternativas = [*range(1, 100)]
    print(alternativas)
    return render_template('index.html', alternativas=alternativas)


@app.route('/confirma-voto', methods=['POST'])
def confirma_voto():
    alternativas = []

    print(len(request.form.getlist('alternativa')))

    print(request.form.getlist('alternativa'))



    for alternativa in request.form.getlist('alternativa'):
        alternativas.append(alternativa)


    return render_template('confirma-voto.html',alternativas=alternativas)



app.debug = True
app.run(host='0.0.0.0')