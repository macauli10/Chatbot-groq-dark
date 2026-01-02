# app.py atualizado
from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configure sua API key da Groq aqui a partir do .env
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', 'chave-padrao-seguranca')

# Configura a chave secreta do Flask para sessões
app.secret_key = SECRET_KEY

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mensagem vazia'}), 400
        
        # Verifica se a API key está configurada
        if not GROQ_API_KEY or GROQ_API_KEY == "GROQ_API_KEY":
            return jsonify({
                'error': 'API key não configurada. Configure a variável GROQ_API_KEY no arquivo .env'
            }), 500
        
        # Configuração do cabeçalho da API Groq
        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Corpo da requisição para a Groq
        payload = {
            'model': 'llama-3.1-8b-instant',  # ou outro modelo da Groq
            'messages': [
                {'role': 'system', 'content': 'Você é um assistente útil.'},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7,
            'max_tokens': 1024
        }
        
        # Faz a requisição para a API Groq
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            bot_response = result['choices'][0]['message']['content']
            return jsonify({'response': bot_response})
        else:
            error_detail = "Erro desconhecido"
            try:
                error_detail = response.json().get('error', {}).get('message', str(response.status_code))
            except:
                error_detail = str(response.status_code)
            
            return jsonify({
                'error': f'Erro na API Groq: {error_detail}'
            }), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Erro de conexão com a API Groq. Verifique sua internet.'}), 500
    except Exception as e:
        app.logger.error(f'Erro no servidor: {str(e)}')
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500

# Rota de verificação de saúde da API
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'groq_configured': bool(GROQ_API_KEY and GROQ_API_KEY != "GROQ_API_KEY"),
        'app': 'Chatbot com Groq API'
    })

if __name__ == '__main__':
    # Configurações de host e porta também podem vir do .env
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)