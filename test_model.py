import numpy as np
from sklearn.metrics import accuracy_score
import pickle

# Carregar o modelo treinado
with open('modelo_arvore_decisao_otimizado.pkl', 'rb') as f:
    arvore_otimizada = pickle.load(f)

# Carregar o scaler treinado para normalizar os dados
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Definir a acurácia mínima aceitável
ACURACIA_MINIMA = 0.90  # Valor que você deseja como mínimo para passar no teste

# Dados fornecidos para o teste
dados_teste = np.array([
    [0, 4500000, 11500000, 14, 509, 13400000, 2300000, 15400000, 5900000, 1, 1],  # Rejected
    [5, 8800000, 29300000, 10, 560, 16800000, 13900000, 31100000, 9900000, 0, 0],  # Approved
    [3, 3000000, 7500000, 6, 881, 1400000, 4500000, 6100000, 2300000, 0, 1],      # Approved
    [5, 1300000, 3000000, 20, 540, 1000000, 2300000, 3200000, 1900000, 0, 0],     # Rejected
    [3, 5000000, 12700000, 14, 865, 4700000, 8100000, 19500000, 6300000, 0, 0],   # Approved
    [5, 1000000, 2300000, 12, 317, 2800000, 500000, 3300000, 800000, 1, 1],       # Rejected
    [0, 3300000, 11300000, 20, 559, 4200000, 2900000, 11000000, 1900000, 1, 1],   # Approved
    [2, 6500000, 23900000, 18, 457, 1200000, 12400000, 18100000, 7300000, 1, 0],  # Rejected
    [1, 4100000, 12800000, 8, 780, 8200000, 700000, 14100000, 5800000, 1, 0],     # Approved
    [1, 9200000, 29700000, 10, 607, 17800000, 11800000, 35700000, 12000000, 0, 0] # Approved
])

# Rótulos esperados para esses dados de teste (incluindo espaço no início)
labels_esperados = np.array([
    ' Rejected', ' Approved', ' Approved', ' Rejected', ' Approved', 
    ' Rejected', ' Approved', ' Rejected', ' Approved', ' Approved'
])

# Função para testar a acurácia do modelo
def test_acuracia_modelo():
    # Normalizar os dados de teste
    dados_teste_normalizados = scaler.transform(dados_teste)

    # Fazer a predição usando o modelo treinado
    predicoes = arvore_otimizada.predict(dados_teste_normalizados)

    # Calcular a acurácia do modelo
    acuracia = accuracy_score(labels_esperados, predicoes)

    # Verificar se a acurácia atende ao valor mínimo
    assert acuracia >= ACURACIA_MINIMA, f"A acurácia {acuracia:.4f} está abaixo do mínimo esperado ({ACURACIA_MINIMA:.2f})"
    
    # Mostrar a acurácia no terminal, mesmo que o teste passe
    print(f"Acurácia: {acuracia:.4f}")
