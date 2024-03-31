from run import Flask

app = Flask(__name__)


@app.route('/')
def f():
    return 'fffffffff'


if __name__ == '__main__':
    app.run(debug=True)
