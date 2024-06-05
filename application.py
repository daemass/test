from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is your Flask application running on Elastic Beanstalk with Python 3.7!'

if __name__ == '__main__':
    app.run(debug=True)
