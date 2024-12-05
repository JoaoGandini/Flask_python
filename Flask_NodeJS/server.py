"""
@file server.py
@description O script define uma API usando Flask para calcular números primos em um intervalo especificado.
A API recebe os limites inferior e superior como parâmetros de consulta em uma requisição GET
ao endpoint `/primos`.

@dependencies Flask - Framework para criação de aplicações web.
"""
from flask import Flask, request, jsonify

# Inicializa a aplicação Flask
app = Flask(__name__)

# Função utilizada para calcular números primos em um intervalo
def calcular_primos(limite_inferior, limite_superior):
    primos = []                                               # Lista para armazenar os números primos
    for num in range(limite_inferior, limite_superior + 1):   # Itera números no intervalo
        if num > 1:                                           # Se Números primos são maiores que 1
            for i in range(2, int(num ** 0.5) + 1):           # Verifica divisibilidade até a raiz quadrada
                if num % i == 0:                              # verifica se i divide num    
                    break
            else:
                primos.append(num)                            # Adiciona à lista se for primo
    return primos


"""
    @function func_primos
    @description Endpoint para receber números primos em um intervalo.
    Recebe os parâmetros de consulta `limite_inferior` e `limite_superior` e retorna os números primos no intervalo.
    @return JSON - Resposta contendo os números primos ou mensagem de erro.
"""
# Define a rota principal da API
@app.route('/primos', methods=['GET'])
def func_primos():
    try:
        limite_inferior = int(request.args.get('limite_inferior'))
        limite_superior = int(request.args.get('limite_superior'))
        
        # Verifica se os limites são válidos
        if limite_inferior > limite_superior:
            return jsonify({"erro": "Limite inferior maior que o superior"}), 400  # Resposta de erro HTTP 400

        primos = calcular_primos(limite_inferior, limite_superior)
        return jsonify({"primos": primos})  # Retorna a lista de primos como resposta JSON
    
    except ValueError:
        return jsonify({"erro": "Parâmetros inválidos"}), 400 # Erro de parametros inválidos, Bad Request
    except Exception as e:
        return jsonify({"erro": str(e)}), 500 # Erro genérico não tratado

# Parte Main da aplicação
if __name__ == '__main__':
    # Executa a aplicação Flask no modo de depuração
    app.run(debug=True)