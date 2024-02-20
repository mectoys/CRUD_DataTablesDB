from flask import Flask, render_template
from views import viewProject

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.register_blueprint(viewProject.main, url_prefix='/')
    app.run(host='0.0.0.0', port=5004, debug=True)
