import os

VERSION = "0.0.1"
DESCRIPTION = "A lib to manage your flask projects"

def criar_projeto_flask(nome_projeto):
    # Cria a pasta do projeto
    os.makedirs(nome_projeto)
    
    # Cria os arquivos dentro da pasta do projeto
    with open(os.path.join(nome_projeto, 'README.md'), 'w') as f:
        f.write("# Meu Projeto Flask\n\nEste é um projeto Flask básico.")
    
    with open(os.path.join(nome_projeto, '.gitignore'), 'w') as f:
        f.write("# Arquivos e pastas a serem ignorados pelo Git")
    
    with open(os.path.join(nome_projeto, 'main.py'), 'w') as f:
        f.write('''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
''')
    
    # Cria a pasta 'templates' dentro do projeto
    os.makedirs(os.path.join(nome_projeto, 'templates'))
    
    # Cria o arquivo 'index.html' dentro da pasta 'templates'
    with open(os.path.join(nome_projeto, 'templates', 'index.html'), 'w') as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n    <title>Index</title>\n</head>\n<body>\n    <h1>Hello, world!</h1>\n</body>\n</html>")
    
    print(f"Projeto '{nome_projeto}' criado com sucesso!")