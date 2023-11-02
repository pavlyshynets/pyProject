from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/api/v1/hello-world-17')
def hello_world():
    return 'Hello World 17', 200

# if __name__ == '__main__':
    # app.run(debug=True)

serve(app, host='0.0.0.0', port=8000)

# http://127.0.0.1:5000/api/v1/hello-world-17
# http://127.0.0.1:8000/api/v1/hello-world-17

# waitress-serve --port=8000 main.py:app
