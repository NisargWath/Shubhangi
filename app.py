from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Gallery')
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)