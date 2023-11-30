from flask import Flask, jsonify, request

app = Flask(__name__) # __name__ guarda o nome do arquivo

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n-1)

def termo_fibonacci(n):
    if n <= 1:
        return n
    else:
        return termo_fibonacci(n-1) + termo_fibonacci(n-2) 

titulo = 'Trabalho 4 SEL0456\n Eduardo Rocha Lima Jorge\n N° USP: 12547722'

@app.route('/')
def index(): #tem como objetivo retornar uma string que será retornada ao cliente
    return titulo


@app.route('/calculos', methods=['POST','GET'])
def calculos():
    if request.method == 'GET':
        return "Bem vindo à página de cálculos. Envie uma solicitação POST, com dados JSON, que será calculado o fatorial ou fibonacci conforme desejado!"

    dados_entrada = request.get_json()

    if 'operacao' not in dados_entrada or 'valor' not in dados_entrada:
        return jsonify({'erro': 'Forneça o tipo (fatorial ou fibonacci) e o número na solicitação JSON.'}), 400

    operacao = dados_entrada['operacao']
    valor = dados_entrada['valor']

    if operacao == 'fatorial':
        resultado = calcular_fatorial(valor)
        sequencia = [calcular_fatorial(i) for i in range(valor + 1)]
    elif operacao == 'fibonacci':
        resultado = termo_fibonacci(valor)
        sequencia = [termo_fibonacci(i) for i in range(valor + 1)]
    else:
        return jsonify({'erro': 'Tipo de cálculo não suportado. Use "fatorial" ou "fibonacci".'}), 400

    return jsonify({'resultado': resultado, 'sequencia': sequencia})

if __name__ == '__main__':
    app.run(debug=True)


#FIz a sequencia Fib e tenho q ver como colocar ele para retornar na linha 48 e 52