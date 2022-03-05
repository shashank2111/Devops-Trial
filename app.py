from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='localhost', port=port,debug=True)