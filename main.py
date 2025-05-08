
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

questions = [
    "Você já reparou como a luz entra pela janela de um quarto escuro em certos momentos do dia? O que acontece com a claridade e com as sombras dentro do ambiente?",
    "Imagine que você está olhando para um espelho pequeno segurando uma lanterna. O que acha que aconteceria se você mudasse o ângulo do espelho? Descreva com suas palavras.",
    "Se colocarmos um objeto em frente a uma fonte de luz forte (como uma lanterna), o que você acha que acontece com a luz? Ela passa pelo objeto, para, muda de caminho...? Por quê?",
    "Você acha que é possível ver sem que haja luz? Por quê? Dê um exemplo que justifique sua resposta.",
    "Você já viu luz 'dobrar' ou mudar de direção em alguma situação? O que aconteceu? Onde foi?"
]

@app.route('/')
def index():
    session['answers'] = []
    return redirect(url_for('question', q=1))

@app.route('/question/<int:q>', methods=['GET', 'POST'])
def question(q):
    if request.method == 'POST':
        answer = request.form['answer']
        session['answers'].append(answer)
        session.modified = True
        if q < len(questions):
            return redirect(url_for('question', q=q+1))
        else:
            return redirect(url_for('thank_you'))
    return render_template(f'question{q}.html', question=questions[q-1], q=q)

@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')
