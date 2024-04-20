from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
app = Flask(__name__)
from forms import NumberInput
import os
matplotlib.use('Agg')
valores_formulario = {}


app.config['SECRET_KEY'] = 'hqwidh1728eg'












@app.route('/', methods=['GET', 'POST'])
def index():
    number_input = NumberInput()
    if request.method == 'POST':
        a = float(request.form['num_a'])
        b = float(request.form['num_b'])
        c = float(request.form['num_c'])
        valores_formulario['a'] = a
        valores_formulario['b'] = b
        valores_formulario['c'] = c
        gerar_grafico(a, b, c)  # Chamando a função para gerar o gráfico
        return render_template('index.html', number_input=number_input)
    return render_template('index.html', number_input=number_input)

    

def gerar_grafico(a, b , c):
    x_vals = np.linspace(-10, 10, 100)
    y_vals = a*x_vals**2 + b*x_vals + c

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_vals, y_vals, label='Função Quadrática', linestyle='--')
    ax.set_title('Gráfico da função quadrática')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    
    # Verifica se o diretório 'static/img' existe e cria-o se não existir
    if not os.path.exists('static/img'):
        os.makedirs('static/img')
    
    # Salva a imagem do gráfico no diretório especificado
    plt.savefig('static/img/grafico.png')  # Salvando o gráfico como um arquivo de imagem
    plt.close()




















if __name__ == '__main__':
    app.run(debug=True)