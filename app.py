from flask import Flask, render_template, request, jsonify, send_file
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
app = Flask(__name__)
from forms import NumberInput, NumberInput_1
import os
matplotlib.use('Agg')
valores_formulario = {}
valores_formulario_1 = {}

app.config['SECRET_KEY'] = 'hqwidh1728eg'












@app.route('/', methods=['GET', 'POST'])
def index():
    number_input = NumberInput()
    number_input_1 = NumberInput_1()
    
    if request.method == 'POST':
        if 'submit_segundo_grau' in request.form:
            a = float(request.form['num_a'])
            b = float(request.form['num_b'])
            c = float(request.form['num_c'])
            valores_formulario['b'] = b
            valores_formulario['c'] = c
            gerar_grafico(a, b, c)
            return render_template('index.html', number_input=number_input, number_input_1=number_input_1)
        
        elif 'submit_primeiro_grau' in request.form:
            a_1 = float(request.form['num_a_1'])
            b_1 = float(request.form['num_b_1'])
            valores_formulario_1['a'] = a_1
            valores_formulario_1['b'] = b_1
            gerar_grafico_1(a_1, b_1)
            return render_template('index.html', number_input=number_input, number_input_1=number_input_1)
        
    return render_template('index.html', number_input=number_input, number_input_1=number_input_1)



@app.route('/download-image')
def download_image():
    # Caminho para a imagem que você deseja baixar
    image_path = 'static/img/grafico.png'
    # Nome do arquivo que será baixado pelo usuário
    filename = 'grafico.png'
    # Retorna a imagem para o cliente fazer o download
    return send_file(image_path, as_attachment=True)

@app.route('/download-image_1')
def download_image_1():
    # Caminho para a imagem que você deseja baixar
    image_path = 'static/img/grafico_1.png'
    # Nome do arquivo que será baixado pelo usuário
    filename = 'grafico_1.png'
    # Retorna a imagem para o cliente fazer o download
    return send_file(image_path, as_attachment=True)

def gerar_grafico(a, b , c):
    x_vals = np.linspace(-10, 10, 100)
    y_vals = a*x_vals**2 + b*x_vals + c
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_vals, y_vals, label='Função Quadrática', linestyle='--')
    ax.set_title('Gráfico da função quadrática')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='r', linewidth=1)
    plt.axvline(0, color='r', linewidth=1)
    ax.set_xlim([-20, 20])  # Limites no eixo x de -10 a 10
    ax.set_ylim([-50, 100])  # Limites no eixo y de -50 a 50

    plt.grid(True)
    #ax.set(xlim=(-10, 10), ylim=(-10, 10))

    
    # Verifica se o diretório 'static/img' existe e cria-o se não existir
    if not os.path.exists('static/img'):
        os.makedirs('static/img')
    
    # Salva a imagem do gráfico no diretório especificado
    plt.savefig('static/img/grafico.png')  # Salvando o gráfico como um arquivo de imagem
    plt.close()

def gerar_grafico_1(a_1, b_1 ):
    x_vals = np.linspace(-10, 10, 100)
    y_vals = a_1*x_vals *  b_1
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_vals, y_vals, label='Função Afim', linestyle='--')
    ax.set_title('Gráfico da função Afim')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='r', linewidth=1)
    plt.axvline(0, color='r', linewidth=1)
    ax.set_xlim([-20, 20])  # Limites no eixo x de -10 a 10
    ax.set_ylim([-50, 100])  # Limites no eixo y de -50 a 50

    plt.grid(True)
    #ax.set(xlim=(-10, 10), ylim=(-10, 10))

    
    # Verifica se o diretório 'static/img' existe e cria-o se não existir
    if not os.path.exists('static/img'):
        os.makedirs('static/img')
    
    # Salva a imagem do gráfico no diretório especificado
    plt.savefig('static/img/grafico_1.png')  # Salvando o gráfico como um arquivo de imagem
    plt.close()




















if __name__ == '__main__':
    app.run(debug=True)