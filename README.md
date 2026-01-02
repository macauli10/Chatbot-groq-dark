# Missouri ChatBot - Assistente IA com Groq API

Um chatbot inteligente desenvolvido com Flask e Groq API, apresentando uma interface moderna com tema dark e efeitos visuais.

## 🚀 Funcionalidades

- 💬 Chat em tempo real com IA utilizando a Groq API
- 🎨 Interface moderna com tema dark e efeitos de partículas
- ⚡ Respostas rápidas usando modelos de última geração
- 📱 Design responsivo para desktop e mobile
- 🔒 Gerenciamento seguro de chaves de API via variáveis de ambiente

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **IA**: Groq API
- **Efeitos Visuais**: Particles.js
- **Fontes**: Font Awesome

## 📁 Estrutura do Projeto

```
missouri-chatbot/
├── app.py                    # Aplicação Flask principal
├── requirements.txt          # Dependências Python
├── .env                     # Variáveis de ambiente (não versionado)
├── .env.example            # Template das variáveis de ambiente
├── .gitignore              # Arquivos ignorados pelo Git
└── templates/
    └── index.html          # Interface do chatbot
```

## 🚀 Como Executar

### 1. Pré-requisitos

- Python 3.8 ou superior
- Conta na [Groq Cloud](https://console.groq.com/) para obter uma API key

### 2. Clonar e Configurar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/missouri-chatbot.git
cd missouri-chatbot

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua API key da Groq
nano .env  # ou use seu editor preferido
```

Conteúdo do `.env`:
```env
GROQ_API_KEY=sua_chave_aqui
SECRET_KEY=sua_chave_secreta_flask
FLASK_ENV=development
```

### 4. Executar a Aplicação

```bash
# Execute o servidor Flask
python app.py
```

### 5. Acessar a Aplicação

Abra seu navegador e acesse: [http://localhost:5000](http://localhost:5000)

## 🔧 Configuração da API Groq

1. Acesse [Groq Cloud Console](https://console.groq.com/)
2. Crie uma conta ou faça login
3. Gere uma nova API key
4. Copie a key e cole no arquivo `.env`

## 🌟 Características da Interface

- **Tema Dark Moderno**: Cores escuras com acentos azul neon
- **Partículas Animadas**: Efeitos visuais interativos de fundo
- **Design Responsivo**: Adaptado para diferentes tamanhos de tela
- **Feedback Visual**: Indicadores de status e animações
- **Histórico de Conversa**: Mensagens com timestamp

## 🎯 Modelos Disponíveis

O projeto utiliza por padrão o modelo `mixtral-8x7b-32768`, mas pode ser configurado para usar outros modelos da Groq como:
- `llama2-70b-4096`
- `llama3-70b-8192`
- `gemma-7b-it`

## 📝 Uso

1. Digite sua mensagem no campo de entrada
2. Pressione Enter ou clique no botão de enviar
3. Aguarde a resposta da IA
4. Continue a conversa normalmente

## 🔒 Segurança

- API key armazenada em variáveis de ambiente
- Arquivo `.env` adicionado ao `.gitignore`
- Validação de entrada no backend
- Tratamento de erros robusto

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ✨ Demonstração de Habilidades

Este projeto demonstra habilidades em:
- Desenvolvimento Full Stack com Flask
- Integração com APIs de terceiros
- Interface de usuário moderna
- Gerenciamento de dependências
- Versionamento de código

---

