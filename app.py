from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler  # ou MinMaxScaler, dependendo do que você usou

app = Flask(__name__)

# Carregar o modelo treinado
with open('modelo_arvore_decisao_otimizado.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Carregar o scaler (caso você tenha usado StandardScaler ou MinMaxScaler no treinamento)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obter os dados do formulário enviados pelo HTML
        dados = [float(request.form.get(key)) for key in [
            'no_of_dependents', 'income_annum', 'loan_amount', 'loan_term',
            'cibil_score', 'residential_assets_value', 'commercial_assets_value',
            'luxury_assets_value', 'bank_asset_value', 'education__Not_Graduate',  # Nome atualizado
            'self_employed__Yes'
        ]]

        dados_teste = np.array(dados).reshape(1, -1)

        # Normalizar os dados usando o mesmo scaler que foi usado no treinamento
        dados_teste_normalizados = scaler.transform(dados_teste)

        # Fazer a predição usando o modelo treinado
        predicao = modelo.predict(dados_teste_normalizados)

        # Exibir diretamente o valor retornado pelo modelo ('Approved' ou 'Rejected')
        resultado = predicao[0]

        return render_template('index.html', prediction_text=resultado)

    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

