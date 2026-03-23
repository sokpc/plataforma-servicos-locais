from flask import Flask, render_template, request

app = Flask(__name__)

# Lista completa de profissionais (Baseada no seu Design do Figma)
profissionais = [
    {"id": 1, "nome": "João da Silva", "servico": "Pedreiro", "bairro": "Centro", "emoji": "🧱", "whats": "11999999001"},
    {"id": 2, "nome": "Maria Souza", "servico": "Manicure", "bairro": "Vila Nova", "emoji": "💅", "whats": "11999999002"},
    {"id": 3, "nome": "Carlos Auto", "servico": "Mecânico", "bairro": "São João", "emoji": "🔧", "whats": "11999999003"},
    {"id": 4, "nome": "Ana Costa", "servico": "Eletricista", "bairro": "Centro", "emoji": "⚡", "whats": "11999999004"},
    {"id": 5, "nome": "Pedro Santos", "servico": "Encanador", "bairro": "Vila Nova", "emoji": "🚰", "whats": "11999999005"},
    {"id": 6, "nome": "Juliana Lima", "servico": "Cabeleireira", "bairro": "São João", "emoji": "💇", "whats": "11999999006"}
]

@app.route('/')
def index():
    # Pega o que o usuário digitou na busca
    termo_busca = request.args.get('busca', '').lower()
    
    # Filtra a lista se houver uma busca
    if termo_busca:
        resultados = [
            p for p in profissionais 
            if termo_busca in p['nome'].lower() 
            or termo_busca in p['servico'].lower() 
            or termo_busca in p['bairro'].lower()
        ]
    else:
        resultados = profissionais

    return render_template('index.html', profissionais=resultados)

if __name__ == '__main__':
    app.run(debug=True)