from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "API DevOps PUC - Funcionando no Docker!"

# +++ ADICIONE ISSO +++
@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)