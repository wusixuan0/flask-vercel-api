import os
from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return {"message": "Hello"}

if 'VERCEL' in os.environ:
    app = app.wsgi_app

if __name__ == '__main__':
    app.run(debug=True)