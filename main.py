from flask import Flask, render_template, request, redirect
app = Flask(__name__)

games = []


@app.route('/')
def index():
    return render_template('index.html', games=games)


@app.route('/adicionar_jogo', methods=['GET', 'POST'])
def adicionar_jogo():

    if request.method == 'POST':
        nomejogo = request.form['nomejogo']
        genero = request.form['genero']
        desenvol = request.form['desenvol']
        codigo = len(games)
        games.append([codigo, nomejogo, genero, desenvol])
        return redirect('/')
    else:
        return render_template('adicionar_jogo.html')


@app.route('/editar_jogo/<int:codigo>', methods=['GET', 'POST'])
def editar_jogo(codigo):

    if request.method == 'POST':
        nomejogo = request.form['nomejogo']
        genero = request.form['genero']
        desenvol = request.form['desenvol']
        games[codigo] = [codigo, nomejogo, genero, desenvol]
        return redirect('/')
    else:
        jogo = games[codigo]
        return render_template('editar_jogo.html', jogo=jogo)


@app.route('/apagar_jogo/<int:codigo>')
def apagar_jogo(codigo):
    del games[codigo]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
